import ply.lex as lex

tokens = (
        'CMD',
        'NUMBER',
        'SIZE',
        'KIND',
)

t_SIZE = r'mał(e|ych)'
t_KIND = r'niezbędnik(i|ów)'
t_CMD  = r'(D|d)ostarczono|(W|w)ydano'

def t_NUMBER(t):
    r'\d+|dwa|pięć'
    try:
        t.value = int(t.value)
    except:
        if t == 'dwa':
            t = int(2)
        elif t == 'pięć':
            t.value = int(5)
        return t
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

t_ignore  = ' \t'

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

lexer = lex.lex()
