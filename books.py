'''
This will download all the books from http://www.freetechbooks.com
Author = Turry
'''

import requests, os, re
from bs4 import BeautifulSoup

link = "http://www.freetechbooks.com/topics?page=" #This will be the link that the thread will use (In case I will use multi-threading)


#Create the folder and open it
os.makedirs('Books', exist_ok=True)
os.chdir('./Books')


#Here we find the book's urls
setul = set() # We make a set so we won't get duplicates
request = requests.get(link) # Download the page
SiteObj = BeautifulSoup(request.text, 'html.parser') #Make a Soup Object out of the site
PElem = SiteObj.find_all('p', attrs={'class':'media-heading lead'}) # Search the p elements that contain the 'a' elems that we need
ElemObj = BeautifulSoup(str(PElem), 'html.parser') # We create another Soup Object out of the PElem
for link in ElemObj.find_all('a', href=True): #Here we find the book pages and store them in the set variable (setul)
	setul.add(link['href'])



Links = [] #We make a list to store Links to the PDFs
#Here we find the website of the pdfs
#<a class="btn btn-primary" href="link here"  ---> This is the download box
for PdfUrl in setul: #We loop through the set to get the book links
	PdfRequest = requests.get(PdfUrl) #We download the page
	PdfSoup = BeautifulSoup(PdfRequest.text, 'html.parser') #We create a Soup Object from the book url
	PdfLink = PdfSoup.find_all('a', attrs={'class':'btn btn-primary'}) #We find the pdf link
	PdfLink = str(PdfLink) #We convert it in a string
	if 'pdf' in PdfLink: # We check if the link contains .pdf in it. *Some of them are not directly pdf's...*
		Link = PdfLink[PdfLink.find("htt"):PdfLink.find('.pdf')] + '.pdf'  #We take the pdf link
		Links.append(Link) #We just add it to a list so we can use it later



chunk_size = 2000 #We set how much we download at the time
for x in range(len(Links)):
	r = requests.get(Links[x], stream=True)
	print("Downloading from page {}".format(Links[x]))
	with open(str(x)+'.pdf', 'wb') as f:
		for chunk in r.iter_content(chunk_size):
			f.write(chunk)




"""
Things to add:
Make it download from a certain page / range or pages
Make it work from command line
Maybe make it multi-thread but not sure since I don't want to slow the page down and cause trouble.
Make the names better , not just numbers.
"""





