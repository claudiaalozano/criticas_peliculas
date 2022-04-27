import csv


#funcion para analizar critica_pelis.csv 
def analisis_critica_peliculas(archivo):
    with open('critica_pelis.csv', newline=" ") as File:
        reader = csv.reader(File, delimiter=',', quotechar=',',
                        quoting=csv.QUOTE_MINIMAL)
        
        for row in reader:
            print(row)
    



nombre_archivo= "critica_pelis.csv"
with open('critica_pelis.csv', "r") as archivo:
    for linea in archivo:
        linea= linea.rstrip()
        separate= ","
        lista = linea.split(",")
        nota=int(lista[0])
        numero_votantes= int (lista[1])
        



