import ply.yacc as yacc

from magazyn import tokens

magazyn = dict() 

def p_expression_cmd(p):
    'expression : CMD NUMBER SIZE KIND'
    if(p[1] == 'dostarczono'):
        if(p[4] not in magazyn):
            magazyn[p[4]] = {p[3]:int(p[2])}
        elif(p[3] not in magazyn[p[4]]):
            magazyn[p[4]] = {p[3]:int(p[2])}
        else:
            magazyn[p[4]][p[3]] += int(p[2])
    elif(p[1] == 'wydano'):
        if(p[4] in magazyn and p[3] in magazyn[p[4]] and magazyn[p[4]][p[3]]>0):
            magazyn[p[4]][p[3]] -= int(p[2])
        else:
            print('Nie ma na magazynie')
    else:
        print('blad')

    
def p_error(p):
    print("Syntax error in input!")

parser = yacc.yacc()

while True:
    try:
        s = input('polecenie> ')
    except EOFError:
        break
    if not s:
        continue
    result = parser.parse(s)
    print(magazyn)
