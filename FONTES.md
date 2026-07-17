# Fontes e Metodologia — Censo Nacional de Pós-Graduação (mestrados_brasil.csv)

Este documento explica **como cada dado foi levantado** e onde encontrar a fonte de cada programa individual. Ele não lista uma URL por afirmação porque isso nunca foi registrado dessa forma — o que existe, de forma honesta, é descrito abaixo.

## Como citar a fonte de um programa específico

A fonte primária de cada linha do CSV é a própria coluna **`link`** — é o site oficial do programa de pós-graduação (PPG), a mesma página usada para confirmar nome do programa, nota CAPES e (quando encontrado) e-mail de coordenação. **Para verificar qualquer dado da planilha, o primeiro passo é sempre abrir o link daquela linha.**

Quando um dado tem uma ressalva entre parênteses na coluna `explicacao`, `email` ou `compat_clinica` (ex.: "não confirmado", "consultar site", "verificar"), isso significa que a fonte não confirmou aquele dado com certeza — não é uma URL fantasma, é uma marcação explícita de incerteza (Regra Zero: nada foi inventado para preencher lacunas).

## Fontes gerais usadas na pesquisa (por categoria)

| Categoria | O que foi usado |
|---|---|
| **Catálogo oficial de programas** | Plataforma Sucupira (CAPES) — base oficial de todos os PPGs reconhecidos no Brasil, usada como referência de existência/nota CAPES dos programas |
| **Sites institucionais dos PPGs** | Página oficial de cada programa (a mesma que está na coluna `link`) — fonte primária para linhas de pesquisa, e-mail de coordenação, área de concentração |
| **Buscas web dirigidas** | Pesquisas pontuais via WebSearch, uma leva por lote de programas, para preencher e-mails de coordenação e confirmar linhas de pesquisa quando o site institucional não estava indexado ou era incompleto |
| **Verificação cruzada** | Para os 207 e-mails que apareciam sem nenhuma ressalva (ou seja, mais arriscados por parecerem 100% confirmados), foi feita uma segunda rodada independente de busca — resultado: 9 erros reais corrigidos (ver commits `d81538b` a `0701503`) |

## Por que não existe uma bibliografia com uma URL por dado

O levantamento foi feito em dezenas de lotes paralelos ao longo de várias sessões, cada um cobrindo um grupo de programas via busca web dirigida. As buscas individuais (URLs exatas abertas por cada consulta) não foram registradas separadamente do resultado final — apenas o dado extraído (e-mail, linha de pesquisa, nota CAPES) foi salvo na planilha. Reconstruir uma URL retroativa por linha, sem tê-la registrado no momento, seria inventar precisão que não existe — o que viola a mesma regra que guiou o resto deste projeto (nunca fabricar dado). A fonte confiável e verificável que **de fato existe** para cada linha é o link do próprio programa, na coluna `link`.

## Casos com fonte adicional documentada

Alguns achados específicos tiveram fonte/confirmação registrada em mais detalhe no histórico de commits e nos arquivos `candidaturas/*.md`:

- **UNISINOS — Psicologia encerrada em 2022**: confirmado via busca dedicada que a universidade fechou 12 PPGs (incluindo Psicologia) por corte orçamentário em julho/2022, apesar de nota CAPES 5.
- **UENF vs. UFSC** e **CEFET-MG vs. UFMG**: dois erros de instituição identificados por um agente de verificação independente e corrigidos (commit `c7a5a9d`).
- **UPE vs. UFPE (Posneuro)**: mesmo programa listado duas vezes sob instituições diferentes; corrigido e consolidado numa única linha (commit `dcdc397`).
- **9 e-mails corrigidos na auditoria** (USP-IP Psicologia Clínica, UnB Ciências do Comportamento, UnB PPGE, UFG PPGE, Bahiana/EBMSP, USP-IP NEC, UERGS PPGEd, UFT PPPGE, UFPE Psicologia Cognitiva): motivo de cada correção documentado nos commits da fase de auditoria (`d81538b` → `0701503`).

## Resumo prático

**Se você (Daniela/Maria Eduarda/Rafael) for se candidatar a um programa específico:** não confie apenas na planilha — abra o `link` daquela linha, confirme o edital vigente diretamente no site do programa, e trate qualquer e-mail marcado "não encontrado" ou sem `✓verificado` como precisando de confirmação manual antes de enviar qualquer documento.
