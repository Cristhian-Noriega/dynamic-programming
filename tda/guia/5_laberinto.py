"""
Si estoy en (i,j), pude haber llegado desde (i-1,j) o (i,j-1)
casos base: 
- Si i == 0 o j == 0, entonces hay una sola forma de llegar a (i,j) que es moviéndome solo en una dirección.
- Si i == 0 y j == 1, entonces hay una sola forma de llegar a (0,1) que es moviéndome hacia la derecha.
- Si i == 1 y j == 0, entonces hay una sola forma de llegar a (1,0) que es moviéndome hacia abajo.

defino opt(i, j) como la cantidad de caminos posibles para llegar a (i,j)
opt(i, j) = opt(i-1, j) + opt(i, j-1)
"""


def laberinto(matriz):
    n, m = len(matriz), len(matriz[0])
    dp = [[0] * m for _ in range(n)]
    dp[0][0] = 1  
    for i in range(n):
        dp[i][0] = 1
    for j in range(m):
        dp[0][j] = 1
    for i in range(1, n):
        for j in range(1, m):
            dp[i][j] = dp[i-1][j] + dp[i][j-1]
    return dp[n-1][m-1] 


"""
Modificacion: Quiero recorrer el laberinto recolectando la mayor cantidad de valores posibles.
defino opt(i, j) como la el valor máximo que puedo recolectar al llegar a (i,j)
opt(i, j) = max(opt(i-1, j), opt(i, j-1)) + matriz[i][j]
"""

def laberinto_valores(matriz):
    n, m = len(matriz), len(matriz[0])
    dp = [[0] * m for _ in range(n)]
    dp[0][0] = matriz[0][0] 
    for i in range(1, n):
        dp[i][0] = dp[i-1][0] + matriz[i][0]
    
    for j in range(1, m):
        dp[0][j] = dp[0][j-1] + matriz[0][j]

    for i in range(2, n):
        for j in range(2, m):
            dp[i][j] = max(dp[i-1][j], dp[i][j-1]) + matriz[i][j]

    # printear la matriz en formato de tabla
    for fila in dp:
        print(" | ".join(f"{valor:3}" for valor in fila))
    print()

    # la mayor cantidad de dinero que puedo recolectar al llegar a la celda (n-1, m-1)
    print("Valor máximo:", dp[n-1][m-1])

    return reconstruir_solucion(dp)

def reconstruir_solucion(dp):
    n, m =len(dp), len(dp[0])
    camino = []
    i, j = n - 1, m - 1
    while i >= 0 and j >= 0:
        camino.append((i, j))
        if i == 0:
            j -= 1
        elif j == 0:
            i -= 1
        elif dp[i-1][j] > dp[i][j-1]:
            i -= 1
        else:
            j -= 1

    return camino[::-1]  



matriz = [
    [5, 3, 2, 1],
    [1, 2, 10, 2],
    [4, 3, 1, 7],
    [2, 1, 2, 3]
]
# printear la matriz en formato de tabla
for fila in matriz:
    print(" | ".join(f"{valor:3}" for valor in fila))
print()
resultado = laberinto_valores(matriz)
print("Camino con mayor valor:", resultado)