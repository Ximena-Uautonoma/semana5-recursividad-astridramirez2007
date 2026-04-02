"""
Ejercicio 2:
Dado un número entero positivo N, retornar la suma de los primeros N números.

Debe implementar:
- suma_ciclo(n)
- suma_recursiva(n)
"""

def suma_ciclo(n):
    """
    Retorna la suma de los primeros n números usando un ciclo.
    """
    total=0
    for i in range(1, n+1):
        total+= i
    return total
print(suma_ciclo(4))



def suma_recursiva(n):
    """
    Retorna la suma de los primeros n números usando recursividad.
    """
    if n==1:
        return 1
    return n+ suma_recursiva(n-1)
print(suma_recursiva(4))


