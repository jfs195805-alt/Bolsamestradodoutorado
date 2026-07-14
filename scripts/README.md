# scripts/

## `scrape_fontes.py` — raspador das fontes fixas (foco: **opportunityportal.info**)

Lê os posts de bolsas do site deles e imprime JSON (`{source, strategy, count, posts:[{title,link,date,excerpt}]}`).

### Rodar
```bash
pip install --quiet playwright        # a lib; o Chromium já vem no ambiente
python3 scripts/scrape_fontes.py                      # opportunityportal.info (padrão)
python3 scripts/scrape_fontes.py https://opportunityportal.info 5   # 5 páginas
```

### Estratégias (tenta em ordem)
1. **API REST WordPress** `/wp-json/wp/v2/posts` (mais barata)
2. **RSS** `/feed/`
3. **Navegador real** (Playwright + Chromium do ambiente, através do proxy `HTTPS_PROXY`)

### ⚠️ Pré-requisito de rede
Enquanto a **política de rede do ambiente** estiver restrita, o proxy nega o CONNECT (403) e as três estratégias falham — o script devolve `strategy: null` + `errors` + `hint`. **Assim que a rede externa for liberada** (config. do ambiente no Claude Code na web), o script funciona sem alteração. Detalhes e caminhos alternativos em `../FONTES_MONITORADAS.md`.

### Depois de raspar
Processar o JSON e, para cada bolsa **nova e verificada na fonte oficial**, acrescentar em `../bolsas.csv` (10 colunas) e encaixar na pessoa certa em `../candidaturas/` (mantendo o ranking). **Regra Zero: nada de prazo/valor inventado.**
