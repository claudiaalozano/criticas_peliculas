import csv


#funcion para analizar critica_pelis.csv 
def analisis_critica_peliculas(archivo):
    with open('critica_pelis.csv', newline=" ") as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar=',',
                        quoting=csv.QUOTE_MINIMAL)
        contador = 0
        contador_critica = 0
        contador_buena = 0
        contador_mala = 0
        contador_total = 0
        for row in reader:
            contador += 1
            if row[2] == 'Critica':
                contador_critica += 1
            elif row[2] == 'Buena':
                contador_buena += 1
            elif row[2] == 'Mala':
                contador_mala += 1
            contador_total += 1
        print('El 68% de los datos son criticas: ', contador_critica/contador*100)
        print('El 95% de los datos son criticas: ', contador_critica/contador*100)
        print('El 68% de los datos son buenas: ', contador_buena/contador*100)
        print('El 95% de los datos son buenas: ', contador_buena/contador*100)
        print('El 68% de los datos son malas: ', contador_mala/contador*100)
        print('El 95% de los datos son malas: ', contador_mala/contador*100)
        print('El 68% de los datos son criticas: ', contador_critica/contador*100)
        print('El 95% de los datos son criticas: ', contador_critica/contador*100)
        print('El 68% de los datos son buenas: ', contador_buena/contador*100)
        print('El 95% de los datos son buenas: ', contador_buena/contador*100)
        print('El 68% de los datos son malas: ', contador_mala/contador*100)
        print('El 95% de los datos son malas: ', contador_mala/contador*100)







