from sqlite3 import *
from ConexionDB import *

onCreate()

respuesta = "s"

while respuesta.__eq__("s"):
    opcion = input("1. Insertar alumno\n2. Eliminar alumno\n3. Insertar profesor\n4. Eliminar profesor")

    match opcion:
        case 1:
            insertarAlumno()
        case 2:
            eliminarAlumno()
        case 3:
            insertarProfesor()
        case 4:
            eliminarProfesor()
        case _:
            print("Respuesta no válida")

    respuesta = input("¿Desea continuar? (s/n)")