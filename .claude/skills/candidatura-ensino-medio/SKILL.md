---
name: candidatura-ensino-medio
description: Pipeline para construir candidatura vencedora de ensino médio no exterior com bolsa integral (UWC, colégios internos com financial aid, intercâmbios) — descoberta de campus/escola, projeto (ensaios) sob medida por destino, baseado em casos reais de aprovados, humanização na voz autêntica do/a jovem, e preparação de entrevista e dinâmica de grupo. Usar quando um adolescente (13-17) quiser bolsa integral de ensino médio fora.
---

# Candidatura de Ensino Médio no Exterior — Pipeline Vencedor (adaptado do candidatura-mestrado)

Adaptação da skill `candidatura-mestrado` para o pré-universitário. Um PROJETO (conjunto de ensaios/
materiais) sob medida POR DESTINO. Siga as fases na ordem.

## AS TRÊS REGRAS ZERO (invioláveis)
1. **Zero dado inventado.** Nenhuma conquista, atividade, nota ou experiência que não seja REAL do/a
   jovem. Fraude é checável e elimina — e há entrevista/dinâmica ao vivo. Apresentar o que é REAL no
   enquadramento mais forte; `[PREENCHER]` para o que só a família sabe.
2. **Painel = os seletores REAIS.** Modelar, por pesquisa, quem avalia e o que valoriza: no UWC, o
   Comitê UWC Brasil + os valores UWC (paz, sustentabilidade, entendimento intercultural, serviço);
   nos colégios (Exeter/Andover), o admissions office (fit, caráter, potencial, necessidade financeira).
   Para cada destino: o que premia, o que reprova, a objeção provável, a pergunta mais dura na entrevista.
3. **Tudo autêntico e defensável ao vivo.** Cada frase do ensaio tem de ser algo que o/a jovem
   consegue defender na entrevista e na dinâmica de grupo, na própria voz, com naturalidade. Se não
   soa como uma pessoa de 14-16 anos real, reescrever.

## Fase −1 — Descoberta de campus/escola/programa (a partir do perfil)
A partir do perfil (idade/série, inglês, notas, interesses, causa que ama, contexto de renda), fazer
fan-out de busca e rankear por probabilidade de aprovação COM o perfil: campi UWC (18 opções — clima,
foco, seletividade), colégios com financial aid need-blind (Exeter/Andover/St. Paul's), intercâmbios
gratuitos (Jovens Embaixadores aos 15, AFS Global STEM, Technovation aos 14). Recomendar alvo + plano B,
com prazos e requisitos reais. Registrar em `alvos_ensino_medio.md`.

## Fase 0 — Perfil e voz autêntica do/a jovem
1. Coletar do questionário (KIT_CANDIDATURA.md, seção 5): cenas reais, desafios, serviço, valores,
   causa, atividades, matérias, livro que marcou, por que estudar fora.
2. Extrair o PERFIL DE ESTILO de um texto real dele/dela (uma redação da escola): traços de voz +
   marcas a evitar (texto adulto/formal demais, clichê, "sempre sonhei", listas sem alma). Salvar
   `estilo_<nome>.md`. O texto final tem de soar uma pessoa jovem, curiosa e verdadeira.

## Fase 1 — Inteligência do processo (por destino)
- **UWC (via Comitê UWC Brasil):** cronograma anual (abre meados do ano p/ o ano seguinte), etapas
  (formulário → prova escrita [conteúdo + atualidades] → entrevista → fim de semana de seleção em
  grupo), critérios, isenção de taxa. Fontes: br.uwc.org (cronograma, critério), guia.uwc.org.br.
- **Colégios EUA (Exeter/Andover/St. Paul's):** prazos (~15/jan), SSAT/TOEFL/Duolingo, ensaios,
  2-3 cartas, entrevista, formulários financeiros dos pais.
- Extrair para `padrao_<destino>.md`: prazos exatos, documentos, LIMITES dos ensaios (nº de palavras/
  caracteres), enunciados EXATOS quando o ciclo abre.

## Fase 2 — Escolha de campi/escolas (fit)
Para cada opção plausível: caso do advogado (por que é a melhor PARA ela) → juiz decide por
probabilidade de aprovação e fit de valores/interesses. Plano B barato no mesmo ciclo.

## Fase 3 — Dossiê de "o que os seletores premiam" (casos reais)
Minerar, em fontes públicas, ensaios/relatos de aprovados REAIS (UWC "application inspiration",
relatos de scholars, blogs de admitidos em boarding) e a orientação oficial. Registrar padrões
concretos: temas de ensaio que funcionam, como demonstrar valores por histórias (não adjetivos),
o que derruba candidaturas. Salvar `casos_aprovados_<destino>.md` com FONTE/URL de cada aprendizado.

## Fase 4 — O PROJETO (ensaios) sob medida por destino
1. Estrutura = enunciados EXATOS do destino (nada além). Um conjunto de ensaios POR destino.
2. Eixo = interseção {valores/critérios do destino} × {histórias reais dela} × {causa que ela ama}.
3. Personal statement + ensaios (desafio, impacto/serviço, por que este campus) construídos a partir
   do material REAL da Fase 0. Placeholders `[INSERIR]` para o que faltar. NUNCA inventar.
4. Um arquivo por destino: `projeto_<nome>_<destino>.md`.

## Fase 5 — Auditoria adversarial (3 lentes)
- AUTENTICIDADE (soa uma jovem real de 14-16? defensável na entrevista?),
- FIT (o seletor daquele destino aprovaria? cobre os valores/critérios?),
- INTEGRIDADE (toda conquista/atividade é real e comprovável? zero exagero checável?).
Aplicar todas as críticas confirmadas.

## Fase 6 — Aberturas fortes
Gerar várias primeiras frases (cenas concretas reais) → escolher a que mais prende sem clichê.

## Fase 7 — Humanização (voz jovem autêntica)
Reescrever na voz dela (usar frases reais do texto da Fase 0), frases de tamanho variado, zero marca
de IA/adulto. Verificação: autenticidade + fidelidade (nenhuma conquista mudou) + limite de palavras.

## Fase 8 — Formatação/limites
Ajustar a cada limite de palavras/caracteres do formulário. Medir. Iterar até caber sem perder o miolo.

## Fase 9 — Materiais de defesa (entrevista + dinâmica de grupo)
- `entrevista_<nome>.md`: perguntas prováveis (UWC/colégio) + guias de resposta na voz dela + as
  perguntas-âncora ("fale de você", "por que UWC", "uma questão global que te importa", "um conflito
  que você resolveu"). Treinar até natural.
- `dinamica_grupo.md`: como se portar no fim de semana de seleção UWC (colaborar, ouvir, liderar sem
  atropelar — o que os observadores procuram), com base em relatos reais.
- `checklist_<destino>.md`: documentos, prazos, o que só a família faz (envio, financeiro, provas).

## Estrutura de arquivos por destino
```
candidaturas/<nome>/
  alvos_ensino_medio.md
  estilo_<nome>.md
  <destino>/
    padrao_<destino>.md
    casos_aprovados_<destino>.md
    projeto_<nome>_<destino>.md
    entrevista_<nome>.md
    checklist_<destino>.md
```

## O que fica com a família (menor de idade)
Provas (SSAT/TOEFL/prova UWC), entrevistas e dinâmicas, documentos oficiais e o ENVIO — sempre com
os pais no controle. O Claude prepara todo o material escrito e o treino; a família revisa e envia.

> Honestidade: não existe aprovação garantida nem "IA indetectável". A força real é voz autêntica +
> conquistas reais + preparação de entrevista. Começar 1-2 anos antes (aos 14) é a maior vantagem.
