"""


"""


def cambio(monedas, monto):
    dp = [float('inf')] * (monto + 1)
    dp[0] = 0
    for i in range(1, monto + 1):
        for moneda in monedas:
            if moneda > i:
                continue
            dp[i] = min(dp[i], dp[i-moneda] + 1)
    
    return reconstruir(dp, monedas, monto)

def reconstruir(dp, monedas, monto):
    j = monto
    res = []
    while j > 0:
        for moneda in monedas:
            if moneda <= j and dp[j] == dp[j-moneda] + 1:
                res.append(moneda)
                j -= moneda
                break

    return res