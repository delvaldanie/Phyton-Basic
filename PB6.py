# Ejercicio 
# Escribir una función que calcule el área de un círculo y otra que calcule el volumen de un cilindro usando la primera función.


def area_circulo(radio):
    area = 3.14 * radio * radio
    return area

def volumen_cilindro(radio_cilindro, altura):
    volumen = 3.14 * radio_cilindro * radio_cilindro *altura
    return volumen

radio = 4
print(f"El area del circulo de radio {radio} es {area_circulo(radio)}")
radio_cilindro = 5
altura = 10
print(f"El volumen del cilindro de radio {radio} y alura {altura} es {volumen_cilindro(radio_cilindro, altura)}")