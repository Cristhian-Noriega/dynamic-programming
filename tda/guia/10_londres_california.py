"""
Ec de recurrencia:
opt_l[n] = min(opt_l[n-1], M + opt_c[n-1]) + L[n]
opt_c[n] = min(opt_c[n-1], M + opt_l[n-1]) + C[n]
opt[n] = min(opt_l[n], opt_c[n])
"""

L = 'londres'
C = 'california'

def plan_operativo(arreglo_L, arreglo_C, M):
    n = len(arreglo_L)
    opt_l = [0] * (n + 1)
    opt_c = [0] * (n + 1)

    for i in range(1, n +1):
        opt_l[i] = min(opt_l[i-1], M + opt_c[i-1]) + arreglo_L[i-1]
        opt_c[i] = min(opt_c[i-1], M + opt_l[i-1]) + arreglo_C[i-1]

    return reconstruir_solucion(opt_l, opt_c, arreglo_L, arreglo_C, M)


def reconstruir_solucion(opt_l, opt_c, arreglo_L, arreglo_C, M):
    n = len(arreglo_L)
    sol = []
    i = n
    
    en_londres = opt_l[n] <= opt_c[n]
    
    while i > 0:
        if en_londres:
            
            if opt_l[i] == opt_l[i-1] + arreglo_L[i-1]:
                sol.append(L)
            else:
                
                sol.append(L)
                en_londres = False
        else:
       
            if opt_c[i] == opt_c[i-1] + arreglo_C[i-1]:
                sol.append(C)
            else:
                sol.append(C)
                en_londres = True
        i -= 1
    
    return sol[::-1] 