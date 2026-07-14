# 🎓 Agenda de Bolsas — Mestrado & Doutorado

Sistema para **acompanhar prazos, documentos, status e valores** de bolsas de mestrado e doutorado
**do mundo todo**, com um filtro de qualidade: só entram bolsas com **auxílio mensal em dinheiro acima de US$ 1.000/mês**.
A base é atualizada **automaticamente todos os dias** por um agente de pesquisa.

## O que tem aqui

| Arquivo | O que é |
|---|---|
| **`bolsas.csv`** | A base de dados (41+ bolsas). Fácil de editar no Excel/Google Sheets e versionada no Git. `valor_mensal` está em USD. |
| **`RELATORIO.md`** | Panorama da última rodada: bolsas agrupadas por urgência de prazo e por região, com destaque para as que fecham em breve. |
| **`index.html`** | App web visual: calendário/lista com contagem regressiva, checklist de documentos, filtros e estatísticas. |

## Como usar

### Ver os dados rápido
- Abra o **`bolsas.csv`** (planilha) ou o **`RELATORIO.md`** (relatório pronto) direto aqui no GitHub.

### App web visual (`index.html`)
- **Melhor experiência:** hospede a pasta (ex.: **GitHub Pages**) e abra o `index.html` — ele carrega automaticamente todas as bolsas do `bolsas.csv`.
- **Abrindo do disco (dois cliques):** por segurança do navegador, o carregamento automático não funciona via `file://`. Clique em **📥 Importar CSV** e selecione o `bolsas.csv` para carregar tudo.
- Botão **🔄 Sincronizar bolsas.csv** recarrega a base a qualquer momento.
- Marque os documentos conforme for reunindo (checklist). Os dados ficam salvos no seu navegador (localStorage).

> Cores dos cartões por urgência do prazo:
> 🟢 tranquilo · 🟠 ≤30 dias · 🔴 ≤7 dias · ⚪ encerrado · 🔵 enviado/aprovado

## Filtro aplicado
- ✅ **Incluídas:** bolsas do mundo todo com auxílio mensal **> US$ 1.000/mês**, mestrado/doutorado, abertas a internacionais/brasileiros.
- ❌ **Excluídas:** estipêndios baixos (China CSC, Coreia GKS, Turquia, Índia, Colômbia, Romênia...) e programas que **não pagam mensalidade em dinheiro** (Orange Tulip, Instituto Ling, Fundação Estudar — valor único ou só desconto de taxa). Ver detalhes no `RELATORIO.md`.

## Atualização automática 🔄
Um **agendamento diário** (todo dia às 08h de Brasília) roda agentes que re-varrem dezenas de fontes de bolsas, acrescentam novas oportunidades com auxílio > US$ 1.000/mês ao `bolsas.csv`, atualizam o `RELATORIO.md` e enviam um resumo por notificação/e-mail.

## Formato do `bolsas.csv`
Colunas: `nome, instituicao, nivel, prazo_inscricao, valor_mensal, duracao_meses, status, documentos, link, observacoes`
- **`prazo_inscricao`** no formato `AAAA-MM-DD` (vazio = sem prazo fixo / vagas contínuas).
- **`valor_mensal`** em USD (número).
- **`documentos`** separados por ponto e vírgula.
- **`observacoes`** traz o valor na moeda original, país e ressalvas.

> ⚠️ Os valores e prazos são aproximados (câmbio jul/2026) e vários prazos de 2027 ainda são estimados. **Confirme sempre na página oficial** antes de se candidatar.
