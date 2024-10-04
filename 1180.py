'''
Beecrowd: Problema 1180
07/08/2024
Prof. Gregory --> Marcos Marçal Machado Junior
'''

N = int(input())

valores = input().split()
X = [int(valor) for valor in valores]

menorValor = X[0]
menorPosicao = 0

for i in range(1, N):
    if X[i] < menorValor:
        menorValor = X[i]
        menorPosicao = i


print(f"Menor valor: {menorValor}")
print(f"Posicao: {menorPosicao}")