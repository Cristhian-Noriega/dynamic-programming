def carlitos(c_publicitaria, P):
    n = len(c_publicitaria)
    dp = [[0] * (P + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        g_i, c_i = c_publicitaria[i - 1]
        for j in range(1, P + 1):
            if c_i <= j:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - c_i] + g_i)
            else:
                dp[i][j] = dp[i - 1][j]
    return reconstruir_solucion(dp, c_publicitaria, P)



def reconstruir_solucion(dp, c_publicitaria, P):
    sol = []
    i, j = len(c_publicitaria), P
    while i > 0 and j > 0:
        g_i, c_i = c_publicitaria[i - 1]
        if c_i <= j and dp[i][j] == dp[i - 1][j - c_i] + g_i:
            sol.append(c_publicitaria[i - 1])
            j -= c_i
        i -= 1
    return sol[::-1]  