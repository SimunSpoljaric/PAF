import matplotlib.pyplot as plt
import numpy as np
from particle import Particle

def main():
    v0 = 10  
    kut_otklona = 60  

    delta_t_values = np.linspace(0.01, 1, 100)
    relative_errors = []

    for delta_t in delta_t_values:
        particle = Particle(v0, kut_otklona, 0, 0)
        relative_error = particle.relative_error(delta_t)
        relative_errors.append(relative_error)

    plt.plot(delta_t_values, relative_errors)
    plt.xlabel('Vremenski korak (∆t)')
    plt.ylabel('Relativna pogreška')
    plt.title('Ovisnost relativne pogreške o vremenskom koraku')
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    main()
