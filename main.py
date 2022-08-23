import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from pprint import pprint

import reader
import distributions


data_path = './data/messages.csv'

df = pd.read_csv(data_path)
df = reader.filtrar_dataframe(df)


l = 14
u = 21
timestamps = map(reader.timestamp_to_hour, df['sent_date'])
timestamps = [t for t in timestamps if l <= t <= u]

# print(timestamps)

n, bins = np.histogram(timestamps, bins=u-l)

dist = distributions.histogram_to_generator(n, bins)

nn = [dist() for n in range(10000)]
plt.hist(nn, bins=u-l) #type: ignore
plt.show()