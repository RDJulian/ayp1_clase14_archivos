# Constantes
ALTA_ALUMNO = 1
BUSCAR_ALUMNO = 2
LISTAR_ALUMNOS = 3
SALIR = 4


# Codigo de la Clase 8
def agregarAlumno(alumnos: list[dict]) -> None:
    """
    PRE: Los alumnos que esten en la lista deben tener una llave "Padron".
    POST: Se agrega un nuevo alumno a la lista, con un Padron (int), Nombre (str) y Apellido (str). Imprime un mensaje
    de error si ya se ingresó.
    """
    padron = int(input("Ingrese el padron: "))
    nombre = input("Ingrese el nombre: ")
    apellido = input("Ingrese el apellido: ")
    if buscarAlumno(padron, alumnos) is None:
        alumno = {"Padron": padron, "Nombre": nombre, "Apellido": apellido}
        alumnos.append(alumno)
    else:
        print(f"El alumno con padron {padron} ya fue dado de alta.")


def buscarAlumno(padron: int, alumnos: list[dict]) -> dict | None:
    """
    PRE: Los alumnos que esten en la lista deben tener una llave "Padron".
    POST: Devuelve el alumno buscado si coincide el padron ingresado, None en caso contrario.
    """
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
    PRE: Todos los alumnos deben tener las tres llaves ("Nombre", "Apellido", "Padron").
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
    alumnos = []
    opcion = 0
    while not opcion == SALIR:
        imprimirMenu()
        opcion = int(input("Ingrese una opcion: "))
        if opcion == ALTA_ALUMNO:
            agregarAlumno(alumnos)
        elif opcion == BUSCAR_ALUMNO:
            padron = int(input("Ingrese el padron a buscar: "))
            alumno = buscarAlumno(padron, alumnos)
            imprimirAlumno(alumno)
        elif opcion == LISTAR_ALUMNOS:
            imprimirAlumnos(alumnos)


main()
