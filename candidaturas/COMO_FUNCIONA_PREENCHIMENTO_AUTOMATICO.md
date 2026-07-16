# 🤖 Como funciona o botão "Preparar candidatura"

## O que o botão faz (e o que ele NÃO faz)

O site (`index.html`) e o painel (Artifact) são páginas **estáticas** — HTML/CSS/JS que roda no seu navegador, sem servidor por trás. Isso significa que **nenhum botão numa página consegue, sozinho, abrir um navegador automatizado, pesquisar na internet ou enviar formulários**. Qualquer ferramenta que prometa isso está exagerando o que uma página web pode fazer.

O botão **🤖 Preparar candidatura** faz uma coisa simples e honesta: copia para a sua área de transferência um **prompt pronto**, com todos os dados daquela bolsa específica (nome, instituição, prazo, link oficial, documentos exigidos, pessoa indicada, por que encaixa). Você cola esse texto numa conversa comigo (Claude) para eu começar o trabalho de verdade.

## O que acontece quando você cola o prompt aqui

1. **Pesquisa real dos critérios de seleção** — busco editais anteriores, o que o comitê daquele programa específico avalia, perfis de aprovados quando isso é público. Nada inventado: se eu não conseguir verificar algo, digo que não verifiquei, em vez de supor.
2. **Monto um dossiê de candidatura**: rascunho de carta de motivação personalizada com base no seu perfil real (os arquivos `candidaturas/RAFAEL.md`, `DANIELA.md`, `MARIA_EDUARDA.md`, `LETICIA.md` deste repositório), checklist de documentos específico daquela bolsa, e um briefing para a pessoa que vai escrever sua carta de recomendação (usando os padrões documentados em `candidaturas/CARTAS_DE_RECOMENDACAO.md`).
3. **Pré-preenchimento assistido**: se o link oficial for um formulário de inscrição, uso automação de navegador (Playwright, já disponível no meu ambiente) para abrir o portal oficial e preencher os campos com os dados que você me passar naquele momento da conversa.

## Os limites de segurança — sempre, sem exceção

- **Eu nunca clico em "enviar/submit"**. O pré-preenchimento para antes da submissão final; você revisa tudo e envia pessoalmente.
- **Eu não guardo seus documentos sensíveis no repositório público** (CPF, RG, diploma, histórico, comprovantes). Você me passa esses dados na hora, dentro da conversa, e eles não viram commit neste projeto.
- **Nenhuma promessa de "% de chance de aprovação"**. Já decidimos isso no ranking por pessoa — ninguém consegue calcular isso de forma honesta, e eu não vou inventar um número para parecer mais confiável.

## O que NÃO dá para automatizar (e eu vou avisar quando isso acontecer)

Muitos portais de bolsa são desenhados para **impedir** automação — isso não é uma limitação minha, é intencional dos próprios sites:
- **CAPTCHA** e verificação "não sou um robô".
- **Autenticação em duas etapas** (código por e-mail/SMS).
- **Upload de documentos** — isso continua sendo você quem faz.
- **Ensaios/redações que precisam da sua voz pessoal** — posso rascunhar uma base, mas o texto final precisa soar como você, não como IA.
- **Entrevistas** — obviamente, isso ninguém automatiza.

Quando eu encontrar um desses bloqueios numa candidatura específica, vou avisar claramente o que consegui preencher e o que ficou pendente para você — nunca vou fingir que terminei uma etapa que na verdade travou.

## Como usar, na prática

1. No site ou no painel, encontre a bolsa que quer atacar e clique em **🤖 Preparar candidatura**.
2. Cole o texto copiado numa conversa comigo.
3. Eu pesquiso, monto o dossiê e, se o link for um formulário simples, tento pré-preencher — te avisando em cada etapa.
4. Você revisa tudo (carta de motivação, documentos, campos preenchidos) e faz o envio final pessoalmente.

Isso é feito **bolsa por bolsa**, porque cada portal de inscrição é diferente — não existe um botão único que já sabe preencher os 684 formulários de uma vez.
