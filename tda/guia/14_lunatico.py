"""
Puedo dividir el problema en dos, paso de un problema circular a uno lineal.
Considero una solucion parecida al de juan el vago, en donde tengos dos opciones:
- considerar la casa actual i, por lo que la anterior no la puedo robar y obtengo la ganacia de i
- no considera la casa actual i, por lo que considero el optimo del subpoblema anterior

Me queda la ecuacion de recurrencia:
opt_lineal[i] = max(opt_lineal[i-2] + gi, opt_lineal[i-1])
opt_circular[i] = max(opt_lineal_(0, n-1), opt_lineal(1, n))
"""


def lunatico(ganancias):
    n = len(ganancias)
    if n == 0:
        return 0, []
    if n == 1:
        return ganancias[0], [0]
    ganancias_sin_n, casas_sin_n = lunatico_lineal(ganancias, 0, n - 2)
    ganancias_con_0, casas_sin_0 = lunatico_lineal(ganancias, 1, n - 1)
    if ganancias_sin_n[-1] > ganancias_con_0[-1]:
        return casas_sin_n
    else:
        return casas_sin_0



def lunatico_lineal(ganancias, ini, fin):
    dp = [0] * (fin - ini + 1)
    dp[0] = ganancias[ini]
    dp[1] = max(ganancias[ini], ganancias[ini + 1])

    for i in range(2, len(dp)):
        dp[i] = max(dp[i - 2] + ganancias[ini + i], dp[i - 1])

    return dp, reconstruir_casas(dp, ini, fin)


def reconstruir_casas(dp, ini, fin):
    casas = []
    i = len(dp) - 1
    while i >= 0:
        if i == 0 or dp[i] != dp[i-1]:
            casas.append(ini + i)  
            i -= 2  
        else:
            i -= 1   
    return casas[::-1] 





print(lunatico([1, 2, 3, 4, 5]))  