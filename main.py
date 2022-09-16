from random import random
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

import reader
import graphs

# Establezco estilo por defecto de graficas
plt.style.use('seaborn-deep') #type: ignore

# Tambien donde estan los datos a usar en la simulacion
paths = {
    'messages' : './data/messages.csv',
    'tutorials' : './data/tutorials.csv',
    'shifts' : './data/shifts.csv',
}

day_start = 14
day_end = 22

# A priori, leo los csv en formato csv
tutorials_df = pd.read_csv(paths['tutorials']) 
messages_df = pd.read_csv(paths['messages'])
shifts_df = pd.read_csv(paths['shifts'])

# Saco la lista de tutores, esto para filtrar mensajes
tutors = reader.get_tutors(tutorials_df)

# Filtro los mensajes, tutorias y franjas
messages_df = reader.filter_messages(messages_df, tutors, day_start, day_end)
tutorials_df = reader.filter_tutorials(tutorials_df, day_start, day_end)
shifts_df = reader.filter_shifts(shifts_df, day_start, day_end)

# Obtengo funciones que generan numeros aleatorios de acuerdo a las distribuciones
# representadas por los histogramas
rmessage = graphs.graph_message_hour_histogram(messages_df, day_start, day_end)
graphs.graph_tutorial_hour_histogram(tutorials_df, day_start, day_end)
rtutorialtime = graphs.graph_tutorial_time_histogram(tutorials_df)
graphs.graph_shift_hour_histogram(shifts_df, day_start, day_end)

# Inicia la simulacion
print('Empieza la simulacion')
k = 1000
final_data = {
    'tutorias_fallidas' : [],
    'tutorias_cortadas' : [],
}

for _ in range(k):
    # Tiempo actual
    t = 0

    # Siguiente tiempo de llegada
    t_arrivals = sorted([rmessage() + random() for _ in range(40)]) #type: ignore
    t_arrivals.append(float('inf'))
    t_arrival = t_arrivals.pop(0)

    # Siguiente tiempo en el que sale una persona
    t_exits = [float('inf'), float('inf')]
    t_exit = min(t_exits)

    # Siguiente tiempo en el que ocurre un cambio de franja
    t_changes = [n for n in range(day_start, 2, day_end+1)]

    # Numero de gente llegada hasta el momento
    n_arrivals = 0

    # Tiempos de inicio y fin de dia
    t_start = day_start
    t_end = day_end

    # Cantidad de personas en cola para 
    queue = 0


    while t < t_end:

        t = min(t_arrival, t_exit)

        if t == float('inf'):
            break

        # Si el evento es de llegada
        if t == t_arrival:
            n_arrivals += 1

            t_arrival = t_arrivals.pop(0)

            # Lo paso de minutos a horas
            service_t = rtutorialtime() / 60 #type: ignore

            # Voy por la lista de tutores para buscar si hay alguno libre
            found = False
            for i, exit in enumerate(t_exits):
                # Si hay uno libre, le asigno un tiempo de salida y dejo de buscar
                if exit == float('inf'):
                    t_exits[i] = t + service_t
                    found = True
                    break

            t_exit = min(t_exits)

            # Si no se encontro tutor libre, aumento la cola
            if not found:
                queue += 1
                
        # Si el evento es de salida
        if t == t_exit:

            # Libero el tutor que termino la tutoria
            freed_tutor = t_exits.index(t)
            t_exits[freed_tutor] = float('inf')

            # Ahora asigno tutorias si hay en cola
            if queue > 0:
                # Lo paso de minutos a horas
                service_t = rtutorialtime() / 60 #type: ignore
                t_exits[freed_tutor] = t + service_t
                queue -= 1

            t_exit = min(t_exits)

    final_data['tutorias_fallidas'].append(queue)

df = pd.DataFrame(final_data)
df.to_csv('final_data.csv')