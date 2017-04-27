"""
PacktHub offers a free book everyday and because I'm lazy you can get the title of the book and the link.
"""

import requests, re
from bs4 import BeautifulSoup as bs

link = "https://www.packtpub.com/packt/offers/free-learning"

user_agent = "User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:12.0) Gecko/20100101 Firefox/21.0"
headers = {
	'User-Agent': user_agent,
	'From': 'Viorel@gmail.com',
} #Set the headers

request = requests.get(link, headers=headers) #Request the site
SiteObj = bs(request.text, 'html.parser') #BeautifulSoup object with the site
aElem = SiteObj.find_all('a', attrs={'class':'twelve-days-claim'}) #Find the a elem with the button
TitleElem = SiteObj.find_all('div', attrs={'class':'dotd-title'}) #Element with the title of the book
href = str(aElem).split('\"')[3] #Here is the link
print("*"*30)
print(str(TitleElem).split('h2')[1].replace('>', '').replace('<','').replace("/",'').lstrip()) #Clean the junk
print('https://www.packtpub.com' + href)
print("*"*30)

#DEBUG
#with open('test.txt','w') as f: 
#	f.write(request.text)

