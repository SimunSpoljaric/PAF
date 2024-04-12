import matplotlib.pyplot as plt
import numpy as np
from calculus import calculus

def f(x):
    return np.sin(x)

def main():
    lower = 0
    upper = np.pi
    num_partitions_values = [10, 50, 100, 200]

    analytical_integral = 2  # Analitički rezultat za integral od 0 do pi od sin(x)

    rectangle_lower_sums = []
    rectangle_upper_sums = []
    trapezoidal_integrals = []

    for num_partitions in num_partitions_values:
        lower_sum, upper_sum = calculus.rectangle_rule(f, lower, upper, num_partitions)
        rectangle_lower_sums.append(lower_sum)
        rectangle_upper_sums.append(upper_sum)
        trapezoidal_integral = calculus.trapezoidal_rule(f, lower, upper, num_partitions)
        trapezoidal_integrals.append(trapezoidal_integral)

    plt.plot(num_partitions_values, rectangle_lower_sums, label='Rectangle Lower Sum')
    plt.plot(num_partitions_values, rectangle_upper_sums, label='Rectangle Upper Sum')
    plt.plot(num_partitions_values, trapezoidal_integrals, label='Trapezoidal Integral')
    plt.axhline(y=analytical_integral, color='r', linestyle='--', label='Analytical Integral')
    plt.xlabel('Number of Partitions')
    plt.ylabel('Integral Value')
    plt.title('Numerical Integration')
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    main()
