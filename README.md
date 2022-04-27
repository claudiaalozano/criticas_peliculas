# CRITICA DE PELICULAS

Mi dirección de github es: https://github.com/claudiaalozano/criticas_peliculas.git

Para realizar este trabajo he creado un dataset con el número de votantes y con una calificación de 0 a 5. En el archivo aparecen dos archivos csv, uno más detallado donde muestro un gráfico y más datos estadísticos, y otro donde muestro los datos necesarios para ejecutar el código.

El código empleado es: 
```
import csv
 
nombre_archivo = "datos_pelis.csv"
def analisis_datos_peliculas(nombre_archivo):
    with open(nombre_archivo, "r") as File:
        next(File, None)
        for linea in File:
            linea= linea.rstrip()
            separate= ","
            lista = linea.split(",")
            nota=lista[0]
            int_nota = nota (map(int,lista))
            numero_votantes= lista[1]
            int_numero_votantes = numero_votantes (map(int,lista))
            promedio= nota/numero_votantes
            print("La nota es: ", nota)
            print("El numero de votantes es: ", numero_votantes)
            print("El promedio es: ", promedio)
            print("\n")
    pregunta=input(int("¿Desea analizar el 68% (1), el 95% (2) o el 97%(3) de los votos? "))
    if pregunta == 1:
        with open(nombre_archivo, "r") as File:
            for linea in File:
                linea= linea.rstrip()
                separate= ","
                lista = linea.split(",")
                nota=int(lista[0])
                numero_votantes= int (lista[1])
                promedio= nota/numero_votantes
                if promedio>=6.8:
                    print("La pelicula es buena")
                else:
                    print("La pelicula es mala")
                print("\n")
    elif pregunta == 2:
        with open(nombre_archivo, "r") as File:
            for linea in File:
                linea= linea.rstrip()
                separate= ","
                lista = linea.split(",")
                nota=int(lista[0])
                numero_votantes= int (lista[1])
                promedio= nota/numero_votantes
                if promedio>=9.5:
                    print("La pelicula es buena")
                else:
                    print("La pelicula es mala")
                print("\n")
    elif pregunta == 3:   
        with open(nombre_archivo, "r") as File:
            for linea in File:
                linea= linea.rstrip()
                separate= ","
                lista = linea.split(",")
                nota=int(lista[0])
                numero_votantes= int (lista[1])
                promedio= nota/numero_votantes
                if promedio>=9.7:
                    print("La pelicula es buena")
                else:
                    print("La pelicula es mala")
                print("\n")


analisis_datos_peliculas(nombre_archivo)
```
