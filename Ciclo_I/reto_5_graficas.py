"""
Descripción y  requerimiento:

Como consultor técnico de la WHO (World Health Organization) se le ha solicitado que organice
la información necesaria para realizaruna gráfica qué: por continente, muestre la evolución del
promedio de la razón entre el número total de casos de COVID-19 y el número total de camas de
hospital disponibles a través del tiempo.

Para probar esta tarea, usted cuenta con el archivo de datos owid-covid-data.csv. Escriba una
función que reciba como parámetro una cadena con la ruta dónde se encuentra guardado el archivo,
incluyendo la extensión, y lo lea desde esta misma. A partir de estos datos, construya un
dataframe sobre el cual, al utilizar el método df.plot() se obtenga la
gráfica esperada
"""

import numpy as np
import pandas as pd


def caso_who(ruta_archivo_csv: str) -> dict:
    if ruta_archivo_csv[-4:len(ruta_archivo_csv)] != ".csv":
        return "Extensión inválida."
    try:
        data = pd.read_csv(ruta_archivo_csv)
        print(data.columns)
        print(data["continent"].unique())
        print(data.groupby("continent").count())
        return data.to_dict()
    except:
        return "Error al leer el archivode datos."

caso_who("owid-covid-data.csv")