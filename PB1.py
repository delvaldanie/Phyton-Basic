# Crea un programa que haga lo siguiente:
# 1. Define una función agregar_alumno(diccionario, nombre, notas) que reciba un diccionario, un nombre (string) y 
# una lista de notas (números), y añada al alumno al diccionario.

# 2. Define una función promedio(notas) que reciba una lista de notas y devuelva el promedio.

# 3. Define una función mostrar_resultados(diccionario) que recorra todos los alumnos e imprima su nombre y si ha aprobado 
# (promedio ≥ 5) o suspendido.

def agregar_alumno(nombre, notas, n):
    alumno_notas[f"nombre{n}"] = nombre
    alumno_notas[f"notas{n}"] = notas

def promedio(notas):
    suma = 0
    for j in range(len(notas)):
        suma = suma + notas[j]
    return suma / len(notas)

def mostrar_resultados(total):
    for i in range(1, total + 1):
        nota_promedio = promedio(alumno_notas[f"notas{i}"])
        nombre = alumno_notas[f"nombre{i}"]
        if nota_promedio >= 5:
            print(f"{nombre} - Promedio: {nota_promedio:.1f} → Aprobado ✓")
        else:
            print(f"{nombre} - Promedio: {nota_promedio:.1f} → Suspendido ✗")

n = 1
alumno_notas = {}
Ana_notas = [4, 8, 6, 9, 4, 7, 5, 8]
Luis_notas = [5, 8, 6, 9, 4, 1, 7, 8]
Marta_notas = [3, 8, 6, 7, 4, 9, 5, 8]
agregar_alumno("Ana", Ana_notas, n)
n += 1
agregar_alumno("Luis", Luis_notas, n)
n += 1
agregar_alumno("Marta", Marta_notas, n)
mostrar_resultados(3)