from sqlite3 import *

def onCreate():
    try:
        bbdd = connect("Instituto.db")
        cursor = bbdd.cursor()
        tablas = [
            """
            CREATE TABLE "profesor" (
                "id"	INTEGER,
                "nif"	TEXT NOT NULL UNIQUE,
                "nombre"	TEXT NOT NULL,
                "especialidad"	TEXT NOT NULL,
                "telefono"	INTEGER NOT NULL UNIQUE,
                PRIMARY KEY("id" AUTOINCREMENT)
            )
            """,
            """
                CREATE TABLE "alumno" (
                    "numMatricula"	INTEGER,
                    "nombre"	TEXT NOT NULL,
                    "fechaNac"	TEXT NOT NULL,
                    "telefono"	INTEGER NOT NULL,
                    PRIMARY KEY("numMatricula" AUTOINCREMENT)
                )
            """,
            """
                CREATE TABLE "asignatura" (
                    "cod"	INTEGER,
                    "nombre"	TEXT NOT NULL,
                    "codProfesor"	INTEGER NOT NULL,
                    PRIMARY KEY("cod" AUTOINCREMENT),
                    FOREIGN KEY("codProfesor") REFERENCES "profesor"("id")
                )
            """,
            """
                CREATE TABLE "curso_escolar" (
                    "codAlumno"	INTEGER,
                    "codAsignatura"	INTEGER,
                    PRIMARY KEY("codAlumno","codAsignatura"),
                    FOREIGN KEY("codAlumno") REFERENCES "alumno"("numMatricula"),
                    FOREIGN KEY("codAsignatura") REFERENCES "asignatura"("cod")
                )
            """
        ]
        for tabla in tablas:
            cursor.execute(tabla)

        profesores = [
            """
                INSERT INTO profesor (
                    nif,
                    nombre,
                    especialidad,
                    telefono
                )
                VALUES
                ("11111111P", "Persona1", "especialidad1", 111111111)
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
                ("Nombre1", "1-1-2001"),
                ("Nombre2", "2-2-2002"),
                ("Nombre3", "3-3-2003"),
                ("Nombre4", "4-4-2004"),
                ("Nombre5", "5-5-2005"),
                ("Nombre6", "6-6-2006"),
                ("Nombre7", "7-7-2007"),
                ("Nombre8", "8-8-2008"),
                ("Nombre9", "9-9-2009"),
                ("Nombre10", "10-10-2010")
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
    except OperationalError as error:
        print("Error al crear la bbdd: ", error)
    finally:
        cursor.close()

def numAlumnos():
    bbdd = connect("Instituto.db")
    cursor = bbdd.cursor()

    cursor.execute("SELECT COUNT(numMatricula) FROM alumno;")
    return cursor.fetchall()[0]

def insertarAlumno():
    if numAlumnos() <= 25:
        try:
            bbdd = connect("Instituto.db")
            cursor = bbdd.cursor()

            nombre = input("\nNombre:")
            fechaNac = input("\nFecha de nacimiento:")
            telefono = input("\nTeléfono:")

            cursor.execute("INSERT INTO alumno (nombre, fechaNac, telefono) VALUES (?, ?, ?)", [nombre, fechaNac, telefono])

            bbdd.commit()

            print("Alumno insertado correctamente")
        except OperationalError as error:
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
        except OperationalError as error:
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
    except OperationalError as error:
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
    except OperationalError as error:
        print("Ha ocurrido un fallo al eliminar el profesor: ", error)
    finally:
        cursor.close()