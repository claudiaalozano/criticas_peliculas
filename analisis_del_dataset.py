import csv


#funcion para analizar CRITICA DE PELICULAS- Hoja 1.csv y devolver el 68% y el 95% de los datos 
import csv
def analisis_peliculas(archivo):
    with open(archivo, 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
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

    


#funcion mediante pandas para analizar CRITICA DE PELICULAS- Hoja 1.csv y devolver el 68% y el 95% de los datos
import pandas as pd
import csv
def analisis_peliculas_pandas("CRITICA_DE_PELICULAS_Hoja1.csv"):
    df = pd.read_csv(CRITICA DE PELICULAS- Hoja 1.csv, sep=',')
    df.columns = ['id', 'titulo', 'critica']
    df.head()
    df.info()
    df.describe()
    df.groupby('critica').count()
    df.groupby('critica').count().plot(kind='bar')
    df.groupby('critica').count().plot(kind='pie')
    df.groupby('critica').count().plot(kind='pie', subplots=True)
    df.groupby('critica').count().plot(kind='pie', subplots=True, figsize=(6, 6))
    df.groupby('critica').count().plot(kind='pie', subplots=True, figsize=(6, 6), autopct='%1.1f%%')
    df.groupby('critica').count().plot(kind='pie', subplots=True, figsize=(6, 6), autopct='%1.1f%%', startangle=90)
    df.groupby('critica').count().plot(kind='pie', subplots=True, figsize=(6, 6), autopct='%1.1f%%', startangle=90, labels=['Critica', 'Buena', 'Mala'])
    df.groupby('critica').count().plot(kind='pie', subplots=True, figsize=(6, 6), autopct='%1.1f%%', startangle=90, labels=['Critica', 'Buena', 'Mala'], colors=['red', 'green', 'blue'])
    df.groupby('critica').count().plot(kind='pie', subplots=True, figsize=(6, 6), autopct='%1.1f%%', startangle=90, labels=['Critica', 'Buena', 'Mala'], colors=['red', 'green', 'blue'], shadow=True)
    df.groupby('critica').count().plot(kind='pie', subplots=True, figsize=(6, 6), autopct='%1.1f%%', startangle=90, labels=['Critica', 'Buena', 'Mala'], colors=['red', 'green', 'blue'], shadow=True, explode=[0.1, 0, 0])
    df.groupby('critica').count().plot(kind='pie', subplots=True, figsize=(6, 6), autopct='%1.1f%%', startangle=90, labels=['Critica', 'Buena', 'Mala'], colors=['red', 'green', 'blue'], shadow=True, explode=[0.1, 0, 0], labeldistance=1.2)
    df.groupby('critica').count().plot(kind='pie', subplots=True, figsize=(6, 6), autopct='%1.1f%%', startangle=90, labels=['Critica', 'Buena', 'Mala'], colors=['red', 'green', 'blue'], shadow=True, explode=[0.1, 0, 0], labeldistance=1.2, fontsize=12)
    df.groupby('critica').count().plot(kind='pie', subplots=True, figsize=(6, 6), autopct='%1.1f%%', startangle=90, labels=['Critica', 'Buena', 'Mala'], colors=['red', 'green', 'blue'], shadow=True, explode=[0.1, 0, 0], labeldistance=1.2, fontsize=12, fontweight='bold')
    df.groupby('critica').count().plot(kind='pie', subplots=True, figsize=(6, 6), autopct='%1.1f%%', startangle=90, labels=['Critica', 'Buena', 'Mala'], colors=['red', 'green', 'blue'], shadow=True, explode=[0.1, 0, 0], labeldistance=1.2, fontsize=12, fontweight='bold', fontname='Arial')
    df.groupby('critica').count().plot(kind='pie', subplots=True, figsize=(6, 6), autopct='%1.1f%%', startangle=90, labels=['Critica', 'Buena', 'Mala'], colors=['red', 'green', 'blue'], shadow=True, explode=[0.1, 0, 0], labeldistance=1.2, fontsize=12, fontweight='bold', fontname='Arial', rotation=90)
    df.groupby('critica').count().plot(kind='pie', subplots=True, figsize=(6, 6), autopct='%1.1f%%', startangle=90, labels=['Critica', 'Buena', 'Mala'], colors=['red', 'green', 'blue'], shadow=True, explode=[0.1, 0, 0], labeldistance=1.2, fontsize=12, fontweight='bold', fontname='Arial', rotation=90, center=(0, 0))
