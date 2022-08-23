import pandas as pd
from matplotlib import pyplot as plt

from datetime import timedelta, datetime
from pprint import pprint

def timestamp_to_datetime(timestamp):
    # Quito los milisegundos
    cleaned = timestamp.split('.')[0]

    # Convierto el string de fecha a un datetime
    date = datetime.strptime(cleaned, '%Y-%m-%dT%H:%M:%S')

    # Le resto 5 horas para que sean horas de Colombia
    return  date - timedelta(hours=5)

def timestamp_to_hour(timestamp):
    # Quito los milisegundos
    cleaned = timestamp.split('.')[0]

    # Convierto el string de fecha a un datetime
    date = datetime.strptime(cleaned, '%Y-%m-%dT%H:%M:%S')
    colombian_date = date - timedelta(hours=5)

    # Le resto 5 horas para que sean horas de Colombia
    return  colombian_date.hour


def filtrar_dataframe(df):
    # Primero remuevo los mensajes del canal de bienvenida, pues estos
    # no tienen solicitudes de tutoria
    df = df[df.channel_name != 'bienvenida']

    # Quito los mensajes nulos
    df = df[df.content.notnull()]

    # Tambien remuevo los comandos
    df = df[df.is_command == False]

    return df