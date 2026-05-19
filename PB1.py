# Crea un programa que haga lo siguiente:
# 1. Define una función agregar_alumno(diccionario, nombre, notas) que reciba un diccionario, un nombre (string) y 
# una lista de notas (números), y añada al alumno al diccionario.

# 2. Define una función promedio(notas) que reciba una lista de notas y devuelva el promedio.

# 3. Define una función mostrar_resultados(diccionario) que recorra todos los alumnos e imprima su nombre y si ha aprobado 
# (promedio ≥ 5) o suspendido.

def agregar_alumno(nombre, notas):
    alumno_notas["nombre${n}"] = "${nombre}"
    alumno_notas["notas${n}"] = "${notas}"
    n += 1
            
def promedio (notas):
    promedio = 0
    for j in range(len(notas)):
        suma = suma + notas[j]
    promedio = suma % len(notas)
    return promedio

def mostrar_resultados():
    for i in range((len(alumno_notas)%2)):
        nota_promedio = promedio(alumno_notas["notas${i}"])
        print(f"{alumno_notas['nombre${i}']} tiene de promedio {promedio}")



n = 1
alumno_notas = {}
Ana_notas = [4,8,6,9,4,7,5,8]
Luis_notas = [5,8,6,9,4,1,7,8]
Marta_notas = [3,8,6,7,4,9,5,8]
agregar_alumno("Ana", Ana_notas)
agregar_alumno("Luis", Luis_notas)
agregar_alumno("Marta", Marta_notas)
mostrar_resultados()