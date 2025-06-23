"""
dado un conjunto de elementos óptimos, ¿cuál es el último paso que puedo haber tomado?
Defino los subproblemas como el valor maximo que puedo obtener al considerar los primeros i elementos y una capacidad de mochila W.
Tengo dos opciones, para cada elemento:
1. No incluir el elemento i, en cuyo caso el valor máximo es el mismo que al considerar los primeros i-1 elementos con la misma capacidad W.
2. Incluir el elemento i, en cuyo caso el valor máximo es el valor del elemento i más el valor máximo que puedo obtener
con los primeros i-1 elementos y una capacidad reducida en el peso del elemento i

OPT(i, W) = max(OPT(i-1, W), OPT(i-1, W - peso[i]) + valor[i]) si peso[i] <= W
"""

def mochila(elementos, W):
    n = len(elementos)
    dp = [[0] * (W + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(W + 1):
            valor, peso = elementos[i - 1]
            if peso <= j:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - peso] + valor)
            else:
                dp[i][j] = dp[i - 1][j]

    return reconstruir_solucion(dp, elementos)


def reconstruir_solucion(dp, elementos):
    i, j = len(dp) - 1, len(dp[0]) - 1
    solucion = []
    while i > 0 and j > 0:
        elemento = elementos[i - 1]
        valor, peso = elemento
        if dp[i][j] == dp[i - 1][j - peso] + valor:
            solucion.append(elemento)
            j -= peso
        i -= 1
        
    return solucion[::-1]