def bubble_sort(fila):
    n = len(fila)
    for i in range(n):
        for j in range(0, n - i - 1):
            if fila[j] > fila[j + 1]:
                fila[j], fila[j + 1] = fila[j + 1], fila[j]  # Intercambio de valores
    return fila

# Definir una matriz 3x3
matriz = [
    [5, 8, 3],
    [4, 1, 7],
    [9, 6, 2]
]

# Mostrar la matriz original
print("Matriz original:")
for fila in matriz:
    print(fila)

# Seleccionar la fila a ordenar
fila_a_ordenar = int(input("Ingrese el número de fila a ordenar (0-2): "))

# Ordenar la fila seleccionada
matriz[fila_a_ordenar] = bubble_sort(matriz[fila_a_ordenar])

# Mostrar la matriz con la fila ordenada
print("\nMatriz con la fila ordenada:")
for fila in matriz:
    print(fila)
