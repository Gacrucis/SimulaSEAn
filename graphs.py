import numpy as np
from matplotlib import pyplot as plt

import distributions

def graph_message_hour_histogram(df, day_start, day_end):
    hour_bins = [n for n in range(day_start, day_end+1)]
    timestamps = list(df.sent_hour)

    n, bins = np.histogram(timestamps, bins=hour_bins)

    dist = distributions.histogram_to_generator(n, bins)

    nn = [dist() for n in range(10000)]

    fig = plt.figure(1)
    plt.hist(nn, bins=hour_bins) #type: ignore
    plt.xlabel('Hora')
    plt.ylabel('Frecuencia')
    plt.title('Histograma de mensajes por hora del dia (Filtrados)')
    plt.show()


def graph_tutorial_hour_histogram(df, day_start, day_end):
    hour_bins = [n for n in range(day_start, day_end+1)]
    timestamps = list(df.tutorial_hour)

    n, bins = np.histogram(timestamps, bins=hour_bins)

    dist = distributions.histogram_to_generator(n, bins)

    nn = [dist() for n in range(10000)]

    fig = plt.figure(2)
    plt.hist(nn, bins=hour_bins) #type: ignore
    plt.xlabel('Hora')
    plt.ylabel('Frecuencia')
    plt.title('Histograma de tutorias por hora del dia (Filtradas)')
    plt.show()

def graph_tutorial_time_histogram(df, hard_min=5, hard_max=120, minute_step=10):

    min_duration = max(min(df.estimated_duration), hard_min)
    max_duration = min(max(df.estimated_duration), hard_max)
    minute_bins = [n for n in range(min_duration, max_duration+1, minute_step)]
    durations = list(df.estimated_duration)

    n, bins = np.histogram(durations, bins=minute_bins)

    dist = distributions.histogram_to_generator(n, bins)

    nn = [dist() for n in range(10000)]

    fig = plt.figure(3)
    plt.hist(nn, bins=minute_bins) #type: ignore
    plt.xlabel('Minutos')
    plt.ylabel('Frecuencia')
    plt.title('Histograma de tiempos de tutoria')
    plt.show()