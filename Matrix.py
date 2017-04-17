import sys

"Simple matrix calculator"
h = [0,0,0,0]
f = [0,0,0,0]
g = [0,0,0,0]

"""
try:
    linii, coloane = input("Cate linii si cate coloane? (Separeta them by a space)\n>  ").split()
except ValueError:
    print("Ai gresit tu ceva sigur")
    sys.exit(0)
"""


# Define functions

def Suma():
    for x in range(0,4):
        h[x] = f[x] + g[x]

def Multiply():
    h[0] = f[0] * g[0] + f[1] * g[2]
    h[1] = f[0] * g[1] + f[1] * g[3]
    h[2] = f[2] * g[0] + f[3] * g[2]
    h[3] = f[2] * g[1] + f[3] * g[3]

def Invers():
    #Determinantul
    det = (f[0] * f[3]) - (f[1] * f[2])
    if det == 0:
        print("Matricea nu poate avea inversa, Determinantul = 0")
        sys.exit(0)
    # A*
    f[3], f[0] = f[0] , f[3]
    f[1] *= -1
    f[2] *= -1

    # 1/det(A) * A*
    #Setam det sa fie 1/det pentru a nu o face in loop
    det = 1/det
    for x in range(0,4):
        h[x] = det * f[x]

try:
    f[0] , f[1], f[2], f[3] = input("Pune valorile pentru prima matrice (Merge doar cu 2x2 momentan)\n> ").split()
    g[0] , g[1], g[2], g[3] = input("Pune valorile pentru a doua matrice (Merge doar cu 2x2 momentan)\n> ").split()
except ValueError:
    print("Nu ai pus ceva bine")
    sys.exit(0)


action = input("Suma (S) , Multiply (M), Inversa (I)")[0]
if action == 'S':
    Suma()
elif action == 'M':
    Multiply()
elif action == 'S':
    Invers()
else:
    print("???")
    sys.exit(0)


#Transform the strings from lists into integers
f = list(map(int, f))
g = list(map(int, g))


for x in range(0,4):
    print("Element {} has the value of {} ".format(x+1,str(h[x])))
