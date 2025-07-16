"""
Dada una soga de n metros (n mayor o igual a 2) implementar un algoritmo que, utilizando programación dinámica, permita cortarla (en partes de largo entero) de manera tal que el producto del largo de cada una de las partes resultantes sea máximo. El algoritmo debe devolver el valor del producto máximo alcanzable. Tener en cuenta que la soga puede cortarse varias veces, como se muestra en el ejemplo con n = 10. Indicar y justificar la complejidad del algoritmo.

Ejemplos:

n = 2 --> Debe devolver 1 (producto máximo es 1 * 1)
n = 3 --> Debe devolver 2 (producto máximo es 2 * 1)
n = 4 --> Debe devolver 4 (producto máximo es 2 * 2)
n = 5 --> Debe devolver 6 (producto máximo es 2 * 3)
n = 6 --> Debe devolver 9 (producto máximo es 3 * 3)
n = 7 --> Debe devolver 12 (producto máximo es 3 * 4)
n = 10 --> Debe devolver 36 (producto máximo es 3 * 3 * 4)
"""


def problema_soga(n):
    maximo_producto = [0] * (n + 1)
    for i in range(2, n + 1):
        max_valor = 0
        for j in range(1, i):
            max_valor = max(max_valor, j * maximo_producto[i - j], j * (i - j))
        maximo_producto[i] = max_valor

    return maximo_producto[n]