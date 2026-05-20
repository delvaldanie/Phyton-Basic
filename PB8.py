# Ejercicio 
# Escribir una función que reciba una muestra de números en una lista y devuelva un diccionario con su media, varianza y desviación típica.
import math

def crear_lista(numeros_lista):
    lista = numeros_lista
    
    return lista

def crear_diccionario(lista):
    suma = 0
    suma_cuadrada = 0
    desviaciones_cuadrado = 0
    for i in range(len(lista)):
        suma = suma + lista[i]
        suma_cuadrada = suma_cuadrada + (lista[i]*lista[i])
        
    media = suma / len(lista)
    varianza = (suma_cuadrada/len(lista)) - (media*media)
    
    for i in range(len(lista)):
        desviaciones_cuadrado = desviaciones_cuadrado + ((lista[i]-media)*(lista[i]-media))
    varianza_muestral = desviaciones_cuadrado / (len(lista)-1)
    desviacion_tipica =  math.sqrt(varianza_muestral)

    return {"media": media, "varianza": varianza, "desviacion tipica": desviacion_tipica}

print(crear_diccionario(crear_lista([1,2,3,4,5,6])))
