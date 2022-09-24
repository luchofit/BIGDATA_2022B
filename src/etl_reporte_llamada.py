#Pseudo codigo
#main ()
#   datos = get_data(filename)
#   reporte = generate_report(datos)
#   save_date(reporte)

import os
from pathlib import Path
import pandas as pd

root_dir = Path(".").resolve() 

def get_data(filename):
    filename = "llamadas123_julio_2022.csv" #creamos variable con el nombre del archivo que queremos extraer
    data_dir = "raw"
    file_path = os.path.join(root_dir, "data", data_dir, filename) #me una las palabras dentro con / para crear la ruta de la carpeta
    datos = pd.read_csv(file_path, sep=";", encoding="latin-1")
    print("estoy en get data")
    print("la tabla contiene", datos.shape[0],"filas", datos.shape[1],"columnas")
    return datos

def generate_report(datos):
    lista_columnas = datos.columns
    dict_reporte = dict()

    #loop para crear una lista del diccionario con valores unicos
    for col in lista_columnas:
        lista_unicos = datos[col].unique()
        n_unicos = len(lista_unicos) #recuerda que len de caracter es diferente que len de lista
        # len de "hola" es 4 y len de (e,a,d) es 3 
        dict_reporte[col] =n_unicos
        print(dict_reporte)
    reporte = pd.DataFrame.from_dict(dict_reporte, orient="index") 
    reporte.rename({0:"Conteo"}, inplace=True, axis=1)
    print("generate_report")
    print(reporte.head())
    return reporte

def save_date(reporte,filename):
    out_name = "reporte_" + filename 
    out_path = os.path.join(root_dir,"data","processed", out_name)
    reporte.to_csv(out_path)
    

def main():
    filename = "llamadas123_julio_2022.csv"
    datos = get_data(filename)
    reporte = generate_report(datos)
    save_date(reporte, filename)

if __name__ == "__main__":
    main()
