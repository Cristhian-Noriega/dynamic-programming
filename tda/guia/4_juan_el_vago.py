"""
Ec de recurrencia:
Debo elegir entre no trabajar el día i (opt[i-1]) o trabajar (opt[i-2] + trabajos[i-1])
opt[i] = max(opt[i-1], opt[i-2] + trabajos[i-1])
"""

def juan_el_vago(trabajos):
    n = len(trabajos)
    dp = [0] * n
    dp[0] = trabajos[0]
    dp[1] = max(trabajos[0], trabajos[1])

    for i in range(2, n):
        dp[i] = max(dp[i-1], dp[i-2] + trabajos[i])

    print(dp)
    
    solucion = reconstruir_solucion(dp, trabajos)
    return solucion


def reconstruir_solucion(dp, trabajos):
    sol = []
    i = len(dp) - 1
    while i >= 0:
        print("i:", i, "dp[i]:", dp[i])
        if i == 0 or dp[i] != dp[i-1]:
            sol.append(i)  
            i -= 2  
        else:
            i -= 1  
    return sol[::-1] 


trabajos = [1, 2, 5, 12, 7]  # Ejemplo de trabajos con sus ganancias
resultado = juan_el_vago(trabajos)
print(resultado)