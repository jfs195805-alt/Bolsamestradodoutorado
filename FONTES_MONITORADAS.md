# 📡 Fontes monitoradas — regras de raspagem diária

Estas fontes são **re-raspadas automaticamente todos os dias** pelo agente de pesquisa (agendamento diário às 11h UTC). O resultado alimenta `bolsas.csv` e o app.

## 🔒 Regra fixa — scholarshippk (serve para TODOS nós)
- **Fonte:** https://www.linkedin.com/company/scholarshippk/
- **Regra:** **re-raspar todos os dias** e trazer também o **histórico dos últimos 3 meses**.
- **Uso:** as oportunidades desta fonte **servem para todos da família** (Rafael, Maria Eduarda, Daniela, Letícia e amigos) — classificar cada bolsa por quem se encaixa (nível, idade, área, elegibilidade a brasileiros).
- **⚠️ Limitação técnica honesta:** o LinkedIn e o site `scholarshippk.com` **bloqueiam acesso automatizado (HTTP 403 / muro de login)** a partir deste ambiente — não há como raspar o HTML diretamente sem uma conta/credencial do LinkedIn. Enquanto não houver um acesso autenticado, o agente diário busca o **mesmo conteúdo por vias indexáveis** (WebSearch pelo nome de cada bolsa que a scholarshippk divulga, portais oficiais das bolsas) e adiciona ao repositório apenas o que for **verificável na fonte oficial** (nunca inventar prazo/valor).
- **Como destravar a raspagem direta (opcional):** fornecer um acesso autenticado ao LinkedIn (cookie/sessão) ou um serviço MCP de scraping autorizado — aí o agente passa a ler os posts diretamente.

## 🔒 Regra fixa — opportunityportal.info (o portal deles; serve para TODOS)
- **Fonte:** https://opportunityportal.info/ — **entrar em TODOS os links do site** (é onde ficam as bolsas em geral que a scholarshippk divulga).
- **Regra:** **re-raspar todos os dias** e trazer o histórico recente.
- **Uso:** oportunidades servem para **todos da família** — classificar por quem se encaixa.
- **⚠️ Limitação:** o site também **bloqueia automação (HTTP 403)** a partir deste ambiente. O agente diário busca cada bolsa por vias indexáveis (WebSearch) e adiciona só o verificável na fonte oficial. Destravar = acesso autenticado / MCP de scraping autorizado.

## Bolsas-bandeira já capturadas via busca (o tipo que esses portais divulgam)
MEXT 🇯🇵 · GKS 🇰🇷 · Türkiye Bursları 🇹🇷 · Stipendium Hungaricum 🇭🇺 · Chevening/Commonwealth 🇬🇧 · Fulbright 🇺🇸 · DAAD 🇩🇪 · Erasmus Mundus 🇪🇺 · CSC 🇨🇳 · KAUST/MBZUAI 🌍 — já no `bolsas.csv`.

## Outras fontes já mapeadas
- scholarshipdreamss.com · Hanjo Foundation (Japão) · Opportunity Desk · ScholarshipsAds · agregadores e portais oficiais por país/continente (ver `RELATORIO.md`).

> Regra Zero: nada de dados inventados. Toda bolsa entra só com prazo/valor conferidos na fonte oficial; estimativas ficam marcadas.
