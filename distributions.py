import random
import numpy as np
from matplotlib import pyplot as plt

# Genera una funcion generadora de numeros aleatorios
# de acuerdo a la distribucion mostrada por un histograma
def histogram_to_generator(freq, bins):
    total = sum(freq)

    probs = freq / total

    def dist():
        p_list = probs
        nums = bins

        u = random.random()

        accum = 0
        for p, num in zip(p_list, nums):
            if u <= accum + p:
                return num

            accum += p

        return None

    return dist

def λ_func(x):
    if (x <= 3):
        return 750
    else:
        return -33.3 * x + 1900.1


def poisson(t_max, λ_max = 2000):
    times = []
    t = 0
    while (t < t_max):
        u = np.random.uniform(0, 1)
        t = t - (1 / λ_max) * np.log(u)
        if (t > t_max): break
        if (np.random.uniform(0, 1) <= λ_func(t) / λ_max):
            times.append(t)

    return times

# 120, 0.7
def poisson_hom(t_max, λ):
    times = []
    t = 0
    while (t < t_max):
        u = np.random.uniform(0, 1)
        t = t - (1 / λ)  * np.log(u)
        if (t > t_max): break
        times.append(t)

    return times
