# Tome esta lista:
# edades = [12, 17, 18, 20, 15, 30, 22]
# Use filter() para quedarse solo con los mayores de edad.
# Use map() para sumar uno acada edad 


edades = [12, 17, 18, 20, 15, 30, 22]
lista_filtrada = list(filter(lambda edad: edad >= 18, edades))
lista_sumada = list(map(lambda x: x+1, edades))
print(lista_filtrada)
print(lista_sumada)