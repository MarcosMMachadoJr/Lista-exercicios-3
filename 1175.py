'''
Beecrowd: Problema 1175
07/08/2024
Prof. Gregory --> Marcos Marçal Machado Junior
'''

N = []

for n in range(20):
    X = int(input())
    N.append(X)

for i in range(10):
    Y = 19 - i
    N[i], N[Y] = N[Y], N[i]

for i in range(len(N)):
    print(f"N[{i}] = {N[i]}")