# Ejercicio 
# Los tramos impositivos para la declaración de la renta en un determinado país son los siguientes:

# |         Renta          | Tipo impositivo |
#| :--------------------: | :-------------: |
#|    Menos de 10000€     |       5%        |
#| Entre 10000€ y 20000€  |       15%       |
#| Entre 20000€ y 35000€  |       20%       |
#| Entre 35000€ y 60000€  |       30%       |
#|     Más de 60000€      |       45%       |
# Escribir un programa que pregunte al usuario su renta anual y muestre por pantalla lo que tiene que pagar.




renta = float(input("Cual es tu renta "))
if renta < 10000:
    inpuesto = renta * 0.05
    print(f"Inpuestos a pagar {inpuesto}")
elif renta >= 10000 and renta <= 20000:
    inpuesto = renta * 0.15
    print(f"Inpuestos a pagar {inpuesto}")

elif renta >= 20000 and renta <= 35000:
    inpuesto = renta * 0.2
    print(f"Inpuestos a pagar {inpuesto}")

elif renta >= 35000 and renta <= 60000:
    inpuesto = renta * 0.3
    print(f"Inpuestos a pagar {inpuesto}")

elif renta > 60000:
    inpuesto = renta * 0.45
    print(f"Inpuestos a pagar {inpuesto}")