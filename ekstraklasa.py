from urllib.request import urlopen
from re import findall

for rok in range(2008,2016):
    print(urlopen("https://pl.wikipedia.org/wiki/Ekstraklasa_w_pi%%C5%%82ce_no%%C5%%BCnej_(2016/2017)" %rok ))
