'''
Beecrowd: Problema 1176
07/08/2024
Prof. Gregory --> Marcos Marçal Machado Junior
'''

fib = [0] * 61
fib[1] = 1

T = int(input())

for i in range(2, 61):
    fib[i] = fib[i - 1] + fib[i - 2]

for _ in range(T):
    N = int(input())  
    print(f"Fib({N}) = {fib[N]}")