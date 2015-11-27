import math
import matplotlib.pyplot as plt

def func_f1(y2):
    return y2

def func_f2(A, B, C, D, omega, t, y1, y2):
    return - (A * y1 * y1 * y1) + (B * y1) - (C * y2) + (D * math.sin(omega * t))

def runge_kutta(A, B, C, D, omega, t_start, y1_start, y2_start, h_step):
    t = t_start
    y1 = y1_start
    y2 = y2_start
    while True:
        K11 = h_step * func_f1(y2)
        K22 = h_step * func_f2(A, B, C, D, omega, t, y1, y2)
        K1 = h_step * func_f2(A, B, C, D, omega, t + h_step, y1 + K11, y2 + K22)
        K2 = h_step * func_f1(y2 + K22)

        y1 = y1 + (0.5 * (K11 + K2))
        y2 = y2 + (0.5 * (K22 + K1))
        t = t + h_step
        yield y1, y2


def duffing(A, B, C, D, omega, start_t, end_t, displacement0, velocity0, n_steps):
    '''
    function: Duffing oscillator
    ----------------------------
    solves the Duffing oscillator for velocity, y2, and displacement, y1

    param A: Duffing oscillator parameter
    param B: Duffing oscillator parameter
    param C: Duffing oscillator parameter
    param D: Duffing oscillator parameter
    param omega: Duffing oscillator temporal frequency parameter
    param start_t: starting time
    param end_t: end time

    return: velocity y2 and displacement y1 as time series
    '''

    interval = end_t - start_t
    h_step = float(interval) / float(n_steps)

    runge_kutta_solver = runge_kutta(A, B, C, D, omega, start_t, displacement0, velocity0, h_step)

    phase_space_x = []
    phase_space_v = []

    for time_step in range(0, n_steps):
        y1, y2 = next(runge_kutta_solver)
        phase_space_x.append(y1)
        phase_space_v.append(y2)

    return phase_space_x, phase_space_v



##test
disp, vel = duffing(1.0, 1.0, 1.0, 0.0, 1.0, 0, 20, 0.5, 1.0, 100)
