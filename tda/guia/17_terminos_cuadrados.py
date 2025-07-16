import math

def terminos(n):
    opt = [0] * (n+1)
    for i in range(1, n + 1):
        minimo = i
        for j in range(1, int(math.sqrt(i)) + 1):
            minimo = min(minimo, 1 + opt[i - j * j])
        opt[i] = minimo

    return opt[n]