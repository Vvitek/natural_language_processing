import ply.lex as lex

tokens = (
        'CMD',
        'NUMBER',
        'SIZE',
        'KIND'
)

t_SIZE = r'mał(e|ych)'
t_KIND = r'niezbędnik(i|ów)'

def t_CMD(t):
    r'(D|d)ostarczono|(W|w)ydano'
    t.value = t.value.lower()
    return(t)

def t_NUMBER(t):
    r'\d+|dwa|pięć'
    if t.value == 'dwa':
        t.value = '2' 
    elif t.value == 'pięć':
        t.value = '5'
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

t_ignore  = ' \t'

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

lexer = lex.lex()
