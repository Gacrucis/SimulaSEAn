import random

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