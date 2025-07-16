"""
Osvaldo es un empleado de una inescrupulosa empresa inmobiliaria, y está buscando un ascenso.
Está viendo cómo se predice que evolucionará el precio de un inmueble (el cual no poseen,
pero pueden comprar). Tiene la información de estas predicciones en el arreglo p, para todo
día i = 1, 2, ..., n. Osvaldo quiere determinar un día j en el cuál comprar la casa,
y un día k en el cual venderla (k > j), suponiendo que eso sucederá sin lugar a dudas.
El objetivo, por supuesto, es la de maximizar la ganancia dada por p[k] - p[j].
Implementar un algoritmo de programación dinámica que permita resolver el problema de Osvaldo.
"""



def compra_venta(p):
    n = len(p)
    opt = [0] * n
    min_price = [0] * n
    min_price[0] = p[0]
    for i in range(1, n):
        min_price[i] = min(min_price[i-1], p[i])
        opt[i] = max(opt[i-1], p[i] - min_price[i])
    
    return reconstruir_solucion(p, opt, min_price, n)


def reconstruir_solucion(p, opt, min_price, n):
    max_profit = opt[n-1]
    venta = n - 1
    
    while venta > 0 and opt[venta-1] == max_profit:
        venta -= 1
    
    compra = min_price.index(p[venta] - max_profit)
    
    return compra, venta