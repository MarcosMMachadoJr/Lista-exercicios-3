'''
Beecrowd: Problema 1177
07/08/2024
Prof. Gregory --> Marcos Marçal Machado Junior
'''

N = [0] * 1000
T = int(input())

for i in range(1000):
    N[i] = i % T  

for i in range(len(N)):
    print(f"N[{i}] = {N[i]}")