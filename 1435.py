'''
Beecrowd: Problema 1435
07/08/2024
Prof. Gregory --> Marcos Marçal Machado Junior
'''

x = 1
while x != 0:
    m = []
    t = int(input())
    x = t
    if t == 0:
        break
    for i in range(t):
        p = []
        for j in range(t):
            p.append(0)
        m.append(p)


        camadas = (t + 1) // 2  

    for elemento in range(1, camadas + 1):
        for i in range(elemento - 1, t - elemento + 1):
            for j in range(elemento - 1, t - elemento + 1):
                m[i][j] = elemento

    for i in m:
        print(' '.join(f"{num:>3}" for num in i))
    print()