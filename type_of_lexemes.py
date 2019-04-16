import sys
import ply.lex as lex
slowa_kluczowe = (
    'SK_def', 'SK_return', 'SK_or', 'SK_raise', 'SK_try', 'SK_with', 'SK_pass',
    'SK_bool', 'SK_num', 'SK_in', 'SK_is', 'SK_lambda', 'SK_nonlocal', 'SK_not', 'SK_while',
    'SK_and', 'SK_as', 'SK_assert', 'SK_break', 'SK_from', 'SK_import','SK_do', 'SK_for',
    'SK_class', 'SK_continue', 'SK_except', 'SK_finally', 'SK_global', 'SK_yield', 'SK_read',
    'SK_if', 'SK_then', 'SK_else', 'SK_elif', 'SK_end', 'SK_true', 'SK_false', 'SK_none',
)

tokens = slowa_kluczowe + (
    'LITERAL_NAPISOWY',
    'SREDNIK', 'PRZECINEK', 'DWUKROPEK', 'KROPKA',
    'NAW_L', 'NAW_P', 'NAW_KWADRATOWY_L', 'NAW_KWADRATOWY_P', 'NAW_KLAMROWY_L', 'NAW_KLAMROWY_P',
    'PLUS', 'MINUS', 'WYKRZYKNIK',
    'RAZY', 'DZIEL', 'DZIEL_C', 'RESZTA',
    'MNIEJSZE', 'ROWNE', 'WIEKSZE', 'MNIEJSZE_ROWNE', 'WIEKSZE_ROWNE', 'ROWNA_SIE', 'ROZNE',
    'PLUS_ROWNE', 'MINUS_ROWNE', 'RAZY_ROWNE', 'DZIEL_ROWNE', 'DZIEL_C_ROWNE', 'RESZTA_ROWNE', 'POTEGA_ROWNE',
    'PODSTAW',
    'IDENTYFIKATOR', 'LITERAL_LICZBOWY',
)
t_LITERAL_NAPISOWY = r'["].*["]|[\'].*[\']'
t_SREDNIK = r';'
t_DWUKROPEK = r':'
t_KROPKA = r'\.'
t_PRZECINEK = r','
t_NAW_L = r'\('
t_NAW_P = r'\)'
t_NAW_KWADRATOWY_L = r'\['
t_NAW_KWADRATOWY_P = r'\]'
t_NAW_KLAMROWY_L = r'\{'
t_NAW_KLAMROWY_P = r'\}'
t_PLUS = r'\+'
t_MINUS = r'-'
t_WYKRZYKNIK = r'!'
t_RAZY = r'\*'
t_DZIEL = r'/'
t_DZIEL_C = r'//'
t_RESZTA = r'%'
t_MNIEJSZE = r'<'
T_WIEKSZE = r'>'
T_MNIEJSZE_ROWNE = r'<='
T_WIEKSZE_ROWNE = r'>='
t_ROWNA_SIE = r'='
t_ROWNE = r'=='
t_ROZNE = r'!='
t_PODSTAW = r':='
t_PLUS_ROWNE = r'\+='
t_MINUS_ROWNE = r'-='
t_RAZY_ROWNE = r'\*='
t_DZIEL_ROWNE = r'/='
t_DZIEL_C_ROWNE = r'//='
t_RESZTA_ROWNE = r'%='
t_POTEGA_ROWNE = '\*\*='
t_LITERAL_LICZBOWY = r'[0-9]+|[0-9]*\.[0-9]+'

def t_IDENTYFIKATOR(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    if 'SK_'+t.value in slowa_kluczowe:
        type = 'SK_' + t.value
        t.type = type
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
    t.lexer.skip(1)

lexer = lex.lex()
kod = open(sys.argv[1]).read()
lexer.input(kod)
indyfikatory = {}
for indyfikator in lexer:
    if indyfikator.type in indyfikatory:
        indyfikatory[indyfikator.type] = indyfikatory[indyfikator.type]+1 
    else:
        indyfikatory[indyfikator.type] = 1
for (nazwa, ilosc) in sorted(indyfikatory.items()):
    print (nazwa, ":", ilosc)
