def buscar_valor(matriz, valor):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == valor:
                return i, j  # Retorna la posición del valor encontrado
    return None  # Retorna None si el valor no se encuentra

# Definir una matriz 3x3
matriz = [
    [5, 8, 3],
    [4, 1, 7],
    [9, 6, 2]
]

# Valor a buscar
valor_buscado = int(input("Ingrese el valor a buscar en la matriz: "))

# Llamar a la función de búsqueda
posicion = buscar_valor(matriz, valor_buscado)

# Mostrar el resultado
if posicion:
    print(f"El valor {valor_buscado} se encontró en la posición {posicion} (fila {posicion[0]}, columna {posicion[1]})")
else:
    print(f"El valor {valor_buscado} no se encontró en la matriz.")
