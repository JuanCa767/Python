import pandas as pd

datos = "C:/Users/Juan/Documents/GitHub/Python/UNIDAD 5/movies.csv"

def resumenCotizacion(fichero):
    df = pd.read_csv(fichero, sep=',', decimal='.', thousands=',', index_col=0)
    return pd.DataFrame([df.min(), df.max(), df.mean()], index=["Valor minimo", "Valor Maximo", "Valor Promedio"], columns=['Gross Earnings','IMDB Score'])


print(resumenCotizacion(datos))
