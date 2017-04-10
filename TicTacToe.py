# Puteam sa incerc sa il fac mai compact , dar pentru moment merge
# Sa definesc partea aia lunga rau de tot intr-o singura functie si sa las mai mult loc....dar pentru mai incolo

f1 = ' '
f2 = ' '
f3 = ' '
f4 = ' '
f5 = ' '
f6 = ' '
f7 = ' '
f8 = ' '
f9 = ' '
map = (' | a | b | c |\n1| ' +f1 +' | ' + f2 +' | ' +f3 +' |\n2| ' +f4 +' | ' +f5 +' | ' +f6 +' |\n3| ' +f7 +' | ' +f8 +' | ' +f9 +' |')    #Tabla
print(map)
for x in range(9):
    while x == 0:    # Prima tura
        rasp_1 = input('Jucatorul 1:\n').lower()
        if rasp_1 == 'a1':
            if f1 == ' ':
                f1 = 'X'
            else :
                print('Spatiul acela e deja ocupat , incearca altul')
                continue
        elif rasp_1 == 'a2':
            if f4 == ' ':
                f4 = 'X'
            else :
                print('Spatiul acela e deja ocupat , incearca altul')
                continue
        elif rasp_1 == 'a3':
            if f7 == ' ':
                f7 = 'X'
            else :
                print('Spatiul acela e deja ocupat , incearca altul')
                continue
        elif rasp_1 == 'b1':
            if f2 == ' ':
                f2 = 'X'
            else :
                print('Spatiul acela e deja ocupat , incearca altul')
                continue
        elif rasp_1 == 'b2':
            if f5 == ' ':
                f5 = 'X'
            else :
                print('Spatiul acela e deja ocupat , incearca altul')
                continue
        elif rasp_1 == 'b3':
            if f8 == ' ':
                f8 = 'X'
            else :
                print('Spatiul acela e deja ocupat , incearca altul')
                continue
        elif rasp_1 == 'c1':
            if f3 == ' ':
                f3 = 'X'
            else :
                print('Spatiul acela e deja ocupat , incearca altul')
                continue
        elif rasp_1 == 'c2':
            if f6 == ' ':
                f6 = 'X'
            else :
                print('Spatiul acela e deja ocupat , incearca altul')
                continue
        elif rasp_1 == 'c3':
            if f9 == ' ':
                f9 = 'X'
            else :
                print('Spatiul acela e deja ocupat , incearca altul')
                continue
        else:
            print('Ai gresit coordonatele , incearca din nou')
            continue
        print(' | a | b | c |\n1| ' +f1 +' | ' + f2 +' | ' +f3 +' |\n2| ' +f4 +' | ' +f5 +' | ' +f6 +' |\n3| ' +f7 +' | ' +f8 +' | ' +f9 +' |')
        rasp_1 = ''
        break
    while x == 1:     # A doua tura
        rasp_1 = input('Jucatorul 2:\n').lower()
        if rasp_1 == 'a1':
            if f1 == ' ':
                f1 = 'O'
            else :
                print('Spatiul acela e deja ocupat , incearca altul')
                continue
        elif rasp_1 == 'a2':
            if f4 == ' ':
                f4 = 'O'
            else :
                print('Spatiul acela e deja ocupat , incearca altul')
                continue
        elif rasp_1 == 'a3':
            if f7 == ' ':
                f7 = 'O'
            else :
                print('Spatiul acela e deja ocupat , incearca altul')
                continue
        elif rasp_1 == 'b1':
            if f2 == ' ':
                f2 = 'O'
            else :
                print('Spatiul acela e deja ocupat , incearca altul')
                continue
        elif rasp_1 == 'b2':
            if f5 == ' ':
                f5 = 'O'
            else :
                print('Spatiul acela e deja ocupat , incearca altul')
                continue
        elif rasp_1 == 'b3':
            if f8 == ' ':
                f8 = 'O'
            else :
                print('Spatiul acela e deja ocupat , incearca altul')
                continue
        elif rasp_1 == 'c1':
            if f3 == ' ':
                f3 = 'O'
            else :
                print('Spatiul acela e deja ocupat , incearca altul')
                continue
        elif rasp_1 == 'c2':
            if f6 == ' ':
                f6 = 'O'
            else :
                print('Spatiul acela e deja ocupat , incearca altul')
                continue
        elif rasp_1 == 'c3':
            if f9 == ' ':
                f9 = 'O'
            else :
                print('Spatiul acela e deja ocupat , incearca altul')
                continue
        print(' | a | b | c |\n1| ' +f1 +' | ' + f2 +' | ' +f3 +' |\n2| ' +f4 +' | ' +f5 +' | ' +f6 +' |\n3| ' +f7 +' | ' +f8 +' | ' +f9 +' |')
        rasp_1 = ''
        break
    while x == 2:     # A treia tura 
        rasp_1 = input('Jucatorul 1:\n').lower()
        if rasp_1 == 'a1':
            if f1 == ' ':
                f1 = 'X'
            else :
                print('Spatiul acela e deja ocupat , incearca altul')
                continue
        elif rasp_1 == 'a2':
            if f4 == ' ':
                f4 = 'X'
            else :
                print('Spatiul acela e deja ocupat , incearca altul')
                continue
        elif rasp_1 == 'a3':
            if f7 == ' ':
                f7 = 'X'
            else :
                print('Spatiul acela e deja ocupat , incearca altul')
                continue
        elif rasp_1 == 'b1':
            if f2 == ' ':
                f2 = 'X'
            else :
                print('Spatiul acela e deja ocupat , incearca altul')
                continue
        elif rasp_1 == 'b2':
            if f5 == ' ':
                f5 = 'X'
            else :
                print('Spatiul acela e deja ocupat , incearca altul')
                continue
        elif rasp_1 == 'b3':
            if f8 == ' ':
                f8 = 'X'
            else :
                print('Spatiul acela e deja ocupat , incearca altul')
                continue
        elif rasp_1 == 'c1':
            if f3 == ' ':
                f3 = 'X'
            else :
                print('Spatiul acela e deja ocupat , incearca altul')
                continue
        elif rasp_1 == 'c2':
            if f6 == ' ':
                f6 = 'X'
            else :
                print('Spatiul acela e deja ocupat , incearca altul')
                continue
        elif rasp_1 == 'c3':
            if f9 == ' ':
                f9 = 'X'
            else :
                print('Spatiul acela e deja ocupat , incearca altul')
                continue
        else:
            print('Ai gresit coordonatele , incearca din nou')
            continue
        print(' | a | b | c |\n1| ' +f1 +' | ' + f2 +' | ' +f3 +' |\n2| ' +f4 +' | ' +f5 +' | ' +f6 +' |\n3| ' +f7 +' | ' +f8 +' | ' +f9 +' |')
        rasp_1 = ''
        break
    while x == 3:      # A patra tura
        rasp_1 = input('Jucatorul 2:\n').lower()
        if rasp_1 == 'a1':
            if f1 == ' ':
                f1 = 'O'
            else :
                print('Spatiul acela e deja ocupat , incearca altul')
                continue
        elif rasp_1 == 'a2':
            if f4 == ' ':
                f4 = 'O'
            else :
                print('Spatiul acela e deja ocupat , incearca altul')
                continue
        elif rasp_1 == 'a3':
            if f7 == ' ':
                f7 = 'O'
            else :
                print('Spatiul acela e deja ocupat , incearca altul')
                continue
        elif rasp_1 == 'b1':
            if f2 == ' ':
                f2 = 'O'
            else :
                print('Spatiul acela e deja ocupat , incearca altul')
                continue
        elif rasp_1 == 'b2':
            if f5 == ' ':
                f5 = 'O'
            else :
                print('Spatiul acela e deja ocupat , incearca altul')
                continue
        elif rasp_1 == 'b3':
            if f8 == ' ':
                f8 = 'O'
            else :
                print('Spatiul acela e deja ocupat , incearca altul')
                continue
        elif rasp_1 == 'c1':
            if f3 == ' ':
                f3 = 'O'
            else :
                print('Spatiul acela e deja ocupat , incearca altul')
                continue
        elif rasp_1 == 'c2':
            if f6 == ' ':
                f6 = 'O'
            else :
                print('Spatiul acela e deja ocupat , incearca altul')
                continue
        elif rasp_1 == 'c3':
            if f9 == ' ':
                f9 = 'O'
            else :
                print('Spatiul acela e deja ocupat , incearca altul')
                continue
        print(' | a | b | c |\n1| ' +f1 +' | ' + f2 +' | ' +f3 +' |\n2| ' +f4 +' | ' +f5 +' | ' +f6 +' |\n3| ' +f7 +' | ' +f8 +' | ' +f9 +' |')
        rasp_1 = ''
        break
    while x == 4:      # A cincea tura
        rasp_1 = input('Jucatorul 1:\n').lower()
        if rasp_1 == 'a1':
            if f1 == ' ':
                f1 = 'X'
            else :
                print('Spatiul acela e deja ocupat , incearca altul')
                continue
        elif rasp_1 == 'a2':
            if f4 == ' ':
                f4 = 'X'
            else :
                print('Spatiul acela e deja ocupat , incearca altul')
                continue
        elif rasp_1 == 'a3':
            if f7 == ' ':
                f7 = 'X'
            else :
                print('Spatiul acela e deja ocupat , incearca altul')
                continue
        elif rasp_1 == 'b1':
            if f2 == ' ':
                f2 = 'X'
            else :
                print('Spatiul acela e deja ocupat , incearca altul')
                continue
        elif rasp_1 == 'b2':
            if f5 == ' ':
                f5 = 'X'
            else :
                print('Spatiul acela e deja ocupat , incearca altul')
                continue
        elif rasp_1 == 'b3':
            if f8 == ' ':
                f8 = 'X'
            else :
                print('Spatiul acela e deja ocupat , incearca altul')
                continue
        elif rasp_1 == 'c1':
            if f3 == ' ':
                f3 = 'X'
            else :
                print('Spatiul acela e deja ocupat , incearca altul')
                continue
        elif rasp_1 == 'c2':
            if f6 == ' ':
                f6 = 'X'
            else :
                print('Spatiul acela e deja ocupat , incearca altul')
                continue
        elif rasp_1 == 'c3':
            if f9 == ' ':
                f9 = 'X'
            else :
                print('Spatiul acela e deja ocupat , incearca altul')
                continue
        else:
            print('Ai gresit coordonatele , incearca din nou')
            continue
        print(' | a | b | c |\n1| ' +f1 +' | ' + f2 +' | ' +f3 +' |\n2| ' +f4 +' | ' +f5 +' | ' +f6 +' |\n3| ' +f7 +' | ' +f8 +' | ' +f9 +' |')
        rasp_1 = ''
        break
    while x == 5:       # A sasea tura
        rasp_1 = input('Jucatorul 2:\n').lower()
        if rasp_1 == 'a1':
            if f1 == ' ':
                f1 = 'O'
            else :
                print('Spatiul acela e deja ocupat , incearca altul')
                continue
        elif rasp_1 == 'a2':
            if f4 == ' ':
                f4 = 'O'
            else :
                print('Spatiul acela e deja ocupat , incearca altul')
                continue
        elif rasp_1 == 'a3':
            if f7 == ' ':
                f7 = 'O'
            else :
                print('Spatiul acela e deja ocupat , incearca altul')
                continue
        elif rasp_1 == 'b1':
            if f2 == ' ':
                f2 = 'O'
            else :
                print('Spatiul acela e deja ocupat , incearca altul')
                continue
        elif rasp_1 == 'b2':
            if f5 == ' ':
                f5 = 'O'
            else :
                print('Spatiul acela e deja ocupat , incearca altul')
                continue
        elif rasp_1 == 'b3':
            if f8 == ' ':
                f8 = 'O'
            else :
                print('Spatiul acela e deja ocupat , incearca altul')
                continue
        elif rasp_1 == 'c1':
            if f3 == ' ':
                f3 = 'O'
            else :
                print('Spatiul acela e deja ocupat , incearca altul')
                continue
        elif rasp_1 == 'c2':
            if f6 == ' ':
                f6 = 'O'
            else :
                print('Spatiul acela e deja ocupat , incearca altul')
                continue
        elif rasp_1 == 'c3':
            if f9 == ' ':
                f9 = 'O'
            else :
                print('Spatiul acela e deja ocupat , incearca altul')
                continue
        print(' | a | b | c |\n1| ' +f1 +' | ' + f2 +' | ' +f3 +' |\n2| ' +f4 +' | ' +f5 +' | ' +f6 +' |\n3| ' +f7 +' | ' +f8 +' | ' +f9 +' |')
        rasp_1 = ''
        break
    while x == 6:       # A saptea tura
        rasp_1 = input('Jucatorul 1:\n').lower()
        if rasp_1 == 'a1':
            if f1 == ' ':
                f1 = 'X'
            else :
                print('Spatiul acela e deja ocupat , incearca altul')
                continue
        elif rasp_1 == 'a2':
            if f4 == ' ':
                f4 = 'X'
            else :
                print('Spatiul acela e deja ocupat , incearca altul')
                continue
        elif rasp_1 == 'a3':
            if f7 == ' ':
                f7 = 'X'
            else :
                print('Spatiul acela e deja ocupat , incearca altul')
                continue
        elif rasp_1 == 'b1':
            if f2 == ' ':
                f2 = 'X'
            else :
                print('Spatiul acela e deja ocupat , incearca altul')
                continue
        elif rasp_1 == 'b2':
            if f5 == ' ':
                f5 = 'X'
            else :
                print('Spatiul acela e deja ocupat , incearca altul')
                continue
        elif rasp_1 == 'b3':
            if f8 == ' ':
                f8 = 'X'
            else :
                print('Spatiul acela e deja ocupat , incearca altul')
                continue
        elif rasp_1 == 'c1':
            if f3 == ' ':
                f3 = 'X'
            else :
                print('Spatiul acela e deja ocupat , incearca altul')
                continue
        elif rasp_1 == 'c2':
            if f6 == ' ':
                f6 = 'X'
            else :
                print('Spatiul acela e deja ocupat , incearca altul')
                continue
        elif rasp_1 == 'c3':
            if f9 == ' ':
                f9 = 'X'
            else :
                print('Spatiul acela e deja ocupat , incearca altul')
                continue
        else:
            print('Ai gresit coordonatele , incearca din nou')
            continue
        print(' | a | b | c |\n1| ' +f1 +' | ' + f2 +' | ' +f3 +' |\n2| ' +f4 +' | ' +f5 +' | ' +f6 +' |\n3| ' +f7 +' | ' +f8 +' | ' +f9 +' |')
        rasp_1 = ''
        break
    while x == 7:       # A opta tura
        rasp_1 = input('Jucatorul 2:\n').lower()
        if rasp_1 == 'a1':
            if f1 == ' ':
                f1 = 'O'
            else :
                print('Spatiul acela e deja ocupat , incearca altul')
                continue
        elif rasp_1 == 'a2':
            if f4 == ' ':
                f4 = 'O'
            else :
                print('Spatiul acela e deja ocupat , incearca altul')
                continue
        elif rasp_1 == 'a3':
            if f7 == ' ':
                f7 = 'O'
            else :
                print('Spatiul acela e deja ocupat , incearca altul')
                continue
        elif rasp_1 == 'b1':
            if f2 == ' ':
                f2 = 'O'
            else :
                print('Spatiul acela e deja ocupat , incearca altul')
                continue
        elif rasp_1 == 'b2':
            if f5 == ' ':
                f5 = 'O'
            else :
                print('Spatiul acela e deja ocupat , incearca altul')
                continue
        elif rasp_1 == 'b3':
            if f8 == ' ':
                f8 = 'O'
            else :
                print('Spatiul acela e deja ocupat , incearca altul')
                continue
        elif rasp_1 == 'c1':
            if f3 == ' ':
                f3 = 'O'
            else :
                print('Spatiul acela e deja ocupat , incearca altul')
                continue
        elif rasp_1 == 'c2':
            if f6 == ' ':
                f6 = 'O'
            else :
                print('Spatiul acela e deja ocupat , incearca altul')
                continue
        elif rasp_1 == 'c3':
            if f9 == ' ':
                f9 = 'O'
            else :
                print('Spatiul acela e deja ocupat , incearca altul')
                continue
        print(' | a | b | c |\n1| ' +f1 +' | ' + f2 +' | ' +f3 +' |\n2| ' +f4 +' | ' +f5 +' | ' +f6 +' |\n3| ' +f7 +' | ' +f8 +' | ' +f9 +' |')
        rasp_1 = ''
        break
    while x == 8:       # A noua tura
        rasp_1 = input('Jucatorul 1:\n').lower()
        if rasp_1 == 'a1':
            if f1 == ' ':
                f1 = 'X'
            else :
                print('Spatiul acela e deja ocupat , incearca altul')
                continue
        elif rasp_1 == 'a2':
            if f4 == ' ':
                f4 = 'X'
            else :
                print('Spatiul acela e deja ocupat , incearca altul')
                continue
        elif rasp_1 == 'a3':
            if f7 == ' ':
                f7 = 'X'
            else :
                print('Spatiul acela e deja ocupat , incearca altul')
                continue
        elif rasp_1 == 'b1':
            if f2 == ' ':
                f2 = 'X'
            else :
                print('Spatiul acela e deja ocupat , incearca altul')
                continue
        elif rasp_1 == 'b2':
            if f5 == ' ':
                f5 = 'X'
            else :
                print('Spatiul acela e deja ocupat , incearca altul')
                continue
        elif rasp_1 == 'b3':
            if f8 == ' ':
                f8 = 'X'
            else :
                print('Spatiul acela e deja ocupat , incearca altul')
                continue
        elif rasp_1 == 'c1':
            if f3 == ' ':
                f3 = 'X'
            else :
                print('Spatiul acela e deja ocupat , incearca altul')
                continue
        elif rasp_1 == 'c2':
            if f6 == ' ':
                f6 = 'X'
            else :
                print('Spatiul acela e deja ocupat , incearca altul')
                continue
        elif rasp_1 == 'c3':
            if f9 == ' ':
                f9 = 'X'
            else :
                print('Spatiul acela e deja ocupat , incearca altul')
                continue
        else:
            print('Ai gresit coordonatele , incearca din nou')
            continue
        print(' | a | b | c |\n1| ' +f1 +' | ' + f2 +' | ' +f3 +' |\n2| ' +f4 +' | ' +f5 +' | ' +f6 +' |\n3| ' +f7 +' | ' +f8 +' | ' +f9 +' |')
        rasp_1 = ''
        break
#Aici e cand primul jucator castiga
if f1 == 'X' and f2 == 'X' and f3 == 'X':
    print('\nJucatorul 1 a castigat.')
elif f4 == 'X' and f5 == 'X' and f6 == 'X':
    print('\nJucatorul 1 a castigat.')
elif f7 == 'X' and f8 == 'X' and f9 == 'X':
    print('\nJucatorul 1 a castigat.')
elif f1 == 'X' and f5 == 'X' and f9 == 'X':
    print('\nJucatorul 1 a castigat.')
elif f7 == 'X' and f5 == 'X' and f3 == 'X':
    print('\nJucatorul 1 a castigat.')
elif f1 == 'X' and f4 == 'X' and f7 == 'X':
    print('\Jucatorul 1 a castigat.')
elif f2 == 'X' and f5 == 'X' and f8 == 'X':
    print('\nJucatorul 1 a castigat.')
elif f3 == 'X' and f6 == 'X' and f9 == 'X':
    print('\nJucatorul 1 a castigat.')
# De aici incepe al doilea jucator
elif f1 == 'O' and f2 == 'O' and f3 == 'O':
    print('\nJucatorul 2 a castigat.')
elif f4 == 'O' and f5 == 'O' and f6 == 'O':
    print('\nJucatorul 2 a castigat.')
elif f7 == 'O' and f8 == 'O' and f9 == 'O':
    print('\nJucatorul 2 a castigat.')
elif f1 == 'O' and f5 == 'O' and f9 == 'O':
    print('\nJucatorul 2 a castigat.')
elif f7 == 'O' and f5 == 'O' and f3 == 'O':
    print('\nJucatorul 2 a castigat.')
elif f1 == 'O' and f4 == 'O' and f7 == 'O':
    print('\Jucatorul 2 a castigat.')
elif f2 == 'O' and f5 == 'O' and f8 == 'O':
    print('\nJucatorul 2 a castigat.')
elif f3 == 'O' and f6 == 'O' and f9 == 'O':
    print('\nJucatorul 2 a castigat.')
