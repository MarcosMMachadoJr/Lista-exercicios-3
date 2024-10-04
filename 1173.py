'''
Beecrowd: Problema 1173
07/08/2024
Prof. Gregory --> Marcos Marçal Machado Junior
'''

N = []

while True:
    V = int(input())
    if V <= 50:
        break

N.append(V)
for n in range(1, 10):
    V = N[-1] * 2
    N.append(V)
for i in range(len(N)):
    print(f"N[{i}] = {N[i]}")
