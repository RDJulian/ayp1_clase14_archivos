from os import path
from time import time, ctime


# Manejo de archivos
def generarRegistro() -> None:
    """
    PRE:
    POST: Genera un archivo de registro en caso de no existir.
    """
    if not path.isfile("registro.txt"):
        with open("registro.txt", "w") as registro:
            registro.write(f"Registro de altas de alumnos:\n")


def generarArchivoAlumnos() -> None:
    """
    PRE:
    POST: Genera un archivo de alumnos.
    """
    with open("alumnos.txt", "w"):
        pass


def leerDatosAlumnos() -> list[dict]:
    """
    PRE:
    POST: Devuelve una lista de diccionarios con la información de los alumnos.
    """
    alumnos = []
    with open("alumnos.txt", "r") as archivo:
        while linea := archivo.readline():
            informacion = linea.split()
            alumno = {"Padron": informacion[0], "Nombre": informacion[1], "Apellido": informacion[2]}
            alumnos.append(alumno)
    return alumnos


def cargarDatosAlumnos() -> list[dict]:
    """
    PRE:
    POST: Devuelve la lista si habia un archivo guardado o una vacia de lo contrario.
    """

    if path.isfile("alumnos.txt"):
        return leerDatosAlumnos()
    else:
        generarArchivoAlumnos()
        return []


def guardarAlumno(alumno: dict) -> None:
    """
    PRE: El alumno debe tener las tres llaves ("Nombre", "Apellido", "Padron").
    POST: Se guarda la información del alumno en el archivo de alumnos.
    """
    with open("alumnos.txt", "a") as archivo:
        archivo.write(f"{alumno['Padron']} {alumno['Nombre']} {alumno['Apellido']}\n")


def agregarRegistro(alumno: dict) -> None:
    """
    PRE: El alumno debe tener la llave "Padron".
    POST: Se agrega en el registro la fecha, hora y el padron dado de alta en el archivo de alumnos.
    """
    with open("registro.txt", "a") as registro:
        registro.write(f"{ctime(time())}: Se agrego el alumno con padron {alumno['Padron']}\n")


# Codigo de la Clase 8
def agregarAlumno(alumnos: list[dict]) -> None:
    """
    PRE:
    POST: Se agrega un nuevo alumno a la lista, con un Padron (int), Nombre (str) y Apellido (str).
    """
    padron = int(input("Ingrese el padron: "))
    nombre = input("Ingrese el nombre: ")
    apellido = input("Ingrese el apellido: ")
    alumno = {"Padron": padron, "Nombre": nombre, "Apellido": apellido}
    alumnos.append(alumno)
    guardarAlumno(alumno)
    agregarRegistro(alumno)


def buscarAlumno(alumnos: list[dict]) -> dict | None:
    """
    PRE: Los alumnos que esten en la lista deben tener una llave "Nombre".
    POST: Devuelve el alumno buscado si coincide el nombre ingresado, None en caso contrario.
    """
    padron = input("Ingrese el padron a buscar: ")
    indice = 0
    alumnoBuscado = None
    while indice < len(alumnos) and alumnoBuscado is None:
        if alumnos[indice]["Padron"] == padron:
            alumnoBuscado = alumnos[indice]
        indice += 1
    return alumnoBuscado


def imprimirAlumno(alumno: dict | None) -> None:
    """
    PRE: El alumno debe tener las tres llaves ("Nombre", "Apellido", "Padron"), en caso de no ser None.
    POST: Se imprime la información del alumno, o un mensaje de error si se recibe None.
    """
    if alumno is not None:
        print(f'Padron: {alumno["Padron"]}\nNombre: {alumno["Nombre"]}\nApellido: {alumno["Apellido"]}\n')
    else:
        print("El alumno no fue encontrado.\n")


def imprimirAlumnos(alumnos: list[dict]) -> None:
    """
    PRE: Todos alumnos deben tener las tres llaves ("Nombre", "Apellido", "Padron").
    POST: Se imprime la información de todos los alumnos en la lista.
    """
    for alumno in alumnos:
        imprimirAlumno(alumno)


def imprimirMenu() -> None:
    """
    PRE:
    POST: Se imprime el menu de opciones válidas.
    """
    print(
        f"1. Agregar alumno\n2. Buscar alumno por padron\n3. Imprimir la informacion de todos los alumnos\n4. Salir\n")


def main() -> None:
    alumnos = cargarDatosAlumnos()
    generarRegistro()
    opcion = 0
    while not opcion == 4:
        imprimirMenu()
        opcion = int(input("Ingrese una opcion: "))
        if opcion == 1:
            agregarAlumno(alumnos)
        elif opcion == 2:
            alumno = buscarAlumno(alumnos)
            imprimirAlumno(alumno)
        elif opcion == 3:
            imprimirAlumnos(alumnos)


main()
