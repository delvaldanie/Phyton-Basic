# Ejercicio
# Escribir un programa que almacene la cadena de caracteres `contraseña` en una variable, pregunte al usuario por la 
# contraseña hasta que introduzca la contraseña correcta.

contraseña_usuario = "AeIou123"
contraseña = input("Pasema la contraseña ")
while contraseña_usuario.lower() != contraseña.lower():
    print("Contraseña incorrecta")
    contraseña = input("Pasema la contraseña ")
print("Contraseña correcta")