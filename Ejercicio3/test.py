from sqlite3 import *
from ConexionDB import *

onCreate()

cont = 0

while cont < 10:
    insertarEmpleado()
    cont += 1