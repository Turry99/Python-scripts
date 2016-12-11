#!/usr/bin/env python3
"""
A simple game of hanged man.
"""
import random
#We could use r'' but I'm to lazy
#Best pixel art
first ="""
   o
"""
second ="""
   o
   | 
"""
third ="""
   o
   |\\
"""
forth ="""
   o
  /|\\
"""
fifth ="""
   o
  /|\\
  / 
"""
last ="""
   o
  /|\\
  / \\
"""

draw = {
	0:'',
	1:first,
	2:second,
	3:third,
	4:forth,
	5:fifth,
	6:last,
}
#Here you just add your words
word = ['carar', 'catat', 'vioreliov', 'bagrieladasa']

def main():
	#The welcome shit
	print("We will have you to guess some random fucking words.\nGood luck.\n\n")
	#We split the word in letters
	guess = [q for q in word[random.randint(0,len(word)-1)]]
	show = ['_' for  x in range(len(guess))]
	wrong = 0
	while wrong <= 6:
		print(draw[wrong])
		print(show)
		ask = input("\nInput a single letter.\nInput more and it will just take 1 life.\n>>>\t")
		if ask in guess:
			while ask in guess:
				show[guess.index(ask)] = ask
				guess[guess.index(ask)] = ''
		else:
			wrong += 1
		if '_' not in show:
			print("\n\nCongratulations. You won this shit")
			break


if __name__ == '__main__':
	main()