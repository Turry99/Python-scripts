lista = []
def help():
    print('''
If you type HELP you will get this message.
If you type SHOW it will show you the list.
If you type DEL you will be prompt the list and help you delete.
If you type QUIT you will be prompt with the list.
If you type ADD you will be able to add things in the list.
''')
help()
while True:
    inp = input("> ")
    if inp == "HELP":
        help()
        continue
    elif inp == "SHOW":
        for items in lista:
            print(items)
        continue
    elif inp == "QUIT":
        break
    elif inp == "ADD":
        add = input("Add one item at the time please\n>  ")
        lista.append(add)
        continue
    elif inp == "DEL":
        for item in lista:
            print(item)
        de = input("Input the number of the item you want to delete\n>  ")
        del lista[de]
        continue
k = input("You want to see the list? Y/N").lower()
if k == "y":
    for item in lista:
        print(item)
else:
    print("Have a great day!")

    