'''
Beecrowd: Problema 1178
07/08/2024
Prof. Gregory --> Marcos Marçal Machado Junior
'''

N = [0] * 100
X = float(input())
N[0] = X

for i in range(1, 99):
    N[i] = N[i - 1] / 2

for i in range(len(N)):
    print(f"N[{i}] = {N[i]:.4f}")