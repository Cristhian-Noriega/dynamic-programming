def bodegon_dinamico(P, W):
    n = len(P)
    dp = [[0] * (W + 1) for _ in range(n + 1)]
    for i in range(1 , n + 1):
        for j in range(1, W + 1):
            if P[i - 1] <= j:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - P[i - 1]] + P[i - 1])
            else:
                dp[i][j] = dp[i - 1][j]
    return reconstruir_solucion(dp, P, W)


def reconstruir_solucion(dp, P, W):
    n = len(dp) - 1
    j = W
    seleccionados = []
    while n > 0 and j > 0:
        if dp[n][j] != dp[n - 1][j]:
            seleccionados.append(P[n - 1])
            j -= P[n - 1]
        n -= 1
    return seleccionados[::-1]  