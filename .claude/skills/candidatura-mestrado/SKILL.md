---
name: candidatura-mestrado
description: Pipeline completo para construir candidatura vencedora a mestrado/doutorado (Brasil, Portugal, Espanha, mundo) — escolha de linha/orientador, projeto alinhado à agenda do avaliador, verificação de referências, humanização na voz do candidato, formatação mecânica e materiais de defesa. Usar quando o usuário quiser se candidatar a pós-graduação.
---

# Candidatura de Mestrado/Doutorado — Pipeline Vencedor (padrão faber ultracode)

Método validado na candidatura PPGE/Unicamp 2027 (Maria Eduarda). Siga as fases NA ORDEM.
Regra Zero global: NENHUM dado, número, citação ou referência não verificada em fonte real
aberta. Referência inventada é desclassificação.

Padrão ultracode: orquestrar com **workflows multi-agente** (fan-out para cobrir, verificar
adversarialmente, sintetizar), manter o loop principal como INTEGRADOR (aplica só o que passa
nos verificadores, conferindo citações), e nunca truncar cobertura em silêncio. Custo de token
não é restrição quando o usuário pediu profundidade; qualidade e correção são.

## AS TRÊS REGRAS ZERO (invioláveis, valem em todas as fases)

1. **Zero dado inventado.** Nenhum número, citação, referência, lei-com-artigo, ou item de
   currículo (Lattes/ORCID) sem fonte real aberta e verificada. Isso inclui NÃO fabricar
   experiências, publicações, empregos ou títulos "teoricamente possíveis" do candidato — é
   fraude checável e elimina a candidatura. O papel é apresentar o que é REAL no enquadramento
   mais forte, com placeholders `[PREENCHER]` para o que só o candidato sabe.
2. **Painel de juízes = a banca REAL, sem exceção.** Toda avaliação do projeto precisa ser feita
   por agentes-juízes que modelam, a fundo e por pesquisa web (Lattes/CNPq, sites do programa,
   repositório, SciELO, ORCID), o perfil VERDADEIRO de cada pessoa que comporá a banca
   julgadora da universidade-alvo (orientador pretendido, coordenador, docentes da linha/grupo,
   metodólogo). Para cada um: perfil, obras, o que valoriza/reprova, objeção provável e a
   pergunta mais dura. Quando a composição exata não é pública, modelar os docentes reais/
   prováveis da linha e DECLARAR isso com honestidade. Iterar (achar erro → corrigir → reavaliar)
   ATÉ o painel aprovar em todas as lentes. Artefatos: `juizes_banca.md` (perfis) reusado como
   GABARITO nas fases de corte/auditoria.
3. **Toda resposta explicável para uma criança.** O candidato tem de entender 100% do projeto e
   defender cada frase ao vivo. Mesmo os pontos complexos precisam de uma resposta simples,
   objetiva, na 1ª pessoa do candidato (linguagem de criança de 12 anos) + uma versão técnica
   curta. Verificar com uma lente "leigo" até passar. Artefatos: `defesa_respostas_simples.md`
   e `GUIA_EXPLICACAO_SIMPLES.md`. Prefira reformular a metodologia para o desenho mais simples
   e defensável (ex.: descritivo/monitoramento em vez de alegação causal frágil) — o mais
   honesto costuma ser o mais simples E o que mais blinda contra a banca.

## Fase −1 — Descoberta de universidade, programa, grupo e orientador (a partir do perfil)

Quando o candidato só tem o PERFIL (ex.: graduação em Big Data e Analytics) e um objetivo
("quero fazer mestrado/doutorado"), o Claude DESCOBRE o alvo antes de tudo. Workflow:
1. Extrair do perfil os ATIVOS transferíveis (competências, TCC, artefatos, temas amados).
2. Fan-out de busca por programas/grupos/orientadores — no país pedido OU no mundo — cujas
   agendas casam com esses ativos, em qualquer idioma oficial do programa. Fontes: Catálogo
   CAPES/Sucupira e repositórios (Brasil), DGES/portais (Portugal), portais das comunidades
   autônomas (Espanha), rankings/departamentos e páginas de faculty (EUA/UK/Europa/mundo).
3. Juiz de FIT rankeia por probabilidade de aprovação COM o perfil (aderência, prova/entrevista,
   bolsa, orientador cuja biografia espelha a do candidato, fit de longo prazo). Recomenda alvo
   + plano B, com prazos e requisitos por país.
4. Só então seguir para a Fase 0 com o alvo escolhido. Todo o restante do pipeline é agnóstico
   de país/idioma: adapta o roteiro ao edital/norma local (ver "Adaptações por país") e produz
   o documento no idioma oficial exigido (projeto de pesquisa, SOP, carta de motivação, etc.).

---

## Fase 0 — Perfil e voz do candidato
1. Coletar: formações, TCC/artigos, artefatos (dashboards, repositórios), história pessoal.
2. Extrair PERFIL DE ESTILO de um texto real do candidato (TCC/redação): traços de voz a
   imitar + lista de marcas de IA a eliminar (tríades, paralelismos perfeitos, conectivos
   formulaicos em série — "Nesse sentido/Além disso" —, travessões em excesso — máx. ~1 a cada
   2 parágrafos —, parágrafos simétricos, anáfora mecânica "Primeiro.../Segundo...", enumeração
   em cascata de 3-4 itens que soa preenchimento). Salvar como `estilo_<nome>.md`.

## Fase 1 — Inteligência do edital
1. Baixar o edital (WebFetch; se PDF não converter, baixar e extrair com pypdf).
2. Extrair para uma tabela `padrao_formatacao.md`: prazos exatos, etapas com datas, documentos
   exigidos, FORMATO do projeto (páginas mín/máx e SE incluem rosto+referências — quase sempre
   incluem; fonte; margens; espaçamento; roteiro EXATO de seções), regras de linha/grupo,
   bibliografia oficial da prova, critérios de pontuação. Incluir um ORÇAMENTO DE PALAVRAS por
   seção (régua ~350 palavras/página em Times 12, espaçamento 1,5) somando ao teto de páginas.
3. Alertar o usuário IMEDIATAMENTE se o prazo for próximo (data absoluta, não relativa).

## Fase 2 — Escolha de linha/grupo/orientador (painel adversarial)
1. Listar linhas/grupos/orientadores com vagas (anexos do edital).
2. Workflow: 1 agente ADVOGADO por opção plausível (pesquisa produção real dos docentes na web
   e defende a opção + ataca a atual) → 1 JUIZ decide pela maior probabilidade de aprovação com
   nota alta (aderência do perfil, bibliografia da prova, perfil dos orientadores, fit de longo
   prazo). Registrar plano B no mesmo edital (troca barata).

## Fase 3 — Dossiê do orientador-alvo
1. Minerar publicações REAIS (Lattes, Google Scholar, SciELO, repositórios): abrir CADA uma e
   registrar citação completa + DOI/URL. Mínimo 4-6 obras; idealmente cobrir os DOIS polos da
   obra do docente (no caso Galvão: financiamento/"recursos importam" + shadow education).
2. Extrair: temas, métodos, vocabulário, teses que defende, lacunas que aponta.
3. Ouro estratégico: biografia do orientador que espelhe a do candidato (ex.: economista que
   migrou para educação valida candidata de dados).

## Fase 4 — Projeto de pesquisa
1. Estrutura = roteiro EXATO do edital. Nada além, nada aquém.
2. Eixo central = interseção {agenda do orientador} × {competência do candidato} × {objeto que
   o candidato ama}. Citar 3+ obras do orientador com FUNÇÃO REAL no argumento (método adotado,
   achado transposto, lacuna preenchida) — nunca ornamental.
3. Objeto mensurável ≠ moldura conceitual: declarar explicitamente o que os dados captam e o
   que fica como lente teórica (desarma a crítica mais comum de banca). Ex.: neurodiversidade =
   lente; público-alvo da educação especial/TEA registrado no Censo = objeto mensurável.
4. Fontes de dados públicas nomeadas (Brasil: microdados INEP/Censo Escolar, SIOPE/FNDE, IBGE,
   INSE/INEP). Declarar a unidade de análise (defender ESCOLA quando o orientador defende isso).
5. Placeholders `[INSERIR: ...]` para tudo que só o candidato sabe. NUNCA inventar.
6. Referências: só obras confirmadas, ABNT (ou norma local), DOI/URL quando houver + "Acesso em".
7. Cronograma factível (24 meses mestrado): delimitar série/escopo, marcar exercícios ambiciosos
   como exploratórios (um capítulo, não um eixo autônomo).

## Fase 5 — Auditoria adversarial (workflow, 3 lentes, effort high)
Fan-out por dimensão → cada achado verificado antes de aplicar:
- ADERÊNCIA: banca da linha julga fit com ementa/grupo/orientador.
- FORMAL: páginas, roteiro, idioma, ABNT, coerência título-corpo.
- INTEGRIDADE: reverificar na web os 5 fatos mais arriscados (leis COM o artigo citado,
  resoluções, DOIs); estatísticas sem fonte; promessas irreais.
Aplicar TODAS as críticas confirmadas.

## Fase 6 — Título (torneio)
Geradores com ângulos distintos → juiz SIMULANDO O COORDENADOR recebendo 40 projetos.
Critérios: objeto claro e mensurável, linguagem do campo do avaliador, "eu orientaria isso?".

## Fase 7 — Humanização (voz do candidato)
1. Backup do arquivo antes (`projeto_pesquisa_v2_backup.md`).
2. Reescrita frase a frase seguindo o perfil de estilo da Fase 0 + CLAREZA RADICAL: todo termo
   técnico com tradução simples em meia frase na 1ª aparição; frases de tamanho VARIADO (uma
   ideia por frase; quebrar tríades simétricas); 1ª pessoa nas seções de trajetória (usar frases
   REAIS do texto do candidato).
3. Verificação tripla: anti-IA + FIDELIDADE (diff com backup: nenhum fato/citação mudou) + formal.
Honestidade: não existe "IA indetectável" garantida; a defesa real é voz autêntica + dados reais
+ domínio do conteúdo (o candidato será arguido ao vivo).

## Fase 8 — Formatação mecânica (garantia, não promessa)
Scripts `gerar_docx.py` (aplica formato do edital) + `verificar_formatacao.py` (mede DOCX real:
margens/fonte/espaçamento via python-docx; PÁGINAS REAIS via Word COM `ComputeStatistics(2)` no
Windows; palavras por seção vs orçamento). Iterar até PASSA em TUDO.

**⚠️ Lever de página mais importante (aprendido na prática): a formatação ABNT das REFERÊNCIAS.**
python-docx aplica o estilo Normal (espaçamento 1,5 + space_after) a TODOS os parágrafos,
inclusive às ~25-30 referências — o que infla 2-4 páginas E fere a ABNT. Correção (recuperou
18→16 páginas SEM cortar conteúdo, e ficou MAIS correto):
- Corpo: espaçamento 1,5, `space_after = Pt(0)` (ABNT: o recuo de 1,25 cm marca o parágrafo,
  sem espaço extra entre eles). Justificado, recuo de primeira linha 1,25 cm.
- Referências (NBR 6023): detectar o cabeçalho "# 7. REFER..." e, dali em diante, aplicar
  `line_spacing = SINGLE`, `space_after = Pt(6)` (uma linha entre referências), alinhado à
  esquerda, SEM recuo de primeira linha.
- Cabeçalhos: `space_before` moderado (10-14pt), `space_after` pequeno (4-6pt).

**Só depois** de esgotar a formatação, cortar conteúdo — e cortar REDUNDÂNCIA, não substância:
sobreposição entre a seção "Tema" e a "Justificativa" (a Justificativa reexplica leis já
introduzidas no Tema — enxugar a repetição); objetivos verbosos que repetem a metodologia;
adjetivação dupla; glosas de siglas já definidas antes; encerramentos-resumo ("Juntas, as três
frentes..."). Medir após CADA corte — o page-break é não-linear perto do teto (uma frase pode
custar ou salvar uma página inteira).

## Fase 9 — Materiais de defesa (agentes diretos, gravam arquivos)
- `GUIA_EXPLICACAO_SIMPLES.md`: cada seção explicada como para criança de 12 anos + "como falar
  para a banca" + 12 perguntas prováveis com respostas em 1ª pessoa.
- `juizes_banca.md`: perfil real de cada docente avaliador + objeção provável de cada um +
  resposta pronta. **Este arquivo é reutilizado como GABARITO na Fase 10** (o verificador de
  banca compara o projeto contra ele).
- `defesa_respostas_simples.md`: por avaliador, as perguntas prováveis com resposta "de criança"
  (1ª pessoa) + versão técnica curta; e as 10 perguntas mais prováveis no geral, para decorar
  (cumpre a 3ª Regra Zero).
- `otimizacoes_benchmark.md`: recomendações extraídas de dissertações aprovadas reais no
  repositório da universidade-alvo + BDTD/Catálogo CAPES, cada uma com fonte/URL.
- `Guia_Lattes_ORCID_<nome>.docx` (+ `.md`): guia de preenchimento do currículo Lattes (CNPq) e
  do ORCID, pré-preenchido com o que é REAL e com placeholders `[PREENCHER]` — nunca inventa
  itens (ver 1ª Regra Zero). Padroniza o nome de citação, classifica TCC como trabalho de
  conclusão (não artigo) e o produto técnico como software.
- Artefato de impacto (dashboard/protótipo) — ver Fase 11.
- `LEIA-ME_CHECKLIST`: documentos, prazos, o que só o candidato pode fazer (placeholders).

## Fase 10 — Corte para o teto de páginas COM verificação adversarial (workflow ultracode)
Quando o projeto estoura o teto, NÃO cortar no olho. Workflow `corte-N-paginas-verificado`:
- **Phase Comprimir** (pipeline, um agente por seção gorda): cada editor LÊ o projeto + o
  `estilo_<nome>.md` + o `juizes_banca.md` e retorna a seção comprimida ao alvo de palavras,
  com regras invioláveis: preservar TODAS as citações autor-ano; preservar todos os pontos que
  a banca valoriza; manter placeholders `[INSERIR]`; manter a voz do candidato; cabeçalhos de
  subseção intactos; Regra Zero. Schema de saída: `{secao, markdown, palavras, citacoes[], notas}`.
- **Phase Verificar** (parallel por seção, 3 juízes): VOZ (vs estilo_<nome>.md — humano ou IA?),
  BANCA (vs juizes_banca.md — algum ponto valorizado se perdeu?), INTEGRIDADE (vs original —
  citação sumiu? número alterado/inventado? placeholder perdido? aprova só com ZERO problemas).
  Schema: `{aprova, problemas[]}`.
- O loop principal INTEGRA: aplica cada seção comprimida que passou em INTEGRIDADE, conferindo
  as citações uma a uma, e usa os apontamentos de VOZ e BANCA para ajustar antes de colar.

**Insight de ouro (não esquecer):** os juízes de BANCA comparam contra o gabarito `juizes_banca.md`,
então eles apontam lacunas que já existiam no texto ORIGINAL, não só regressões da compressão.
Trate esses apontamentos como MINERAÇÃO DE BURACOS: pontos que a banca cobra e o projeto não
cobria. No caso PPGE, o painel revelou (e nós inserimos, compactos):
  1. Recorte PÚBLICO × PRIVADO/CONVENIADO (APAEs) — a dupla matrícula também financia a rede
     filantrópica; omitir = "falha grave". Separar os dois setores no desenho e no painel.
  2. VÍNCULO DOCENTE (concursado/temporário/terceirizado, cruzável no Censo escola a escola) —
     condições de trabalho de quem oferta o AEE.
  3. DISCLAIMER CAUSAL — objetivo é descritivo/monitoramento; associação ≠ efeito causal.
  4. PAINEL como CONTROLE SOCIAL (conselhos, Ministério Público, famílias) — desarma a objeção
     de "quantitativismo gerencialista".
  5. QUALITATIVO como etapa seguinte natural (estudos de caso, escuta de gestores/famílias).
Adicionar de volta os pontos críticos de forma COMPACTA mantém o corte líquido E fecha flancos
de arguição ao mesmo tempo. Rerodar o painel após integrar ("teste tudo de novo") até VOZ+BANCA
+INTEGRIDADE aprovarem e as páginas PASSAREM.

## Fase 11 — Artefato de impacto / dashboard (Regra Zero dura + workflow de verificação)
Padrão Power BI, arquivo HTML único autocontido (SVG/CSS/JS inline, SEM CDN — CSP bloqueia).
Regras:
- SÓ números verificados AGORA em fonte oficial PRIMÁRIA, com FONTE + ANO + LINK DIRETO em CADA
  elemento (KPI, gráfico, card). Fonte primária = a origem oficial do dado (Brasil: gov.br/inep,
  gov.br/mec, gov.br/fnde, planalto.gov.br). Fonte secundária = quem apenas republica o dado
  (ONGs, anuários, portais como diversa.org, todospelaeducacao) — **NUNCA pode ser o link de um
  número**, nem "apud". Se um número só existe em fonte secundária e não se confirma na primária,
  REMOVA-o e converta em card "Objeto da pesquisa — a produzir a partir dos microdados", sem
  número. Verificar sempre com grep no fim: zero domínios secundários no arquivo. Ao remover um
  gráfico, remover também o bloco JS que o desenha (senão fica referência órfã a elemento
  inexistente) e o item de rodapé correspondente.
- Dados MAIS ATUAIS possíveis: checar se saiu a edição mais recente (ex.: Censo Escolar do ano
  corrente pode ainda não ter saído em meados do ano seguinte — declarar explicitamente qual é
  o mais recente disponível).
- Resultados da PESQUISA não entram: molduras vazias rotuladas "a preencher com microdados",
  uma por questão de pesquisa (eixo e fonte definidos, valores pendentes).
- Companion `FONTES_E_EXTRACOES.md`: para CADA número — valor, ano, fonte, LINK DIRETO, como foi
  calculado/derivado; separar "verificados" de "a preencher".
Workflow `dashboard-unificado-verificado`: 1 agente CONSTRÓI (une/otimiza) → painel parallel
VERIFICA (integridade de fontes/links; atualidade dos dados; completude/design). Integrar só o
que passa. Componentes típicos: desenho conceitual em fluxo, KPIs, série histórica, barras por
região/UF, evolução do fator de ponderação, complementação da União por ano, rosca de cobertura.

## Adaptações por país
- **Brasil**: projeto de pesquisa + Currículo Lattes (lattes.cnpq.br, obrigatório, pontuado) +
  prova escrita da bibliografia da linha + entrevista. Cotas/ações afirmativas no edital.
  Aprovados de referência: repositório institucional + BDTD (bdtd.ibict.br) + Catálogo CAPES.
  Editais no 1º semestre para ingresso no ano seguinte; gratuito na pública, bolsas depois.
- **Portugal**: candidatura por FASES (1ª ~fev-jun, mais vagas/bolsas; 2ª ~jul-ago; 3ª residual).
  Carta de motivação (1 pág, personalizada) + CV + pré-projeto curto (2-5 págs) + diploma
  apostilado (Apostila de Haia). Contato prévio com orientador é bem-visto. Propinas ~1-7k EUR/ano
  (CPLP às vezes equiparado a nacional). Sites: DGES + universidades (ULisboa, U.Porto, UC, etc.).
- **Espanha**: máster OFICIAL (habilita doutorado; ≠ título próprio) via preinscripción no portal
  da comunidade autônoma. Carta de motivación + CV (Europass) + histórico com NOTA MÉDIA
  CONVERTIDA à escala 0-10 (Equivalencia de nota media, Ministerio de Universidades — fazer ANTES,
  demora semanas). Diploma apostilado. Rodadas fev-set.
- **Mundo (EUA/UK/Canadá/etc.)**: Statement of Purpose (SOP, 1-2 págs, inglês) no lugar do
  projeto, mesma fórmula com ênfase em fit ("Professor X's work on Y informs my proposed Z").
  Contato prévio com supervisor quase obrigatório fora dos EUA course-based (e-mail 5-8 linhas:
  quem é + fit + 1 pergunta + CV, 3-6 meses antes). IELTS/TOEFL com 2+ meses; cartas com 1 mês.
  Bolsas: Chevening (UK), Fulbright (EUA), Erasmus Mundus (Europa, out-jan), DAAD (Alemanha).
  O pipeline continua igual: dossiê do supervisor → SOP alinhado → humanização → mock interview.

## Ferramentas e operação do pipeline (padrão ultracode)
- **Workflows multi-agente** (ferramenta Workflow): painel de escolha (Fase 2), auditoria
  adversarial (Fase 5), torneio de título (Fase 6), humanização+verificação (Fase 7), corte
  verificado (Fase 10), dashboard unificado+verificado (Fase 11). Padrão: pipeline por default;
  barrier (parallel) só quando a fase N precisa de TODOS os resultados da N-1. Loop principal
  = integrador que aplica só o verificado.
- **Agentes diretos** (ferramenta Agent, background) para entregáveis que gravam UM arquivo cada
  (banca intel, guia, benchmark, dashboard) — evita corrida de escrita no mesmo arquivo.
- **Scripts locais**: `gerar_docx.py` (formato do edital, com o fix ABNT de referências),
  `verificar_formatacao.py` (garantia mecânica).
- **Modos de falha conhecidos e correções**:
  - Workflow `agent({schema})` falha com "subagent completed without calling StructuredOutput":
    o schema é obrigatório mas o subagente não o chamou. Correção: reforçar no prompt que a
    resposta DEVE ser via a ferramenta estruturada, ou (fallback) usar agente direto SEM schema
    pedindo para gravar o arquivo, e o loop principal parseia.
  - Limite de sessão/semana de subagentes (ex.: "resets 4pm"): anotar o horário de reset,
    NÃO relançar antes (só gera falha); enquanto isso, o loop principal faz o trabalho que não
    exige agente (cortes, formatação, medição). Após o reset, relançar. Retomar workflow com
    `resumeFromRunId` (cache devolve o que já concluiu; conferir journal.jsonl antes de assumir).
  - Antes de relançar um agente que grava o mesmo arquivo de outro em andamento, PARAR o antigo
    (TaskStop) para não haver corrida.
- **Regra de medição**: nunca declarar "cabe em N páginas" sem rodar `verificar_formatacao.py`
  (páginas reais do Word), porque a régua de palavras/página erra perto do teto.
