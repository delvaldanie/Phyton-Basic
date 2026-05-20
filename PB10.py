# Tome esta lista:
# edades = [12, 17, 18, 20, 15, 30, 22]
# Use filter() para quedarse solo con los mayores de edad.
# Use map() para sumar uno acada edad 
def filtrar_adulto(edad):
    if edad >= 18:
        return edad

edades = [12, 17, 18, 20, 15, 30, 22]
lista_filtrada = list(filter(filtrar_adulto, edades))
lista_sumada = list(map(lambda x: x+1, edades))
print(lista_filtrada)
print(lista_sumada)