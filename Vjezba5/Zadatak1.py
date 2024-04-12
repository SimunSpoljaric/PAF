import matplotlib.pyplot as plt
import numpy as np
from calculus import calculus

def cubic_function(x):
    return x ** 3

def trigonometric_function(x):
    return np.sin(x)

def main():
    lower = 0
    upper = 2 * np.pi
    epsilon = 0.1

    cubic_points = calculus.derivative_on_range(cubic_function, lower, upper, epsilon)
    trigonometric_points = calculus.derivative_on_range(trigonometric_function, lower, upper, epsilon)

    x_values_cubic, y_values_cubic = zip(*cubic_points)
    x_values_trig, y_values_trig = zip(*trigonometric_points)

    plt.plot(x_values_cubic, y_values_cubic, label='Cubic Function')
    plt.plot(x_values_trig, y_values_trig, label='Trigonometric Function')
    plt.xlabel('x')
    plt.ylabel("Derivative")
    plt.title('Numerical Derivatives')
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    main()
