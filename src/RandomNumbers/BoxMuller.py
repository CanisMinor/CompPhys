import numpy as np
import math

def uniform_distribution(A, B, M):
    x_old = 2.1
    while True:
        x_old = (A * x_old + B) % M
        yield x_old/ M

def normal_distribution(generate_random, mu, sigma):
    while True:
        x_first = next(generate_random)
        x_second = next(generate_random)
        rand_gauss = sigma * math.sqrt(-2.0 * math.log(1.0 - x_second)) * math.cos(2.0 * math.pi * x_first) + mu
        yield rand_gauss




