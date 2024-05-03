'''Zadatak 1
Napišite kod koji sadrži klasu Projectile koja ima implementirane metode za simuliranje kosog hitca u dvije
dimenzije s otporom zraka. Testirajte za koji korak ∆t Euler-ova metoda daje dovoljno precizno numeričko
rješenje koje na x - y grafu nema naznake ne-fizikalnog gibanja.
'''



import numpy as np
import matplotlib.pyplot as plt

class Projectile:
    def __init__(self, mass, initial_velocity, angle, air_resistance_coefficient):
        self.mass = mass
        self.initial_velocity = initial_velocity
        self.angle = np.radians(angle)  
        self.air_resistance_coefficient = air_resistance_coefficient
        self.x = [0.0]  
        self.y = [0.0]  
        self.vx = [initial_velocity * np.cos(self.angle)]  
        self.vy = [initial_velocity * np.sin(self.angle)]  
        self.dt = None  

    def update(self, delta_t):
        
        ax = -self.air_resistance_coefficient * self.vx[-1] / self.mass
        ay = -self.air_resistance_coefficient * self.vy[-1] / self.mass - 9.81 

        
        new_vx = self.vx[-1] + ax * delta_t
        new_vy = self.vy[-1] + ay * delta_t

       
        new_x = self.x[-1] + new_vx * delta_t
        new_y = self.y[-1] + new_vy * delta_t

        
        self.vx.append(new_vx)
        self.vy.append(new_vy)
        self.x.append(new_x)
        self.y.append(new_y)

    def simulate(self, total_time, delta_t):
        
        self.dt = delta_t

        
        current_time = 0
        while current_time <= total_time:
            self.update(delta_t)
            current_time += delta_t

    def plot_trajectory(self):
        plt.plot(self.x, self.y)
        plt.xlabel('x (m)')
        plt.ylabel('y (m)')
        plt.title('Trajectory of the Projectile')
        plt.grid(True)
        plt.show()

def main():
    
    masa = 0.1  
    pocetna_brzina = 30 
    kut_otklona = 45 
    otpor_zraka = 0.01  

    
    projektil = Projectile(masa, pocetna_brzina, kut_otklona, otpor_zraka)

    
    totalno_vrijeme = 10  
    delta_t_values = [0.01, 0.001, 0.0001, 0.00001]

    for delta_t in delta_t_values:
        projektil.simulate(totalno_vrijeme, delta_t)
        projektil.plot_trajectory()

if __name__ == "__main__":
    main()
