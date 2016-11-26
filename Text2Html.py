'''
This script will turn .txt files into .html files and makes it easier for people that don't know html.
'''

"""
HIGH LEVEL:
Cauta in text sa vezi daca exista tag-ul de HTML, dupa cauta head sau title iar la sfarsit cauta body.
Daca nimic nu e pus , titlul va fi pus default (Page) iar textul va fi pus in body.
Cauta sa vezi daca sunt tag-uri (--p/--l etc), daca sunt, inlocuieste acel tag cu tag-ul HTML si cauta ///tagname.
Daca nu sunt inchise tag-urile , inchidele automat la sfarsit de document.
Daca e --l , inlocuieste-l doar cu un <br> si atat.
In caz de vreo eroare, incearca sa o redai (Asta era logica)
La sfarsit pune si tu un mesaj mescher.
Daca un tag nou incepe de acelasi tip (ex color) dar celalalt nu a fost inchis , inchide-l automat.
"""
import re, os, sys

colors = ['BLUE', 'RED', 'GREEN']
tags = {'--p':'<p>', '-paragraph':'<p>', '--l':'<br>', '-line':'<br>', '///p':'</p>', '///paragraph':'</p>'}


def help():
	print('''
This script is meant to help people transform .txt files into html with no knowledge of HTML hardly any changes to the text.
Tags:
--p or -paragraph             It makes the line into a paragraph.
--l or -line                  It adds a new line. This can be done with just pressing enter in the file.
///TagName                    It ends the tag.
--c:Color or -color:Color     It makes the text colored.Be sure to use the /// to end the tag or else all the text will be colored. 
--title                       It adds a title to the document.
		''')
found = 0 #We set a variable so we know that its found
new_file = [] #We hold the new text
thingy = [] #We hold the values that we've modified
def main(file_name):
	with open(file_name) as f:
		for line in f:
			found = 0
			for tag in tags:
				if found == 1:
					break
				if re.search(tag, line):
					thingy.append(line)
					line = line.replace(tag, tags[tag])
					new_file.append(line)
					found = 1
					break
				else:
					if line not in thingy:
						thingy.append(line)
			if found == 0:
				new_file.append(line)
	for x in new_file:
		print(x)







if __name__ == '__main__':
	try:
		file_name = sys.argv[1]
		main(file_name)
	except:
		help()