import csv



#nombre_archivo= "critica_pelis.csv"
#with open('critica_pelis.csv', "r") as archivo:
#    for linea in archivo:
      #  linea= linea.rstrip()
    #    separate= ","
     #   lista = linea.split(",")
     #   nota=int(lista[0])
     #   numero_votantes= int (lista[1])
        



#función para analizar datos_peliculas.csv
def analisis_datos_peliculas(nombre_archivo):
    with open("datos_peliculas.csv", "r") as archivo:
        for linea in archivo:
            linea= linea.rstrip()
            separate= ","
            lista = linea.split(",")
            nota=int(lista[0])
            numero_votantes= int (lista[1])
            promedio= nota/numero_votantes
            print("La nota es: ", nota)
            print("El numero de votantes es: ", numero_votantes)
            print("El promedio es: ", promedio)
            print("\n")
    #obtenemos el 68% de los votos
    with open("datos_peliculas.csv", "r") as archivo:
        for linea in archivo:
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
    #obtenemos el 95% de los votos
    with open("datos_peliculas.csv", "r") as archivo:
        for linea in archivo:
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
    #obtenemos el 97% de los votos
    with open("datos_peliculas.csv", "r") as archivo:
        for linea in archivo:
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