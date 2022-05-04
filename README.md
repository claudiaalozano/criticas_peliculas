# CRITICA DE PELICULAS

Mi dirección de github es: https://github.com/claudiaalozano/criticas_peliculas.git

Para realizar este trabajo he creado un dataset con el número de votantes y con una calificación de 0 a 5. En el archivo aparecen dos archivos csv, uno más detallado donde muestro un gráfico y más datos estadísticos, y otro donde muestro los datos necesarios para ejecutar el código.

El código empleado es: 
```
import csv
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

peliculas = pd.read_csv("datos_pelis.csv" , sep= "\t")
peliculas = peliculas.dropna()


def media_notas_pandas():
    media_notas = peliculas.groupby("nota")["nota"].mean()
    print(media_notas)


def desviacion_estandar_pandas():
    desviacion_estandar = peliculas.groupby("nota")["nota"].std()
    print(desviacion_estandar)


def media_desviacion_tipica_pandas():
    media_notas = peliculas.groupby("nota")["nota"].mean()
    desviacion_estandar = peliculas.groupby("nota")["nota"].std()
    print(media_notas)
    print(desviacion_estandar)
    print("\n")
    print("El 68% de los votos es: ", media_notas.loc[6.8])
    print("El 95% de los votos es: ", media_notas.loc[9.5])
    print("El 97% de los votos es: ", media_notas.loc[9.7])
    print("\n")


def diagrama_barras_pandas():
    notas = peliculas.groupby("nota")["nota"].count()
    notas.plot(kind="bar")
    plt.savefig("diagrama_barras.png")
    plt.show()


def diagrama_dispersion_pandas():
  fig, ax = plt.subplots()
  notas = peliculas.groupby("nota")["nota"].count()
  notas.plot(kind="box")
  plt.savefig("diagrama_dispersión.png")
  plt.show()
    
```
