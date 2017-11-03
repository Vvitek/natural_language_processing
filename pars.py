import ply.yacc as yacc

from magazyn import tokens

magazyn = dict() 

def p_expression_cmd(p):
    'expression : CMD NUMBER SIZE KIND'
    p[0] = p[1] + p[2] + p[3] + p[4]
    if(p[1] == 'dostarczono'):
        if(p[4] not in magazyn):
            magazyn[p[4]] = {p[3]:p[2]}
        elif(p[3] not in magazyn[p[4]]):
            magazyn[p[4]] = {p[3]:p[2]}
        else:
            magazyn[p[4]][p[3]] += p[2]
    else:
        if(p[4] in magazyn and p[3] in magazyn[p[4]]):
            print(magazyn[p[4]][p[3]])
        else:
            print('Nie ma na magazynie')
    
def p_error(p):
    print("Syntax error in input!")

parser = yacc.yacc()

while True:
    try:
        s = input('calc > ')
    except EOFError:
        break
    if not s:
        continue
    result = parser.parse(s)
    print(magazyn)
