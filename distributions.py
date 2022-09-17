import random
import numpy as np

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

def exponential(l):
    u = random.random()
    return - (1 / l)  * np.log(u)

def lambda_f(t):
    if t < 4:
        return 5
    
    return 20 - (t - 4) / 1

def poisson_var(t_max):

    t = 0
    tiempos = []
    while True:

        u = random.random()
        t = t - np.log(1 - u) / lambda_f(t)

        if t > t_max:
            break
        else:
            tiempos.append(t)

    return tiempos

def arrival_times(t_max):
    # Tomo la distribucion, la modifico para que sus valores esten entre 0 y 12
    k = 22
    times = [n * t_max / k for n in poisson_var(k)]

    samples = min(46, len(times))

    # Ahora limito la cantidad de tutorias para no hayan mas de 46 (el maximo historico)
    return sorted(random.sample(times, samples))
