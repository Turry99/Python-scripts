import random

colors = [
"\033[30m","\033[31m","\033[32m","\033[33m","\033[34m","\033[35m","\033[36m","\033[37m",
]

for x in range(70):
  string = "Insert the text here"
  for char in string:
    print(colors[random.randint(0,7)] + char, end='')
  print()
