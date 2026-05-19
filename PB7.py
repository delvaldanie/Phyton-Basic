# Ejercicio 
# Escribir una función que reciba una muestra de números en una lista y devuelva otra lista con sus cuadrados.

def mostrar_cuadrados(numeros):
    lista = numeros
    lista_cuadrados = []
    for i in range(len(lista)):
        lista_cuadrados.append(lista[i] * lista[i])
    return lista_cuadrados

lista_cuadrados = mostrar_cuadrados([1, 2, 3, 4, 5])
print(lista_cuadrados)  # [1, 4, 9, 16, 25]

