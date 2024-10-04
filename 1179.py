'''
Beecrowd: Problema 1179
07/08/2024
Prof. Gregory --> Marcos Marçal Machado Junior
'''

Par = []
Impar = []


for i in range(15):
    Num = int(input())
    if(Num % 2 == 0):
        Par.append(Num)
        if len(Par) == 5:
            for j in range(5):
                print(f"par[{j}] = {Par[j]}")
            Par.clear()

    else:
        Impar.append(Num)
        if len(Impar) ==  5:
            for j in range(5):
                print(f"impar[{j}] = {Impar[j]}")
            Impar.clear()

for i in range(len(Impar)):
    print(f"impar[{i}] = {Impar[i]}")

for i in range(len(Par)):
    print(f"par[{i}] = {Par[i]}")

