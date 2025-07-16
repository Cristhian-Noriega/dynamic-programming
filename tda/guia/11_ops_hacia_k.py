def operaciones(k):
    if k == 0:
        return []
    dp = [0] * (k + 1)
    dp[0] = 0
    dp[1] = 1

    for i in range(2, k + 1):
        if i % 2 != 0:
            dp[i] = dp[i - 1] + 1
            continue

        dp[i] = min(dp[i // 2], dp[i-1]) + 1

    return reconstruir_solucion(dp, k)


def reconstruir_solucion(dp, k):
    sol = []
    i = k
    while i > 0: 
        if i % 2 == 0 and dp[i] == dp[i // 2] + 1:
            sol.append('por2')
            i //= 2
        else:
            sol.append('mas1')
            i -= 1
    
    return sol[::-1]  