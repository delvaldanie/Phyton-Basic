def agregar_alumno(nombre, notas):
    alumno_notas["nombre${n}"] = "${nombre}"
    alumno_notas["notas${n}"] = "${notas}"
    n+=1
            
def promedio (nombre):
    promedio = 0
    for i in range(len(alumno_notas)%2):
        if alumno_notas["nombre${i}"] == nombre:
            notas = alumno_notas["notas${i}"]
            for j in range(len(notas)):
                promedio = promedio + notas[j]
        exit()
    print


n = 1
alumno_notas = {}
Ana_notas = [4,8,6,9,4,7,5,8]
Luis_notas = [5,8,6,9,4,1,7,8]
Marta_notas = [3,8,6,7,4,9,5,8]
agregar_alumno("Ana", Ana_notas)
agregar_alumno("Luis", Luis_notas)
agregar_alumno("Marta", Marta_notas)