contraseña_usuario = "AeIou123"
contraseña = input("Pasema la contraseña ")
print(contraseña_usuario.lower())
print(contraseña.lower())
if contraseña_usuario.lower() == contraseña.lower():
    print("Contraseña correcta")
else:
    print("Contraseña incorrecta")