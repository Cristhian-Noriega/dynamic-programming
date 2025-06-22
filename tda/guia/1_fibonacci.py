"""
Implementar un algoritmo que, utilizando programación dinámica, obtenga el valor del n-ésimo número de fibonacci.
Indicar y justificar la complejidad del algoritmo implementado. Definición:
n = 0 --> Debe devolver 1
n = 1 --> Debe devolver 1
n --> Debe devolver la suma entre los dos anteriores números de fibonacci (los fibonacci n-2 y n-1)
"""

def fibonacci(n):
    dp = [0] * (n + 2)
    dp[0] = 0
    dp[1] = 1
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    print(dp)
    return dp[n]


print(fibonacci(9))  

