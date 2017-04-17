import sys

"Simple matrix calculator"
f = []
g = []
h = []
try:
    nrTotal = int(input("X*X? (Matrice patratica , max4)\n>  "))
except ValueError:
    print("Ai gresit tu ceva sigur")
    sys.exit(0)

for x in range(0,nrTotal):
    f.append(x)
    g.append(x)
    h.append(x)


# Define functions

def Suma():
    for x in range(0,nrTotal**2):
        h[x] = f[x] + g[x]

def Multiply():
    if nrTotal == 2:
        h[0] = f[0] * g[0] + f[1] * g[2]
        h[1] = f[0] * g[1] + f[1] * g[3]
        h[2] = f[2] * g[0] + f[3] * g[2]
        h[3] = f[2] * g[1] + f[3] * g[3]
    elif nrTotal == 3:
        h[0] = f[0] * g[0] + f[1] * g[3] + f[2] * g[6]
        h[1] = f[0] * g[1] + f[1] * g[4] + f[2] * g[7]
        h[2] = f[0] * g[2] + f[1] * g[5] + f[2] * g[8]
        h[3] = f[3] * g[0] + f[4] * g[3] + f[5] * g[6]
        h[4] = f[3] * g[1] + f[4] * g[4] + f[5] * g[7]
        h[5] = f[3] * g[2] + f[4] * g[5] + f[5] * g[8]
        h[6] = f[6] * g[0] + f[7] * g[3] + f[8] * g[6]
        h[7] = f[6] * g[1] + f[7] * g[4] + f[8] * g[7]
        h[8] = f[6] * g[2] + f[7] * g[5] + f[8] * g[8]
    elif nrTotal == 4:
        h[0] = f[0]   * g[0] + f[1]  * g[4] + f[2]  * g[8]  + f[3]  * g[12]
        h[1] = f[4]   * g[1] + f[5]  * g[5] + f[6]  * g[9]  + f[7]  * g[13]
        h[2] = f[8]   * g[2] + f[9]  * g[6] + f[10] * g[10] + f[11] * g[14]
        h[3] = f[12]  * g[3] + f[13] * g[7] + f[14] * g[11] + f[15] * g[15]
        h[4] = f[0]   * g[0] + f[1]  * g[4] + f[2]  * g[8]  + f[3]  * g[12]
        h[5] = f[4]   * g[1] + f[5]  * g[5] + f[6]  * g[9]  + f[7]  * g[13]
        h[6] = f[8]   * g[2] + f[9]  * g[6] + f[10] * g[10] + f[11] * g[14]
        h[7] = f[12]  * g[3] + f[13] * g[7] + f[14] * g[11] + f[15] * g[15]
        h[8] = f[0]   * g[0] + f[1]  * g[4] + f[2]  * g[8]  + f[3]  * g[12]
        h[9] = f[4]   * g[1] + f[5]  * g[5] + f[6]  * g[9]  + f[7]  * g[13]
        h[10] = f[8]  * g[2] + f[9]  * g[6] + f[10] * g[10] + f[11] * g[14]
        h[11] = f[12] * g[3] + f[13] * g[7] + f[14] * g[11] + f[15] * g[15]
        h[12] = f[0]  * g[0] + f[1]  * g[4] + f[2]  * g[8]  + f[3]  * g[12]
        h[13] = f[4]  * g[1] + f[5]  * g[5] + f[6]  * g[9]  + f[7]  * g[13]
        h[14] = f[8]  * g[2] + f[9]  * g[6] + f[10] * g[10] + f[11] * g[14]
        h[15] = f[12] * g[3] + f[13] * g[7] + f[14] * g[11] + f[15] * g[15]
    else:
        print("Something went wrong")



def Invers():
    if nrTotal == 2:
        #Determinantul
        det = (f[0] * f[3]) - (f[1] * f[2])
        print("Determinantul e {}".format(det))
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
            
    elif nrTotal == 3:
        #Determinantul
        det = f[0]*f[4]*f[8] + f[3]*f[7]*f[2] + f[6]*f[1]*f[5] - f[2]*f[4]*f[6] - f[5]*f[7]*f[0] - f[8]*f[1]*f[3]
        print("Determinantul e {}".format(det))
        if det == 0:
            print("Matricea nu poate avea inversa, Determinantul = 0")
            sys.exit(0)
        # A*
        f[1], f[2] , f[5] = f[3] , f[6] , f[7]
        k = f
        f[0] = k[4]*k[8] - k[7]*k[5]
        f[1] = -(k[3]*k[8] - k[5]*k[6])
        f[2] = k[3] * k[7] - k[4] * k[6]
        f[3] = -(k[1]*k[8] - k[2]*k[7])
        f[4] = k[0]*k[8] - k[2]*k[6]
        f[5] = -(k[0]*k[7] - k[1]*k[6])
        f[6] = k[1]*k[5] - k[2]*k[4]
        f[7] = -(k[0]*k[5] - k[2]*k[3])
        f[8] =k[0]*k[4] - k[1]*k[3]
        det = 1/det
        
    # 1/det(A) * A*
    for x in range(0,nrTotal**2):
        h[x] = det * f[x]

try:
    if nrTotal == 2:
        f[0] , f[1], f[2], f[3] = input("Pune valorile pentru prima matrice (Merge doar cu matrice patratice)\n> ").split()
        g[0] , g[1], g[2], g[3] = input("Pune valorile pentru a doua matrice (Merge doar cu matrice patratice)\n> ").split()
    elif nrTotal == 3:
        f[0] , f[1], f[2], f[3],f[4] , f[5], f[6], f[7], f[8] = input("Pune valorile pentru prima matrice\n> ").split()
        g[0] , g[1], g[2],g[3], g[4],g[5] , g[6], g[7], g[8] = input("Pune valorile pentru a doua matrice\n> ").split()
    elif nrTotal == 4:
        f[0] , f[1], f[2], f[3],f[4] , f[5], f[6], f[7],f[8] , f[9], f[10], f[11],f[12] , f[13], f[14], f[15] = input("Pune valorile pentru prima matrice (Merge doar cu matrice patratice)\n> ").split()
        g[0] , g[1], g[2], g[3],g[4] , g[5], g[6], g[7],g[8] , g[9], g[10], g[11],g[12] , g[13], g[14], g[15] = input("Pune valorile pentru a doua matrice (Merge doar cu matrice patratice)\n> ").split()
    else:
        print("??")
        sys.exit(0)
except ValueError:
    print("Nu ai pus ceva bine")
    sys.exit(0)


#Transform the strings from lists into integers
f = list(map(int, f))
g = list(map(int, g))

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



for x in range(0,nrTotal**2):
    print("Element {} has the value of {} ".format(x+1,str(h[x])))
