# Ejercicio
# Una inmobiliaria de una ciudad maneja una lista de inmuebles como la siguiente:
# `[{'año': 2000, 'metros': 100, 'habitaciones': 3, 'garaje': True, 'zona': 'A'},
# {'año': 2012, 'metros': 60, 'habitaciones': 2, 'garaje': True, 'zona': 'B'},
# {'año': 1980, 'metros': 120, 'habitaciones': 4, 'garaje': False, 'zona': 'A'},
# {'año': 2005, 'metros': 75, 'habitaciones': 3, 'garaje': True, 'zona': 'B'},
# {'año': 2015, 'metros': 90, 'habitaciones': 2, 'garaje': False, 'zona': 'A'}]`
# Construir una función que permita hacer búsqueda de inmuebles en función de un presupuesto dado. La función recibirá como 
# entrada la lista de inmuebles y un precio, y devolverá otra lista con los inmuebles cuyo precio sea menor o igual que el dado. 
# Los inmuebles de la lista que se devuelva deben incorporar un nuevo par a cada diccionario con el precio del inmueble, donde 
# el precio de un inmueble se calcula con las siguiente fórmula en función de la zona:
# - Zona A: precio = (metros x 1000 + habitaciones x 5000 + garaje x 15000) x (1 - antiguedad / 100)
# - Zona B: precio = (metros x 1000 + habitaciones x 5000 + garaje x 15000) x (1 - antiguedad / 100) x 1.5
AÑO_ACTUAL = 2024

def calcular_precio(inmueble):
    antiguedad = AÑO_ACTUAL - inmueble["año"]
    base = (
        inmueble["metros"] * 1000 +
        inmueble["habitaciones"] * 5000 +
        inmueble["garaje"] * 15000
    ) * (1 - antiguedad / 100)
    return base * 1.5 if inmueble["zona"] == "B" else base

def filtro_inmuebles_precio_menor_igual(lista, precio):
    lista_con_precio = list(map(
        lambda i: {**i, "precio": round(calcular_precio(i), 2)},
        lista
    ))
    return list(filter(
        lambda i: i["precio"] <= precio,
        lista_con_precio
    ))


lista_inmuebles = [
    {'año': 2000, 'metros': 100, 'habitaciones': 3, 'garaje': True,  'zona': 'A'},
    {'año': 2012, 'metros': 60,  'habitaciones': 2, 'garaje': True,  'zona': 'B'},
    {'año': 1980, 'metros': 120, 'habitaciones': 4, 'garaje': False, 'zona': 'A'},
    {'año': 2005, 'metros': 75,  'habitaciones': 3, 'garaje': True,  'zona': 'B'},
    {'año': 2015, 'metros': 90,  'habitaciones': 2, 'garaje': False, 'zona': 'A'},
]

for inmueble in filtro_inmuebles_precio_menor_igual(lista_inmuebles, 150000):
    print(inmueble)