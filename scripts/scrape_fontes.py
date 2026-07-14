#!/usr/bin/env python3
"""
Raspador das fontes fixas (scholarshippk / opportunityportal.info).

Pré-requisito: acesso de rede externo liberado no ambiente. Enquanto a política
de rede estiver restrita (proxy nega CONNECT), TODAS as estratégias falham — o
script detecta isso e explica. Assim que a rede abrir, ele funciona sem mudanças.

Estratégias, em ordem (da mais barata à mais robusta):
  1) API REST WordPress (/wp-json/wp/v2/posts) via HTTP simples
  2) RSS (/feed/) via HTTP simples
  3) Navegador real (Playwright + Chromium do ambiente, através do proxy)

Uso:
  python3 scripts/scrape_fontes.py                 # opportunityportal.info
  python3 scripts/scrape_fontes.py <url> [maxpags] # outra fonte / paginação
Saída: JSON no stdout com {source, strategy, posts:[{title,link,date,excerpt}]}.
Nunca inventa dados — só reporta o que a fonte devolve. Verificar prazo/valor na
fonte oficial antes de gravar em bolsas.csv (Regra Zero).
"""
import os, sys, json, glob, urllib.request, urllib.error

DEFAULT = "https://opportunityportal.info"
UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36")


def _http_get(url, timeout=30):
    req = urllib.request.Request(url, headers={
        "User-Agent": UA, "Accept": "application/json, text/xml, */*",
        "Accept-Language": "en-US,en;q=0.9",
    })
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return r.read().decode("utf-8", "replace")


def via_wp_json(base, maxpages=3):
    posts = []
    for pg in range(1, maxpages + 1):
        url = f"{base}/wp-json/wp/v2/posts?per_page=25&page={pg}&_fields=title,link,date,excerpt"
        data = json.loads(_http_get(url))
        if not data:
            break
        for p in data:
            posts.append({
                "title": (p.get("title", {}) or {}).get("rendered", "").strip(),
                "link": p.get("link", ""),
                "date": p.get("date", ""),
                "excerpt": (p.get("excerpt", {}) or {}).get("rendered", "")[:400],
            })
    return posts


def via_rss(base):
    import xml.etree.ElementTree as ET
    xml = _http_get(f"{base}/feed/")
    root = ET.fromstring(xml)
    posts = []
    for item in root.iter("item"):
        g = lambda t: (item.findtext(t) or "").strip()
        posts.append({"title": g("title"), "link": g("link"),
                      "date": g("pubDate"), "excerpt": g("description")[:400]})
    return posts


def _chrome_path():
    for pat in ("/opt/pw-browsers/chromium-*/chrome-linux/chrome",
                "/opt/pw-browsers/chromium_headless_shell-*/chrome-linux/headless_shell"):
        hits = sorted(glob.glob(pat))
        if hits:
            return hits[-1]
    return None


def via_browser(base, maxpages=3):
    from playwright.sync_api import sync_playwright
    proxy = os.environ.get("HTTPS_PROXY") or os.environ.get("HTTP_PROXY")
    chrome = _chrome_path()
    posts, seen = [], set()
    with sync_playwright() as p:
        launch = dict(headless=True, args=[
            "--no-sandbox", "--disable-blink-features=AutomationControlled",
            "--ignore-certificate-errors"])
        if chrome:
            launch["executable_path"] = chrome
        if proxy:
            launch["proxy"] = {"server": proxy}
        b = p.chromium.launch(**launch)
        ctx = b.new_context(user_agent=UA, locale="en-US",
                            viewport={"width": 1366, "height": 900})
        page = ctx.new_page()
        for pg in range(1, maxpages + 1):
            url = base if pg == 1 else f"{base}/page/{pg}/"
            try:
                page.goto(url, wait_until="domcontentloaded", timeout=45000)
                page.wait_for_timeout(3000)
            except Exception as e:
                if pg == 1:
                    raise
                break
            links = page.eval_on_selector_all(
                "article a[href], h2 a[href], h3 a[href], .entry-title a[href]",
                "els => els.map(e => ({t:(e.innerText||'').trim(), h:e.href}))")
            for l in links:
                if l["h"] not in seen and len(l["t"]) > 12:
                    seen.add(l["h"])
                    posts.append({"title": l["t"], "link": l["h"], "date": "", "excerpt": ""})
        b.close()
    return posts


def main():
    base = (sys.argv[1] if len(sys.argv) > 1 else DEFAULT).rstrip("/")
    maxpages = int(sys.argv[2]) if len(sys.argv) > 2 else 3
    errors = {}
    for name, fn in (("wp-json", lambda: via_wp_json(base, maxpages)),
                     ("rss", lambda: via_rss(base)),
                     ("browser", lambda: via_browser(base, maxpages))):
        try:
            posts = fn()
            if posts:
                print(json.dumps({"source": base, "strategy": name,
                                  "count": len(posts), "posts": posts},
                                 ensure_ascii=False, indent=2))
                return 0
        except Exception as e:
            errors[name] = f"{type(e).__name__}: {e}"[:200]
    print(json.dumps({"source": base, "strategy": None, "count": 0,
                      "posts": [], "errors": errors,
                      "hint": "Rede provavelmente ainda bloqueada (proxy nega CONNECT) "
                              "ou site com Cloudflare. Ver FONTES_MONITORADAS.md."},
                     ensure_ascii=False, indent=2))
    return 1


if __name__ == "__main__":
    sys.exit(main())
