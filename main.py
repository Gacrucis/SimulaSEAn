import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from pprint import pprint

import reader
import distributions

# Establezco estilo por defecto de graficas
plt.style.use('seaborn-deep')

# Tambien donde estan los datos a usar en la simulacion
paths = {
    'messages' : './data/messages.csv',
    'tutorials' : './data/tutorials.csv',
    'shifts' : './data/shifts.csv',
}

day_start = 14
day_end = 22
hour_bins = [n for n in range(day_start, day_end+1)]

# A priori, leo los csv en formato csv
tutorials_df = pd.read_csv(paths['tutorials']) 
messages_df = pd.read_csv(paths['messages'])

# Saco la lista de tutores, esto para filtrar mensajes
tutors = reader.get_tutors(tutorials_df)

# Filtro los mensajes (remuevo mensajes no relacionados a solicitud o actividad de tutorias)
messages_df = reader.filter_messages(messages_df, tutors, day_start, day_end)

timestamps = list(messages_df.sent_hour)

# print(sorted(timestamps))

# print(timestamps)

n, bins = np.histogram(timestamps, bins=hour_bins)

dist = distributions.histogram_to_generator(n, bins)

nn = [dist() for n in range(10000)]
plt.hist(nn, bins=hour_bins) #type: ignore

plt.show()