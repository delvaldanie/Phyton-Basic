# Escribir un programa que reciba una cadena de caracteres y devuelva un diccionario con cada palabra que contiene y su frecuencia. 
# Escribir otra función que reciba el diccionario generado con la función anterior y devuelva una tupla con la palabra más repetida 
# y su frecuencia.

def crear_diccionario(cadena):
    lista = cadena.split()
    diccionario = {}
    for i in range(len(lista)):
        if diccionario.get(lista[i]):
            diccionario[lista[i]] += 1
        else:
            diccionario[lista[i]] = 1
    return diccionario

def crear_tulpa(diccionario):
    lista = []
    for clave in diccionario:
        if diccionario[clave] >= 2:
            lista.append(f"{clave}: {diccionario[clave]}")
    tupla = (lista)
    return tupla

diccionario = crear_diccionario("Lorem Ipsum es simplemente texto ficticio de la industria de la impresión y la composición tipográfica. Lorem Ipsum ha sido el texto ficticio estándar de la industria desde el siglo XVI, cuando un impresor desconocido tomó una galera de tipos y la codificó para hacer un libro de muestras tipográficas. Ha sobrevivido no sólo cinco siglos, sino también el salto a la composición tipográfica electrónica, permaneciendo esencialmente sin cambios. Se popularizó en la década de 1960 con el lanzamiento de hojas Letraset que contenían pasajes de Lorem Ipsum y, más recientemente, con software de autoedición como Aldus PageMaker que incluía versiones de Lorem Ipsum.")
print(crear_tulpa(diccionario))