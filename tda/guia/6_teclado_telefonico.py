"""
forma de los subprobemas:
cantidad de combinaciones posibles , conociendo la cantidad de pasos y el numero por el que comienza

combinacion de subproblemas:
sabemos que si digito un numero estoy dando nu paso, para considrar todas las combinaciones 
teniendo un paso menos hay que referirnos a la solucion con un paso menos para todos los numeros conectados.

C[pasos=i][desde=v] = Sumatoria para todos los vecinos w de v de C[pasos=i-1][desde=w] 
"""
from tda.graph.grafo import Grafo


def numeros_posibles(k, n):
    if n <= 1:
        return n

    grafo = crear_grafo_telefono()

    cantidades = [[0 for _ in range(10)] for _ in range(n+1)]

    for paso in range(n + 1):
        for tecla in range(10):
            if paso == 0:
                cantidades[paso][tecla] = 0
            elif paso == 1:
                cantidades[paso][tecla] = 1
            else:
                cantidades[paso][tecla] += cantidades[paso - 1][tecla]
                for numero_ady in grafo.adyacentes(tecla):
                    cantidades[paso][tecla] += cantidades[paso - 1][numero_ady]

    return cantidades[n][k]



def crear_grafo_telefono():
    grafo = Grafo()
    
    for tecla in range(10):
        grafo.agregar_vertice(tecla)
    
    grafo.agregar_arista(0, 8)
    grafo.agregar_arista(1, 2)
    grafo.agregar_arista(1, 4)
    grafo.agregar_arista(2, 3)
    grafo.agregar_arista(2, 5)
    grafo.agregar_arista(3, 6)
    grafo.agregar_arista(4, 5)
    grafo.agregar_arista(4, 7)
    grafo.agregar_arista(5, 6)
    grafo.agregar_arista(5, 8)
    grafo.agregar_arista(6, 9)
    grafo.agregar_arista(7, 8)
    grafo.agregar_arista(8, 9)
    
    return grafo
