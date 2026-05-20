# Ejercicio
# Escribir una función que reciba una frase y devuelva un diccionario con las palabras que contiene y su longitud. 

def crear_dicc(cadena):
    lista = cadena.split(" ")
    dicc = {}
    for i in range(len(lista)):
        longitud = len(lista[i])
        dicc[f"{lista[i]}"] = longitud
    return dicc

dicc = crear_dicc("Lorem Ipsum es simplemente texto ficticio de la industria de la impresión y la composición tipográfica. Lorem Ipsum ha sido el texto ficticio estándar de la industria desde el siglo XVI, cuando un impresor desconocido tomó una galera de tipos y la codificó para hacer un libro de muestras tipográficas. Ha sobrevivido no sólo cinco siglos, sino también el salto a la composición tipográfica electrónica, permaneciendo esencialmente sin cambios. Se popularizó en la década de 1960 con el lanzamiento de hojas Letraset que contenían pasajes de Lorem Ipsum y, más recientemente, con software de autoedición como Aldus PageMaker que incluía versiones de Lorem Ipsum.")
print(dicc)