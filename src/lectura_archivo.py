from os import path
from time import ctime, time

NOMBRE = "NOMBRE"
APELLIDO = "APELLIDO"
PADRON = "PADRON"

INDICE_PADRON = 0
INDICE_NOMBRE = 1
INDICE_APELLIDO = 2


def leer_informacion_alumnos(ruta: str) -> list[dict]:
    """
    PRE:
    POST: Devuelve una lista de diccionarios con la información de los alumnos. Devuelve una lista vacia si no existe el
    archivo.
    """
    alumnos = []
    if path.isfile(ruta):
        with open(ruta, "r") as archivo:
            while linea := archivo.readline():
                informacion = linea.rstrip().split(",")
                # ¿Como se podría validar que el formato sea correcto?
                # ¿Qué se podria hacer en caso de que un registro sea incorrecto?
                alumno = {PADRON: int(informacion[INDICE_PADRON]),
                          NOMBRE: informacion[INDICE_NOMBRE],
                          APELLIDO: informacion[INDICE_APELLIDO]}
                alumnos.append(alumno)
    return alumnos


def guardar_informacion_alumnos(alumnos: list[dict], ruta: str) -> None:
    """
    PRE: Todos los alumnos deben tener las llaves "NOMBRE", "APELLIDO", "PADRON".
    POST: Guarda en el archivo alumnos.txt la información de los alumnos.
    """
    with open(ruta, "w") as archivo:
        for alumno in alumnos:
            archivo.write(f"{alumno[PADRON]},{alumno[NOMBRE]},{alumno[APELLIDO]}\n")


def agregar_registro(alumno: dict, ruta: str) -> None:
    """
    PRE: El alumno debe tener la llave "PADRON".
    POST: Se agrega en el registro la fecha, hora y el padrón dado de alta.
    """
    with open(ruta, "a") as registro:
        registro.write(f"{ctime(time())}: Se agrego el alumno con padron {alumno[PADRON]}\n")
