'''Python script to extract all the NHL teams and thier web pages
'''
from bs4 import BeautifulSoup

import requests
fobj1=open('teams','w')
fobj2=open('team_links','w')
wiki='https://en.wikipedia.org/'
r = requests.get('https://en.wikipedia.org/wiki/National_Hockey_League') 


data = r.text

soup = BeautifulSoup(data)

team_table = soup.find('table','navbox wikitable')

all_rows=team_table.find_all('tr')

for row in all_rows:
    col=row.find_all('td')
    if len(col) > 0:
        print col[0].text,
        print col[0].find('a').get('href')
        fobj1.write(col[0].text+"\n")
        fobj2.write(wiki+col[0].find('a').get('href')+"\n")
    else:
        pass
        #print row    
        
fobj1.close()
fobj2.close()
