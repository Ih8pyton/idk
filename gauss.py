import numpy as np

def gauss(a):
    n = len(a)
    
    for k in range(n):
            for i in range(k+1, n):
                    a[k] /= a[k][k]
                    a[i] -= a[k]*(a[i][k])
    a[n-1] /= a[n-1][n-1]

    for i in range(n):
            for j in range(i+1, n):
                    a[i] -= a[j]*a[i][j]

    a2 = []
    for i in range(n):
        a2.append(a[i][n])

    return a2

n = int(input('Размер матрицы уравнений? '))

a = np.zeros(n * (n+1)).reshape(n, n+1)

for i in range(n):
        print("Заполните через пробел", i+1, "строчку расширенной матрицы")
        a[i] = input().split(' ')
        for j in range(n+1):
                a[i][j] = float(a[i][j])

print(gauss(a))

