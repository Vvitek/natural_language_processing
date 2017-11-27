from urllib.request import urlopen
from bs4 import BeautifulSoup

final_table = {}

for r in range(2008,2016):
    soup = BeautifulSoup(urlopen("https://en.wikipedia.org/wiki/{}-{}_Ekstraklasa".format(r, str(r-1999).zfill(2))).read())
    table = soup.find("span", id="League_table").parent.find_next_sibling("table")
    for row in table.find_all("tr",table):
        try:
            if(len(row.find_all("td")) > 9):
                punkty = int(row.find_all("td")[9].find("b").string)
            elif(len(row.find_all("td")) > 8):
                punkty = int(row.find_all("td")[8].string)
            final_table[row.find("a").string] +=punkty 
        except KeyError:
            final_table[row.find("a").string] = punkty 
        except:
            continue
print(final_table)
