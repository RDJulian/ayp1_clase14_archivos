# Clase 14: Introducción a Manejo de Archivos

En esta clase vamos a ver cómo crear y escribir archivos de texto. Manipularemos archivos de formato .txt y .csv. Luego, 
veremos una aplicación práctica, ampliando un programa que ya escribimos, para generar una base de datos y un reporte.

# Presentación

[Enlace a la presentación](https://docs.google.com/presentation/d/1uARtJxOMvpRhCPZFVv9e_kZ6kDwfE7C2mWfHfylfr-w/edit?usp=sharing)

# Ejercicio

Anteriormente, escribimos un programa para dar de alta la información de alumnos. Como cumplimos con las expectativas, 
nos pidieron ampliarlo. Esta vez, nos piden **mantener** las funcionalidades que el programa ya tiene, agregando:

<ol>
<li>
La información debe ser guardada en un archivo alumnos.txt, para luego leerla al abrir el programa. El formato debe cumplir:<br>

>PADRON NOMBRE APELLIDO
</li>
<li>
Se debe generar un archivo registro.txt, que guarde la fecha, hora y el padrón del alumno cuando se le da de alta. El formato debe ser:<br>
    
>FECHA HORA: Se dio de alta al alumno con padron PADRON
</li>
<li>
Como el formato .txt no es favorable para guardar la información de los alumnos, se debe mantener la funcionalidad, pero
generando un archivo de formato .csv.
</li>
<li>
Como la cantidad de alumnos es muy alta para tener toda la información cargada en RAM, se pide que solamente se carguen
los padrones de los alumnos. En caso de necesitar acceder a la información, leerla desde el archivo.
</li>
</ol>

Recomendacion: realizar cada uno de los puntos de forma secuencial, como si se tratasen de diferentes versiones del programa.