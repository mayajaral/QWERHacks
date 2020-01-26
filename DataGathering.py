#Imports
from bs4 import BeautifulSoup
import requests
import re
import json

website_url = requests.get('https://en.wikipedia.org/wiki/List_of_LGBT_characters_in_television_and_radio#Transgender').text
LGBTtvandradio = BeautifulSoup(website_url,'html.parser')
#print(LGBTtvandradio.prettify())
hyperlinks = LGBTtvandradio.find_all('a', {'href':True})
#print(hyperlinks)
#Procure All Tables
tables = LGBTtvandradio.findAll(lambda tag: tag.name=='table' and tag.has_attr('class') and tag['class']==['wikitable', 'sortable'])

#Procure all rows in all tables
trsbisexual = tables[0].tbody.findAll(lambda tag: tag.name=='tr')
trsgay = tables[1].tbody.findAll(lambda tag: tag.name=='tr')
trslesbian = tables[2].tbody.findAll(lambda tag: tag.name=='tr')
trstransgender = tables[3].tbody.findAll(lambda tag: tag.name=='tr')

#print(trsbisexual[n].td) #Functional Example
#print(trsbisexual)
trsbisexualrows = trsbisexual[1].findAll(lambda tag: tag.name == 'td') #Functional example get a row
#print(trsbisexualrows[0]) #Functionally get character name
#print(trsbisexualrows)
blength = len(trsbisexual)
characternames = []
actornames = []
for n in range(1, blength):
    rows = trsbisexual[n].findAll(lambda tag: tag.name == 'td')
    charactername = rows[0]

    characternames.append(charactername)
    actorname = rows[1]
    actornames.append(actorname)
print(characternames)
#print(type(str(characternames[2])))
#str(characternames[2])
regex = r"<td><a[^>]*>([^<]*)</a></td>"
match = re.search(regex, str(characternames[2]))
print(match.group(1))
    #print(actorname)


#print(actornames)
#data ={"Character name":"", "Actor name":"", "TV Shows:"", "Sexuality": "", "Gender" : ""}




