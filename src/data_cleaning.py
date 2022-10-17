#main()
# datos = leer_datos(nombre del archivo: str)-->pd.dataframe
# datos_no_dup = remover_duplicados_y_nulos(datos: pd.dataframe) --> pd.data
# datos = convertir_str_a_num(datos, col ="EDAD")-->pd.dataframe
# datos = corregir_fechas(datos, col="FECHA1")->pd.dataframe
# datos = corregir_fecha(datos, col="FECHA2")-->pd.dataframe

import argparse
from fileinput import filename
import os
from pathlib import Path
import pandas as pd
import numpy as np
from dateutil.parser import parse
#from tabnanny import verbose

data_source = Path(".").resolve().parent
# bucket = "gs://lcastro_llamadas_123a" data_source desde la nube (explicado en video youtube)
listmonth = ["enero","febrero","marzo","abril","mayo","junio","julio","agosto","septiembre","octubre","noviembre","diciembre"]
listyear = ["2021","2022"]
mes = str(input("Por favor ingrese el mes que quiere analizar: "))
ano = str(input("Por favor ingrese el año que quiere analizar: "))
mes = mes.strip()
ano = ano.strip()
try: 
    if mes not in listmonth and ano not in listyear:
        raise ValueError("No se encuentra este mes y año aún disponible para analizar. Por favor intente otra combinación")
    else:
        file_name = "llamadas123_"+mes+"_"+ano+".csv"
        print(file_name)
except ValueError as ve:
    print(ve)    

def get_data(file_name):
    data_raw = os.path.join(data_source,"data","raw",file_name)
    #data_raw = os.path.join(bucket,"data","raw",file_name) nube
    datos = pd.read_csv(data_raw, sep =";", encoding="latin-1")
    try: 
        if datos.shape[1] != 11:
            raise ValueError("Revise el # de columnas del archivo antes de ingresarlo para analizar")
        else:
            datos.columns = datos.columns.str.replace('[#,@,&,-]', '_')
            datos.columns = ["NUMERO_INCIDENTE","FECHA_INICIO_DESPLAZAMIENTO_MOVIL","CODIGO_LOCALIDAD","LOCALIDAD","EDAD","UNIDAD","GENERO","RED","TIPO_INCIDENTE","PRIORIDAD","RECEPCION"]
    except ValueError as ve:
        print(ve)
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
    new_data[col_edad].replace({"SIN_DATO": np.nan, "Sin_dato": np.nan}, inplace =True) #reemplazo SIN_DATO y Sin_dato  por valor nan en la columna EDAD
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
    out_name = "reporte_compilado.csv"
    out_path = os.path.join(data_source,"data","processed", out_name)
    #out_path = os.path.join(bucket,"data","processed", out_name) nube
    #new_data.to_csv(out_path, mode="a", header=not os.path.isfile(out_path) and os.stat(out_path).st_size != 0) #comprobamos que es un archivo y ademas no esta vació
    new_data.to_csv(out_path, mode="a")

def main():
    datos = get_data(file_name)
    new_data = duplicates(datos)
    new_data = cleaning(new_data)
    save_date(new_data)
    

if __name__ == "__main__":
    main()