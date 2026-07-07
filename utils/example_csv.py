import os
import csv, json
from pathlib import Path


def get_csv_data(csv_file="data_login.csv"):
    
    """esta funcion lee un archivo CSV 
    y devuelve una lista con una tupla por cada fila del archivo, 
    para usar en parametrizacion de pytest"""

    csv_file = Path (__file__).parent.parent / "data" / csv_file

    lista = [] 

    with open(csv_file, newline="") as archivo:
        lector = csv.DictReader(archivo) 

        for fila in lector:

            username = fila["username"]
            password = fila["password"]
            login_booleano = fila["login_booleano"].lower() == "true"                                                           

            lista.append((username, password, login_booleano))

    print(lista)

    return lista


def get_json_data(json_file="data.json"):

    json_file = Path (__file__).parent.parent / "data" / json_file

    lista = [] 

    with open(json_file) as archivo:
        datos = json.load(archivo)

        for fila in datos:

            username = fila["username"]
            password = fila["password"]
            login_booleano = fila["login_booleano"]                                                       

            lista.append((username, password, login_booleano))

    return lista





