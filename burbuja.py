
## Version Básica

def burbuja(lista):
    n = len(lista)
    for i in range(n - 1):              # número de pasadas
        for j in range(n - 1 - i):      # los últimos i ya están ordenados
            if lista[j] > lista[j + 1]:
                # intercambio al estilo Python
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista

numeros = [5, 3, 8, 4, 2]
print(burbuja(numeros))   # [2, 3, 4, 5, 8]

## Version Optimizada

def burbuja_optimizada(lista):
    n = len(lista)
    for i in range(n - 1):
        hubo_intercambio = False
        for j in range(n - 1 - i):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                hubo_intercambio = True
        if not hubo_intercambio:   # si no se movió nada, ya está ordenada
            break
    return lista

print(burbuja_optimizada([1, 2, 3, 4, 5]))  # termina tras 1 sola pasada → O(n)

## Con Contadores

def burbuja_analisis(lista):
    comparaciones = 0
    intercambios = 0
    n = len(lista)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            comparaciones += 1
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                intercambios += 1
    print("Comparaciones:", comparaciones)
    print("Intercambios:", intercambios)
    return lista

burbuja_analisis([5, 3, 8, 4, 2])
# Comparaciones: 10
# Intercambios: 7

## Practica

def burbuja_analisis(lista):
    comparaciones = 0
    intercambios = 0
    n = len(lista)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            comparaciones += 1
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                intercambios += 1
    print("Comparaciones:", comparaciones)
    print("Intercambios:", intercambios)
    return lista

'''
Resultado esperado: (Escrito en cuaderno)
97 - 79
95 - 59
93 - 39
91 - 19

75319

75 - 57
73 - 37
71 - 17

53179

53 - 35
51 - 15

31579

31 - 13

13579
'''
burbuja_analisis([9, 7, 5, 3, 1])