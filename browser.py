import tkinter
from tkinter import Label
import requests
from bs4 import BeautifulSoup

#Setting these so the sites don't block you
user_agent = "User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:12.0) Gecko/20100101 Firefox/21.0"
headers = {
    'User-Agent': user_agent,
        'From': 'Viorel@gmail.com',
}

def cleanMe(html):
    '''Thanks to jamescampbell from StackOverflow for this.'''
    soup = BeautifulSoup(html, "html") # create a new bs4 object from the html data loaded
    for script in soup(["script", "style"]): # remove all javascript and stylesheet code
        script.extract()
    # get text
    text = soup.get_text()
    # break into lines and remove leading and trailing space on each
    lines = (line.strip() for line in text.splitlines())
    # break multi-headlines into a line each
    chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
    # drop blank lines
    text = '\n'.join(chunk for chunk in chunks if chunk)
    return text

def getLink(event=None):
    link = UrlBox.get()
    #Check if it has the http
    if link[:4] != "http":
        if link[:4] != "www.":
            link = 'www.' + link
        link = 'http://' + link
    try:
        results.delete('1.0', tkinter.END)
        request = requests.get(link,headers=headers)
        results.insert(tkinter.END, cleanMe(request.text))
    except:
        results.delete('1.0', tkinter.END)
        results.insert(tkinter.END, "The url is not working. Try again.")

#Setting the main stuff
root = tkinter.Tk()
root.title("A simple Browser")
width , height = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%x+0+0" % (width, height))

#Setting the url bar
UrlBox = tkinter.Entry(root, bd = 4)
UrlBox.pack(anchor = tkinter.N, fill=tkinter.X, expand=tkinter.YES)
UrlBox.bind("<Return>", getLink)

#Creating scrollbar
scrollbar = tkinter.Scrollbar(root)
scrollbar.pack(side=tkinter.RIGHT, fill=tkinter.Y)

#Setting the output area and attaching the scrollbar to it
results = tkinter.Text(root, bd=5)
results.config(wrap=tkinter.WORD, yscrollcommand=scrollbar.set)
scrollbar.config(command=results.yview)
results.pack(anchor=tkinter.CENTER, fill=tkinter.BOTH,expand=tkinter.YES)

root.mainloop()
