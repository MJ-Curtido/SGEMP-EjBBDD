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
                    PRIMARY KEY("id" AUTOINCREMENT)
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

        profesores = [
            """
                INSERT INTO region (
                    nombre
                )
                VALUES
                ("11111111P")
                ;
            """
        ]
        for profe in profesores:
            cursor.execute(profe)

        asignaturas = [
            """
                INSERT INTO asignatura (
                    nombre,
                    codProfesor
                )
                VALUES
                ("Nombre1", 1)
                ;
            """
        ]
        for asig in asignaturas:
            cursor.execute(asig)

        alumnos = [
            """
                INSERT INTO alumno (
                    nombre,
                    fechaNac,
                    telefono
                )
                VALUES
                ("Nombre1", "1-1-2001", 111111111),
                ("Nombre2", "2-2-2002", 222222222),
                ("Nombre3", "3-3-2003", 333333333),
                ("Nombre4", "4-4-2004", 444444444),
                ("Nombre5", "5-5-2005", 555555555),
                ("Nombre6", "6-6-2006", 666666666),
                ("Nombre7", "7-7-2007", 777777777),
                ("Nombre8", "8-8-2008", 888888888),
                ("Nombre9", "9-9-2009", 999999999),
                ("Nombre10", "10-10-2010", 101010101)
                ;
            """
        ]
        for alumno in alumnos:
            cursor.execute(alumno)

        cursos = [
            """
                INSERT INTO curso_escolar (
                    codAlumno,
                    codAsignatura
                )
                VALUES
                    (1, 1),
                    (2, 1),
                    (3, 1),
                    (4, 1),
                    (5, 1),
                    (6, 1),
                    (7, 1),
                    (8, 1),
                    (9, 1),
                    (10, 1)
                ;
            """
        ]
        for curso in cursos:
            cursor.execute(curso)

        bbdd.commit()
        print("bbdd creada correctamente")
    except Exception as error:
        print("Error al crear la bbdd: ", error)
    finally:
        cursor.close()

def numAlumnos():
    bbdd = connect("Instituto.db")
    cursor = bbdd.cursor()

    cursor.execute("SELECT COUNT(numMatricula) FROM alumno;")
    bbdd.commit()
    return cursor.fetchone()[0]

def insertarAlumno():
    if numAlumnos() < 25:
        try:
            bbdd = connect("Instituto.db")
            cursor = bbdd.cursor()

            nombre = input("\nNombre:")
            fechaNac = input("\nFecha de nacimiento:")
            telefono = input("\nTeléfono:")

            cursor.execute("INSERT INTO alumno (nombre, fechaNac, telefono) VALUES (?, ?, ?)", [nombre, fechaNac, telefono])

            bbdd.commit()

            print("Alumno insertado correctamente")
        except Exception as error:
            print("Error al insertar el alumno:", error)
        finally:
            cursor.close()
    else:
        print("No puedes introducir un alumno porque superaría el límite de la clase")

def eliminarAlumno():
    if numAlumnos() > 10:
        try:
            bbdd = connect("Instituto.db")
            cursor = bbdd.cursor()

            cursor.execute("SELECT * FROM alumno;")
            alumnos = cursor.fetchall()

            for numMatricula, nombre, fechaNac, telefono in alumnos:
                print(numMatricula," - ", nombre, " - ", fechaNac, " - ", telefono)

            codAlumno = input("\n\nNúmero de matrícula del alumno a eliminar: ")

            cursor.execute("DELETE FROM alumno WHERE numMatricula = ?", [codAlumno])

            bbdd.commit()

            print("Alumno eliminado correctamente")
        except Exception as error:
            print("Ha ocurrido un fallo al eliminar el alumno: ", error)
        finally:
            cursor.close()
    else:
        print("No puedes eliminar un alumno porque superaría el límite de la clase")

def insertarProfesor():
    try:
        bbdd = connect("Instituto.db")
        cursor = bbdd.cursor()

        nif = input("\nNIF:")
        nombre = input("\nNombre:")
        especialidad = input("\nEspecialidad:")
        telefono = input("\nTeléfono:")

        cursor.execute("INSERT INTO profesor (nif, nombre, especialidad, telefono) VALUES (?, ?, ?, ?)", [nif, nombre, especialidad, telefono])

        bbdd.commit()

        print("Profesor insertado correctamente")
    except Exception as error:
        print("Error al insertar el profesor: ", error)
    finally:
        cursor.close()

def eliminarProfesor():
    try:
        bbdd = connect("Instituto.db")
        cursor = bbdd.cursor()

        cursor.execute("SELECT * FROM profesor;")
        profesores = cursor.fetchall()

        for id, nif, nombre, especialidad, telefono in profesores:
            print(id, " - ", nif, " - ", nombre, " - ", especialidad, " - ", telefono)

        codProfesor = input("\n\nNúmero de matrícula del profesor a eliminar: ")

        cursor.execute("DELETE FROM profesor WHERE id = ?", [codProfesor])

        bbdd.commit()

        print("Profesor eliminado correctamente")
    except Exception as error:
        print("Ha ocurrido un fallo al eliminar el profesor: ", error)
    finally:
        cursor.close()