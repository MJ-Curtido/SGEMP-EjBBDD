from sqlite3 import *
import os

def onCreate():
    try:
        os.remove('Empleados.db')
    except:
        print("No hay bbdd")

    try:
        bbdd = connect("Empleados.db")
        cursor = bbdd.cursor()
        tablas = [
            """
                CREATE TABLE IF NOT EXISTS "empleado" (
                    "cod"	INTEGER,
                    "nombre"   TEXT NOT NULL,
                    "apellido"	TEXT NOT NULL,
                    "sueldoBase"	INTEGER NOT NULL,
                    "afap"	INTEGER NOT NULL,
                    "fechaIngreso"	TEXT NOT NULL,
                    "cantidadNinyos"    INTEGER NOT NULL,
                    PRIMARY KEY("cod" AUTOINCREMENT)
                )
            """
        ]
        for tabla in tablas:
            cursor.execute(tabla)

        empleados = [
            """
                INSERT INTO empleado (
                    nombre,
                    apellido,
                    sueldoBase,
                    afap,
                    fechaIngreso,
                    cantidadNinyos
                )
                VALUES
                    ("Nombre1", "Apellido1", 1111, 0, "Fecha1", 1),
                    ("Nombre2", "Apellido2", 2222, 1, "Fecha2", 2),
                    ("Nombre3", "Apellido3", 3333, 0, "Fecha3", 3),
                    ("Nombre4", "Apellido4", 4444, 1, "Fecha4", 4),
                    ("Nombre5", "Apellido5", 5555, 0, "Fecha5", 5),
                    ("Nombre6", "Apellido6", 6666, 1, "Fecha6", 6),
                    ("Nombre7", "Apellido7", 7777, 0, "Fecha7", 7),
                    ("Nombre8", "Apellido8", 8888, 1, "Fecha8", 8),
                    ("Nombre9", "Apellido9", 9999, 0, "Fecha9", 9),
                    ("Nombre10", "Apellido10", 1010, 1, "Fecha10", 10)
                ;
            """
        ]
        for empleado in empleados:
            cursor.execute(empleado)

        bbdd.commit()
        print("bbdd creada correctamente")
    except Exception as error:
        print("Error al crear la bbdd: ", error)
    finally:
        cursor.close()

def insertarEmpleado():
    try:
        bbdd = connect("../Ejercicio2/Empresa.db")
        cursor = bbdd.cursor()

        nombre = input("\nNombre:")
        apellido = input("\nApellido:")
        sueldoBase = input("\nSueldo Base:")
        afapPreg = input("\nAFAP (s/n):")
        if afapPreg.__eq__("s"):
            afap = 1
        else:
            afap = 0
        fechaIngreso = input("\nFecha ingreso:")
        cantidadNinyos = input("\nCantidad de niños:")

        cursor.execute("INSERT INTO empleado (nombre, apellido, sueldoBase, afap, fechaIngreso, cantidadNinyos) VALUES (?, ?, ?, ?, 1)", [nombre, apellido, sueldoBase, afap, fechaIngreso, cantidadNinyos])

        bbdd.commit()

        print("Empleado insertado correctamente")
    except Exception as error:
        print("Error al insertar el empleado:", error)
    finally:
        cursor.close()

def mostrarEmpleados():
    try:
        bbdd = connect("Empleados.db")
        cursor = bbdd.cursor()

        cursor.execute("SELECT * FROM empleado;")
        empleados = cursor.fetchall()

        for cod, nombre, apellido, sueldoBase, afap, fechaIngreso, cantidadNinyos in empleados:
            print(cod, " - ", nombre, " - ", apellido, " - ", sueldoBase, " - ", afap, " - ", fechaIngreso, " - ", cantidadNinyos)
    except Exception as error:
        print("Error al mostrar los empleados:", error)
    finally:
        cursor.close()