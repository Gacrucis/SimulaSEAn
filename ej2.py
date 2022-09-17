import pandas as pd
from matplotlib import pyplot as plt

import reader

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
shift_delta = 2


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

df = tutorials_df
df.registered_date = pd.to_datetime(df['registered_date']).dt.date
m = df.groupby(['registered_date']).count().max()[0]
print(m)