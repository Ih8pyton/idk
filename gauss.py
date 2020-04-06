import numpy as np
from numpy import linalg

def mult(a, b):
    n1 = len(a)
    n2 = len(a[0])
    g2 = len(b[0])
    c = np.zeros(n1*g2).reshape(n1, g2).astype(float)
    for i in range(n1):
        for j in range(g2):
            for k in range(n1):
                c[i][j] += a[i][k]*b[k][j]
    return c

def gauss(a, b):

    a_2 = linalg.inv(a)
    c = mult(a_2, b)
    return c

a = [
    [1,2,1],
    [3,2,3],
    [1,0,0]
]
b = [[5], [6], [7]]

print( gauss(a, b) )
