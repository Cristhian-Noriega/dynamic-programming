def subset_sum(numeros, V):
    n = len(numeros)
    dp = [[0] * (V+1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for v in range(V + 1):
            num = numeros[i - 1]
            if i == 3 and v == 2:
                print(f"i: {i}, v: {v}, num: {num}")
            if num > v:
                dp[i][v] = dp[i - 1][v]
            else:
                dp[i][v] = max(dp[i - 1][v], dp[i - 1][v - num] + num)

    for i in range(n + 1):
        print(dp[i])
    
    return reconstruir_solucion(dp, numeros, V)


def reconstruir_solucion(dp, numeros, V):
    sol = []
    i, j = len(numeros), V
    while i > 0 and j > 0:
        num = numeros[i - 1]
        if num > j or dp[i][j] == dp[i - 1][j]:
            i -= 1
            continue
        sol.append(num)
        i -= 1
        j -= num

    return sol

nums = [2,3,7]
V = 5
subset_sum(nums, V)