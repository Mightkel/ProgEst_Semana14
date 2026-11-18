def busqueda_lineal(lista, objetivo):
    for i in range(len(lista)):
        if lista[i] == objetivo:
            return i          # encontrado: devuelve la posición
    return -1                 # no encontrado

datos = [7, 2, 9, 4, 1]
print(busqueda_lineal(datos, 4))   # 3
print(busqueda_lineal(datos, 8))   # -1