import matplotlib.pyplot as plt
import numpy as np
from math import radians, sin, cos

class Particle:
    def __init__(self, v0, kut_otklona, x0, y0):
        self.v0 = v0  
        self.kut_otklona = kut_otklona  
        self.x0 = x0  
        self.y0 = y0  
        self.reset()

    def reset(self):
        self.trenutno_vrijeme = 0
        self.x = self.x0
        self.y = self.y0
        self.x_values = [self.x]
        self.y_values = [self.y]

    def __move(self, delta_t):
        theta = radians(self.kut_otklona)
        vx = self.v0 * cos(theta)
        vy = self.v0 * sin(theta) - 9.81 * self.trenutno_vrijeme
        self.x += vx * delta_t
        self.y += vy * delta_t
        self.x_values.append(self.x)
        self.y_values.append(self.y)
        self.trenutno_vrijeme += delta_t

    def range(self):
        while self.y >= 0:
            self.__move(0.01)
        return self.x

    def plot_trajectory(self):
        plt.plot(self.x_values, self.y_values)
        plt.xlabel('x (m)')
        plt.ylabel('y (m)')
        plt.title('Putanja čestice')
        plt.grid(True)
        plt.show()

    def relative_error(self, delta_t):
        self.reset()  # Ponovno postavljanje početnih uvjeta
        self.__move(delta_t)  # Numeričko rješavanje s odabranim vremenskim korakom

        # Analitičko rješenje
        theta = radians(self.kut_otklona)
        t_flight = 2 * self.v0 * sin(theta) / 9.81
        x_analytical = self.v0 * cos(theta) * t_flight

        # Relativna pogreška
        x_numerical = self.x
        relative_error = abs(x_analytical - x_numerical) / x_analytical
        return relative_error