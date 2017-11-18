import urllib.request
from re import findall

szlifierki = []

for i in range(60):
    with urllib.request.urlopen("https://www.ceneo.pl/Szlifierki_i_polerki/Rodzaj:Szlifierki_katowe.htmi;0020-30-0-0-%d.htm" % i) as f:
        szlifierki += findall(r'data-source-tag="">(.*)<',f.read().decode('utf-8'))
print(szlifierki)
