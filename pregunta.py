"""
Limpieza de datos usando Pandas
-----------------------------------------------------------------------------------------

Realice la limpieza del dataframe. Los tests evaluan si la limpieza fue realizada 
correctamente. Tenga en cuenta datos faltantes y duplicados.

"""
import pandas as pd
from datetime import datetime
import re

def clean_data():
    df = pd.read_csv("solicitudes_credito.csv", sep=";", encoding="utf-8", index_col=0)
    
    df = df.dropna(axis = 0)
    for c in df.columns:
        if (df[c].dtype not in ['int64', 'float64']):
            df[c] = df[c].apply(str.lower)
            df[c] = df[c].apply(lambda x: x.replace("-", " "))
            df[c] = df[c].apply(lambda x: x.replace("_", " "))
            df[c] = df[c].apply(lambda x: x.replace(",", ""))
            df[c] = df[c].apply(lambda x: x.replace(".00", ""))
            df[c] = df[c].apply(lambda x: x.replace("$ ", ""))
            df[c] = df[c].apply(lambda x: x.replace("$", ""))
        if (c == "comuna_ciudadano"):
            df[c] = df[c].apply(lambda x: float(x))
        if (c == "monto_del_credito"):
            df[c] = df[c].apply(lambda x: int(x))
        if (c == "fecha_de_beneficio"):
            df[c] = df[c].apply(lambda x: datetime.strptime(x, "%Y/%m/%d") if (len(re.findall("^\d+/",x)[0]) - 1) == 4 else datetime.strptime(x, "%d/%m/%Y"))
    df = df.drop_duplicates().reset_index(drop=True)
    return df