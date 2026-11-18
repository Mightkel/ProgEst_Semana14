def busqueda_binaria(lista, objetivo):
    izq, der = 0, len(lista) - 1
    while izq <= der:
        medio = (izq + der) // 2
        if lista[medio] == objetivo:
            return medio
        elif lista[medio] < objetivo:
            izq = medio + 1   # buscar a la derecha
        else:
            der = medio - 1   # buscar a la izquierda
    return -1

datos = [1, 3, 5, 7, 9, 11, 13]
print(busqueda_binaria(datos, 11))  # 5