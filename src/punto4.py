from os import path
from time import ctime, time

# Constantes
ALTA_ALUMNO = 1
BUSCAR_ALUMNO = 2
LISTAR_ALUMNOS = 3
SALIR = 4

ARCHIVO_ALUMNOS = "alumnos.csv"
ARCHIVO_REGISTRO = "registro.txt"


# Codigo de la Clase 8 modificado.
def esAlumnoYaIngresado(padron: int, alumnos: list[int]) -> bool:
    """
    PRE:
    POST: Devuelve True si el padron está dado de alta, False en caso contrario.
    """
    if padron in alumnos:
        return True
    else:
        return False


def agregarAlumno(alumnos: list[int]) -> None:
    """
    PRE:
    POST: Guarda la información del alumno y genera un registro si aún no fue dado de alta. De lo contrario, imprime un
    mensaje de error.
    """
    padron = int(input("Ingrese el padron: "))
    nombre = input("Ingrese el nombre: ")
    apellido = input("Ingrese el apellido: ")
    if not esAlumnoYaIngresado(padron, alumnos):
        guardarInformacionAlumno(padron, nombre, apellido)
        alumnos.append(padron)
        agregarRegistro(padron)
    else:
        print(f"El alumno con padron {padron} ya fue dado de alta.")


def buscarAlumno(alumnos: list[int]) -> list | None:
    """
    PRE:
    POST: Devuelve la información del alumno a buscar si fue dado de alta, None de lo contrario.
    """
    padron = int(input("Ingrese el padron a buscar: "))
    if esAlumnoYaIngresado(padron, alumnos):
        return buscarInformacionAlumno(padron)
    else:
        return None


def imprimirAlumno(informacion: list | None) -> None:
    """
    PRE: La información debe ser completa (padron, nombre, apellido).
    POST: Imprime por pantalla la información del alumno. Si no se encontró, imprime un mensaje de error.
    """
    if informacion is not None:
        print(f'Padron: {informacion[0]}\nNombre: {informacion[1]}\nApellido: {informacion[2]}\n')
    else:
        print("El alumno no fue encontrado.\n")


def imprimirAlumnos() -> None:
    """
    PRE: El archivo alumnos.csv debe existir.
    POST: Imprime por pantalla la información de todos los alumnos.
    """
    with open(ARCHIVO_ALUMNOS, "r") as archivo:
        while linea := archivo.readline().rstrip():
            imprimirAlumno(linea.split(','))


def imprimirMenu() -> None:
    """
    PRE:
    POST: Se imprime el menu de opciones válidas.
    """
    print(
        f"1. Agregar alumno\n2. Buscar alumno por padron\n3. Imprimir la informacion de todos los alumnos\n4. Salir\n")


# Manejo de archivos.
def leerInformacionAlumnos() -> list[int]:
    """
    PRE: El archivo alumnos.csv debe existir.
    POST: Devuelve una lista de todos los padrones cargados.
    """
    alumnos = []
    with open(ARCHIVO_ALUMNOS, "r") as archivo:
        while linea := archivo.readline().rstrip():
            informacion = linea.split(',')
            alumnos.append(int(informacion[0]))
    return alumnos


def buscarInformacionAlumno(padron: int) -> list:
    """
    PRE: El archivo alumnos.csv debe existir.
    POST: Devuelve una lista con la información del alumno buscado.
    """
    encontrado = False
    with open(ARCHIVO_ALUMNOS, "r") as archivo:
        while not encontrado and (linea := archivo.readline().rstrip()):
            informacion = linea.split(',')
            if int(informacion[0]) == padron:
                encontrado = True
    return informacion


def guardarInformacionAlumno(padron: int, nombre: str, apellido: str) -> None:
    """
    PRE:
    POST: Guarda la informacion del alumno al final del archivo alumnos.csv.
    """
    with open(ARCHIVO_ALUMNOS, "a") as archivo:
        archivo.write(f"{padron},{nombre},{apellido}\n")


def generarArchivoAlumnos():
    """
    PRE:
    POST: Genera el archivo alumnos.csv.
    """
    with open(ARCHIVO_ALUMNOS, "w"):
        pass


def cargarArchivoAlumnos() -> list[int]:
    """
    PRE:
    POST: Devuelve una lista de todos los padrones cargados. Devuelve una lista vacia si el archivo alumnos.csv no
    existe.
    """
    # Esta linea revisa si el archivo existe.
    if path.isfile(ARCHIVO_ALUMNOS):
        return leerInformacionAlumnos()
    else:
        generarArchivoAlumnos()
        return []


def generarRegistro() -> None:
    """
    PRE:
    POST: Genera el archivo registro.txt si no existe.
    """
    if not path.isfile(ARCHIVO_REGISTRO):
        with open(ARCHIVO_REGISTRO, "w") as registro:
            registro.write(f"Registro de altas de alumnos:\n")


def agregarRegistro(padron: int) -> None:
    """
    PRE:
    POST: Se agrega en el registro la fecha, hora y el padron dado de alta en el archivo de alumnos.
    """
    with open(ARCHIVO_REGISTRO, "a") as registro:
        registro.write(f"{ctime(time())}: Se agrego el alumno con padron {padron}\n")


# Para el punto 4, el codigo cambia considerablemente. Leer con atencion.
def main() -> None:
    alumnos = cargarArchivoAlumnos()
    generarRegistro()
    opcion = 0
    while not opcion == SALIR:
        imprimirMenu()
        opcion = int(input("Ingrese una opcion: "))
        if opcion == ALTA_ALUMNO:
            agregarAlumno(alumnos)
        elif opcion == BUSCAR_ALUMNO:
            informacion = buscarAlumno(alumnos)
            imprimirAlumno(informacion)
        elif opcion == LISTAR_ALUMNOS:
            imprimirAlumnos()


main()
