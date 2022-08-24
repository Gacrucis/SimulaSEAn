import pandas as pd
# from pandas import Timestamp
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
    # Le resto 5 horas para que sean horas de Colombia
    colombian_date = date - timedelta(hours=5)

    return  colombian_date.hour + colombian_date.minute / 60

# Requiero las tutorias registradas para esto
def get_tutors(tutorials_df):
    
    return tutorials_df.tutor_id.unique()

def filter_messages(df, tutor_list, lower_hour, upper_hour):
    
    # Agrego una columna con la hora del dia en la que se envio el mensaje
    df['sent_hour'] = df.sent_date.apply(timestamp_to_hour)

    # Y actualizo la columna de fecha de envio para que sea de tipo datetime
    df.sent_date = df.sent_date.apply(timestamp_to_datetime)

    # Tomo solo los mensajes cuya hora estan dentro de la jornada de tutorias
    df = df[df.sent_hour < upper_hour]
    df = df[df.sent_hour >= lower_hour]
    
    # Remuevo los mensajes del canal de bienvenida, pues estos
    # nunca son solicitudes de tutoria
    df = df[df.channel_name != 'bienvenida']

    # Quito los mensajes nulos
    df = df[df.content.notnull()]

    # Tambien remuevo los comandos
    df = df[df.is_command == False]
    
    # Y quito los mensajes hechos por tutores
    df = df[~df.author_id.isin(tutor_list)]

    return df