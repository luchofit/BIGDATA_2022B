#main()
# datos = leer_datos(nombre del archivo: str)-->pd.dataframe
# datos_no_dup = remover_duplicados_y_nulos(datos: pd.dataframe) --> pd.data
# datos = convertir_str_a_num(datos, col ="EDAD")-->pd.dataframe
# datos = corregir_fechas(datos, col="FECHA1")->pd.dataframe
# datos = corregir_fecha(datos, col="FECHA2")-->pd.dataframe

import argparse
import os
from pathlib import Path
import pandas as pd
import numpy as np
from dateutil.parser import parse
from tabnanny import verbose

data_source = Path(".").resolve().parent
file_name = "llamadas123_julio_2022.csv"

def get_data(file_name):
    data_raw = os.path.join(data_source,"data","raw",file_name)
    datos = pd.read_csv(data_raw, sep =";", encoding="latin-1")
    return datos

def duplicates(datos):
    new_data = datos.drop_duplicates() 
    new_data.reset_index(inplace=True, drop=True)
    return new_data

def cleaning(new_data):
    col = "UNIDAD"
    new_data[col].fillna("SIN_DATO", inplace=True) #llenamos los nan con el string "SIN_DATO" y reemplazamos en la tabla
    new_data[col].value_counts(dropna = False, normalize=True)
    col_date = "FECHA_INICIO_DESPLAZAMIENTO_MOVIL"
    new_data[col_date] = pd.to_datetime(new_data[col_date], errors ="coerce",format="%Y/%m/%d")
    col_edad = "EDAD"
    new_data[col_edad].replace({"SIN_DATO": np.nan}, inplace =True) #reemplazo SIN_DATO por valor nan en la columna EDAD
    f = lambda x: x if pd.isna(x) else int(x)
    new_data[col_edad] = new_data[col_edad].apply(f) 
    col_recep = "RECEPCION"
    list_fechas = list()
    for fecha in new_data[col_recep]:
        try:
            new_date = parse(fecha)
        except Exception as e:
            new_date = pd.to_datetime(fecha, errors ="coerce")
        list_fechas.append(new_date)
    new_data["RECEPCION_corr"]=list_fechas
    new_data.head(10)
    return new_data

def save_date(new_data):
    out_name = "reporte_" + file_name 
    out_path = os.path.join(data_source,"data","processed", out_name)
    new_data.to_csv(out_path)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--verbose", type=int,default=0,help="para decidir si imprime información o no")
    args = parser.parse_args()
    verbose = args.verbose
    datos = get_data(file_name)
    new_data = duplicates(datos)
    new_data = cleaning(new_data)
    save_date(new_data,verbose)
    

if __name__ == "__main__":
    main()