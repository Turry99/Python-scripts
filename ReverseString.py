#!/usr/bin/python3
#Get a string and output the reverse string
string = input("Write your string here and we will reverse it.\n>")

#Way #1
reverse1 = string[::-1]
print(reverse1)

#Way #2
reverse2 = reversed(string)
for x in reverse2:
    print(x, end='')
