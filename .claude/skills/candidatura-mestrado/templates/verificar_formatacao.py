# -*- coding: utf-8 -*-
"""Verifica o DOCX do projeto contra as regras do Edital PPGE 2027.
Uso: python verificar_formatacao.py [arquivo.docx]"""
import re, sys, glob, os

ALVOS = {  # secao_md: (min_palavras, max_palavras)
    'RESUMO': (250, 320),
    '1. TEMA': (420, 550),
    '2. EXPLICA': (1100, 1350),
    '3. DEFINI': (330, 450),
    '4. OBJETIVOS': (280, 380),
    '5. ASPECTOS': (900, 1150),
}

def palavras_por_secao(md_path):
    txt = open(md_path, encoding='utf-8').read()
    secoes = re.split(r'^# ', txt, flags=re.M)
    out = {}
    for s in secoes:
        if not s.strip():
            continue
        titulo = s.splitlines()[0].strip()
        corpo = '\n'.join(s.splitlines()[1:])
        corpo = re.sub(r'\|.*\|', '', corpo)          # tabelas fora
        corpo = re.sub(r'\*\*|\[|\]', ' ', corpo)
        out[titulo] = len(corpo.split())
    return out

def checar_docx(path):
    from docx import Document
    from docx.shared import Cm
    d = Document(path)
    sec = d.sections[0]
    ok = lambda b: 'PASSA' if b else '*** FALHA ***'
    print(f'\n== DOCX: {os.path.basename(path)} ==')
    print(f"Margem sup {sec.top_margin.cm:.1f}cm / inf {sec.bottom_margin.cm:.1f}cm: "
          + ok(abs(sec.top_margin.cm-2.5) < .05 and abs(sec.bottom_margin.cm-2.5) < .05))
    print(f"Margem esq {sec.left_margin.cm:.1f}cm / dir {sec.right_margin.cm:.1f}cm: "
          + ok(abs(sec.left_margin.cm-3) < .05 and abs(sec.right_margin.cm-3) < .05))
    st = d.styles['Normal']
    print(f"Fonte Normal: {st.font.name} {st.font.size.pt:.0f}pt: "
          + ok(st.font.name == 'Times New Roman' and st.font.size.pt == 12))
    total = sum(len(p.text.split()) for p in d.paragraphs)
    print(f"Palavras no corpo (aprox): {total}")
    return total

def paginas_reais(path):
    try:
        import win32com.client
    except ImportError:
        print('pywin32 ausente — instale com: pip install pywin32 (contagem de páginas real via Word)')
        return None
    word = None
    try:
        word = win32com.client.DispatchEx('Word.Application')
        word.Visible = False
        doc = word.Documents.Open(os.path.abspath(path), ReadOnly=True)
        doc.Repaginate()
        pags = doc.ComputeStatistics(2)  # wdStatisticPages
        doc.Close(False)
        return pags
    except Exception as e:
        print(f'Nao consegui abrir no Word: {e}')
        return None
    finally:
        if word:
            word.Quit()

if __name__ == '__main__':
    base = os.path.dirname(os.path.abspath(__file__))
    docxs = sorted(glob.glob(os.path.join(base, 'Projeto_Pesquisa_*.docx')))
    alvo = sys.argv[1] if len(sys.argv) > 1 else (docxs[-1] if docxs else None)
    md = os.path.join(base, 'projeto_pesquisa.md')

    print('== PALAVRAS POR SECAO (fonte: projeto_pesquisa.md) ==')
    contagens = palavras_por_secao(md)
    for chave, (lo, hi) in ALVOS.items():
        real = next((v for k, v in contagens.items() if k.upper().startswith(chave)), None)
        if real is None:
            print(f'{chave:<14} NAO ENCONTRADA  *** FALHA ***')
        else:
            status = 'PASSA' if lo <= real <= hi else f'*** FORA DO ALVO {lo}-{hi} ***'
            print(f'{chave:<14} {real:>5} palavras  {status}')

    if alvo:
        total = checar_docx(alvo)
        pags = paginas_reais(alvo)
        if pags:
            print(f'PAGINAS REAIS (Word): {pags}  ' + ('PASSA (10-15)' if 10 <= pags <= 15 else '*** FALHA: fora de 10-15 ***'))
        else:
            est = round(total / 350 + 3.5, 1)  # +capa +cronograma +folgas de titulos
            print(f'Paginas ESTIMADAS: ~{est} (instale pywin32 p/ contagem real)')
    else:
        print('Nenhum DOCX encontrado.')
    print('\nChecagem manual final: gerar PDF (Salvar como PDF no Word) e conferir contagem de paginas do PDF.')
