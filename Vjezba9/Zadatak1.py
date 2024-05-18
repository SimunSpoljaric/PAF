"""Zadatak 1
Napišite program koji crta putanju dvije čestice koje međudjeluju gravitacijskom silom. Provjerite valjanost
programa na primjeru Sunca i Zemlje. Promatrajte problem u dvije dimenzije i koristite Euler-ovu metodu
za rješavanje vezanih diferencijalnih jednadžbi.
U početnom trenutku Sunce se nalazi u ishodištu i nema početnu brzinu, a Zemlja je udaljena jednu astronomsku jedinicu (1 a.u. = 1.486 · 1011 m) i ima početnu okomitu komponentu brzine v⊥ = 29783 m
s
.
Masa Sunca je MS = 1.989 · 1030 kg, masa Zemlje je MZ = 5.9742 · 1024 kg, gravitacijska konstanta je
G = 6.67408 · 10−11 Nm2
kg2 , a jedna godina ima 365.242 dana.
"""


import numpy as np
import matplotlib.pyplot as plt

class GravitatingBody:
    def __init__(self, mass, position, velocity):
        self.mass = mass
        self.position = np.array(position, dtype=float)
        self.velocity = np.array(velocity, dtype=float)
        self.force = np.zeros(2, dtype=float)

    def update_force(self, other, G):
        # Izračunaj gravitacijsku silu između dva tijela
        r_vec = other.position - self.position
        r_mag = np.linalg.norm(r_vec)
        if r_mag != 0:
            r_hat = r_vec / r_mag
            self.force = G * self.mass * other.mass / r_mag**2 * r_hat

    def update_position_velocity(self, delta_t):
        # Ažuriraj brzinu i položaj pomoću Eulerove metode
        acceleration = self.force / self.mass
        self.velocity += acceleration * delta_t
        self.position += self.velocity * delta_t

def simulate_gravity(bodies, G, total_time, delta_t):
    positions = {body: [] for body in bodies}
    num_steps = int(total_time / delta_t)
    
    for _ in range(num_steps):
        # Resetiraj sile
        for body in bodies:
            body.force = np.zeros(2, dtype=float)
        
        # Izračunaj nove sile
        for i, body in enumerate(bodies):
            for other in bodies:
                if body != other:
                    body.update_force(other, G)
        
        # Ažuriraj položaj i brzinu
        for body in bodies:
            body.update_position_velocity(delta_t)
            positions[body].append(body.position.copy())
    
    return positions

def plot_trajectories(positions):
    plt.figure(figsize=(8, 8))
    for body, pos in positions.items():
        pos = np.array(pos)
        plt.plot(pos[:, 0], pos[:, 1], label=f"Body {id(body)}")
    
    plt.xlabel("x (m)")
    plt.ylabel("y (m)")
    plt.title("Trajectories of Gravitating Bodies")
    plt.legend()
    plt.grid(True)
    plt.axis('equal')
    plt.show()

def main():
    # Konstantni parametri
    G = 6.67408e-11  # Gravitacijska konstanta (Nm^2/kg^2)
    masa_sunca = 1.989e30  # kg
    masa_zemlje = 5.9742e24  # kg
    AU = 1.486e11  # Astronomska jedinica (m)
    pocetna_brzina_zemlje = 29783  # m/s
    godina_u_sec = 365.242 * 24 * 3600  # sekundi u jednoj godini

    # Inicijalni uvjeti
    sunce = GravitatingBody(masa_sunca, [0, 0], [0, 0])
    zemlja = GravitatingBody(masa_zemlje, [AU, 0], [0, pocetna_brzina_zemlje])

    # Simulacija
    totalno_vrijeme = godina_u_sec  # Simuliraj jednu godinu
    delta_t = 24 * 3600  # Korak vremena (jedan dan)

    positions = simulate_gravity([sunce, zemlja], G, totalno_vrijeme, delta_t)

    # Crtanje putanja
    plot_trajectories(positions)

if __name__ == "__main__":
    main()
