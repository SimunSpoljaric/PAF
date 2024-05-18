"""Zadatak 1
Napišite program koji crta putanju nabijene čestice u konstantnom električnom i magnetnom polju. Demonstrirajte valjanost putanje za slučaj nabijene čestice koja se giba u konstatnom magnetnom polju B⃗ = (0, 0, B)
i ima sve tri komponente početne brzine različite od 0. Kako se u tom slučaju giba elektron, a kako pozitron?"""



import numpy as np
import matplotlib.pyplot as plt

class ChargedParticle:
    def __init__(self, charge, mass, initial_position, initial_velocity, electric_field, magnetic_field):
        self.charge = charge
        self.mass = mass
        self.position = np.array(initial_position, dtype=float)
        self.velocity = np.array(initial_velocity, dtype=float)
        self.electric_field = np.array(electric_field, dtype=float)
        self.magnetic_field = np.array(magnetic_field, dtype=float)
        self.positions = [self.position.copy()]

    def lorentz_force(self, velocity):
        return self.charge * (self.electric_field + np.cross(velocity, self.magnetic_field))

    def update_runge_kutta(self, delta_t):
        # Runge-Kutta 4. reda za poziciju i brzinu
        k1_v = delta_t * self.lorentz_force(self.velocity) / self.mass
        k1_r = delta_t * self.velocity

        k2_v = delta_t * self.lorentz_force(self.velocity + k1_v / 2) / self.mass
        k2_r = delta_t * (self.velocity + k1_v / 2)

        k3_v = delta_t * self.lorentz_force(self.velocity + k2_v / 2) / self.mass
        k3_r = delta_t * (self.velocity + k2_v / 2)

        k4_v = delta_t * self.lorentz_force(self.velocity + k3_v) / self.mass
        k4_r = delta_t * (self.velocity + k3_v)

        self.velocity += (k1_v + 2 * k2_v + 2 * k3_v + k4_v) / 6
        self.position += (k1_r + 2 * k2_r + 2 * k3_r + k4_r) / 6

        self.positions.append(self.position.copy())

    def simulate(self, total_time, delta_t):
        num_steps = int(total_time / delta_t)
        for _ in range(num_steps):
            self.update_runge_kutta(delta_t)

    def plot_trajectory(self):
        positions = np.array(self.positions)
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        ax.plot(positions[:, 0], positions[:, 1], positions[:, 2])
        ax.set_xlabel('X (m)')
        ax.set_ylabel('Y (m)')
        ax.set_zlabel('Z (m)')
        ax.set_title('Trajectory of Charged Particle')
        plt.show()

def main():
    # Parametri čestice
    q_electron = -1.6e-19  # Coulomb
    q_positron = 1.6e-19  # Coulomb
    m = 9.11e-31  # kg (massa elektrona/pozitrona)
    
    # Početni uvjeti
    initial_position = [0, 0, 0]  # m
    initial_velocity = [1e6, 1e6, 1e6]  # m/s
    
    # Električno i magnetno polje
    electric_field = [0, 0, 0]  # V/m
    magnetic_field = [0, 0, 1]  # T

    # Vremenski parametri
    total_time = 1e-8  # s
    delta_t = 1e-11  # s

    # Elektron
    electron = ChargedParticle(q_electron, m, initial_position, initial_velocity, electric_field, magnetic_field)
    electron.simulate(total_time, delta_t)
    electron.plot_trajectory()

    # Pozitron
    positron = ChargedParticle(q_positron, m, initial_position, initial_velocity, electric_field, magnetic_field)
    positron.simulate(total_time, delta_t)
    positron.plot_trajectory()

if __name__ == "__main__":
    main()
