'''Python script to extract all the NHL teams and thier web pages
'''
from bs4 import BeautifulSoup

import requests


r = requests.get('https://en.wikipedia.org/wiki/National_Hockey_League') 


data = r.text

soup = BeautifulSoup(data)
#Extract the table
team_table = soup.find('table','navbox wikitable')

#Extract the rows
all_rows=team_table.find_all('tr')

for row in all_rows:
	#Extract all the columns for the row
    col=row.find_all('td')
    if len(col) > 0:
        print col[0].text,
        print col[0].find('a').get('href')
    else:
        pass
        #print row    
