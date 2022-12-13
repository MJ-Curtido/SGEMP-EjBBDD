from sqlite3 import *
from ConexionDB import *

onCreate()

cont = 0

while cont < 3:
    eliminarEmpleado()
    cont += 1

cont = 0

while cont < 8:
    insertarEmpleado()
    cont += 1