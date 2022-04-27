from Clases import analisis_del_dataset
from Clases.analisis_del_dataset import analisis_datos_peliculas
if __name__ == "__main__":
    analisis_del_dataset.analisis_datos_peliculas("votos_peliculas.csv")
    print("A continuación se muestran los datos por pantalla.")
    print(analisis_del_dataset.analisis_datos_peliculas("datos_pelis.csv"))
    