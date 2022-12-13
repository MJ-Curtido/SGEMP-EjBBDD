from sqlite3 import *
import os

def onCreate():
    try:
        os.remove('Empresa.db')
    except:
        print("No hay bbdd")

    try:
        bbdd = connect("Empresa.db")
        cursor = bbdd.cursor()
        tablas = [
            """
                CREATE TABLE IF NOT EXISTS "region" (
                    "cod"	INTEGER,
                    "nombre"	TEXT NOT NULL,
                    PRIMARY KEY("cod" AUTOINCREMENT)
                )
            """,
            """
                CREATE TABLE IF NOT EXISTS "provincia" (
                    "cod"	INTEGER,
                    "nombre"	TEXT NOT NULL,
                    "codRegion"	INTEGER NOT NULL,
                    PRIMARY KEY("cod" AUTOINCREMENT),
                    FOREIGN KEY("codRegion") REFERENCES "region"("cod")
                )
            """,
            """
                CREATE TABLE IF NOT EXISTS "localidad" (
                    "cod"	INTEGER,
                    "nombre"	TEXT NOT NULL,
                    "codProvincia"	INTEGER NOT NULL,
                    PRIMARY KEY("cod" AUTOINCREMENT),
                    FOREIGN KEY("codProvincia") REFERENCES "provincia"("cod")
                )
            """,
            """
                CREATE TABLE IF NOT EXISTS "empleado" (
                    "cod"	INTEGER,
                    "dni"   TEXT NOT NULL UNIQUE,
                    "nombre"	TEXT NOT NULL,
                    "telefono"	INTEGER NOT NULL UNIQUE,
                    "salario"	INTEGER NOT NULL,
                    "codLocalidad"	INTEGER,
                    PRIMARY KEY("cod" AUTOINCREMENT),
                    FOREIGN KEY("codLocalidad") REFERENCES "localidad"("cod")
                )
            """
        ]
        for tabla in tablas:
            cursor.execute(tabla)

        regiones = [
            """
                INSERT INTO region (
                    nombre
                )
                VALUES
                ("Region1")
                ;
            """
        ]
        for region in regiones:
            cursor.execute(region)

        provincias = [
            """
                INSERT INTO provincia (
                    nombre,
                    codRegion
                )
                VALUES
                ("Provincia1", 1)
                ;
            """
        ]
        for provincia in provincias:
            cursor.execute(provincia)

        localidades = [
            """
                INSERT INTO localidad (
                    nombre,
                    codProvincia
                )
                VALUES
                ("Localidad1", 1)
                ;
            """
        ]
        for localidad in localidades:
            cursor.execute(localidad)

        empleados = [
            """
                INSERT INTO empleado (
                    dni,
                    nombre,
                    telefono,
                    salario,
                    codLocalidad
                )
                VALUES
                ("11111111P", "Nombre1", 111111111, 1, 1),
                ("22222222P", "Nombre2", 222222222, 2, 2),
                ("33333333P", "Nombre3", 333333333, 3, 3),
                ("44444444P", "Nombre4", 444444444, 4, 4),
                ("55555555P", "Nombre5", 555555555, 5, 5),
                ("66666666P", "Nombre6", 666666666, 6, 6),
                ("77777777P", "Nombre7", 777777777, 7, 7),
                ("88888888P", "Nombre8", 888888888, 8, 8),
                ("99999999P", "Nombre9", 999999999, 9, 9),
                ("10101010P", "Nombre10", 101010101, 10, 10)
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
        bbdd = connect("Empresa.db")
        cursor = bbdd.cursor()

        dni = input("\nDNI:")
        nombre = input("\nNombre:")
        telefono = input("\nTeléfono:")
        salario = input("\nSalario:")

        cursor.execute("INSERT INTO empleado (dni, nombre, telefono, salario, codLocalidad) VALUES (?, ?, ?, ?, 1)", [dni, nombre, telefono, salario])

        bbdd.commit()

        print("Empleado insertado correctamente")
    except Exception as error:
        print("Error al insertar el empleado:", error)
    finally:
        cursor.close()

def eliminarEmpleado():
    try:
        bbdd = connect("Empresa.db")
        cursor = bbdd.cursor()

        cursor.execute("SELECT * FROM empleado;")
        empleados = cursor.fetchall()

        for cod, dni, nombre, telefono, salario, codLocalidad in empleados:
            print(cod, " - ", dni, " - ", nombre, " - ", telefono, " - ", salario, " - ", codLocalidad)

        codEmpleado = input("\n\nCódigo del empleado a eliminar: ")

        cursor.execute("DELETE FROM empleado WHERE cod = ?", [codEmpleado])

        bbdd.commit()

        print("Alumno eliminado correctamente")
    except Exception as error:
        print("Ha ocurrido un fallo al eliminar el alumno: ", error)
    finally:
        cursor.close()