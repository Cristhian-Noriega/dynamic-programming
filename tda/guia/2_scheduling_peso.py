"""
Ec de recurrencia:
Debo elegir entre no dar la charla i (opt[i-1]) o darla (opt[p[i-1]] + charlas[i-1][2])
opt[i] = max(opt[i-1], opt[p[i-1]] + charlas[i-1][2])
"""


def scheduling(charlas):
    charlas.sort(key=lambda x: x[1]) 
    n = len(charlas)
    p = obtener_rangos(charlas)
    dp = [0] * (n + 1)
    
    for i in range(1, n + 1):
        dp[i] = max(dp[i-1], dp[p[i-1]] + charlas[i-1][2])
    
    return reconstruir_solucion(dp, charlas, p)


def obtener_rangos(charlas):
    n = len(charlas)
    p = [0] * n
    for i in range(n):
        p[i] = busqueda_binaria(charlas, 0, i - 1, charlas[i][0])
    return p


def busqueda_binaria(arr, ini, fin, h_ini):
    if fin < ini:
        return 0  
    med = (ini + fin) // 2
    if arr[med][1] <= h_ini:
        res = busqueda_binaria(arr, med + 1, fin, h_ini)
        return res if res != 0 else med + 1 
    else:
        return busqueda_binaria(arr, ini, med - 1, h_ini)


def reconstruir_solucion(dp, charlas, p):
    n = len(dp) - 1
    seleccionadas = []
    while n > 0:
        if dp[n] != dp[n - 1]:
            seleccionadas.append(charlas[n - 1])
            n = p[n - 1]
        else:
            n -= 1
    return seleccionadas[::-1]


charlas = [
    (1, 6, 2),  # Start: 1, End: 6, Weight: 2
    (7, 11, 4), # Start: 7, End: 11, Weight: 4
    (3, 14, 7), # Start: 3, End: 14, Weight: 7
    (11, 16, 2) # Start: 11, End: 16, Weight: 2
]

result = scheduling(charlas)
print("Selected charlas:", result)