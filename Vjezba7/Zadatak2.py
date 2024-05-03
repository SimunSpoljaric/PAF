'''Zadatak 2
Klasi Projectile dodajte mogućnost rješavanja problema uz pomoć Runge-Kutta metode 4. reda. Usporedite
putanje projektila preko Euler-ove i Runge-Kutta metode za ∆t = 0.01.'''


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
    def update_euler(self, delta_t):
        
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

    def update_runge_kutta(self, delta_t):
        
        k1_x = self.vx[-1]
        
        k1_y = self.vy[-1]
        
        k1_vx = -self.air_resistance_coefficient * self.vx[-1] / self.mass
        
        k1_vy = -self.air_resistance_coefficient * self.vy[-1] / self.mass - 9.81

        
        k2_x = self.vx[-1] + k1_vx * delta_t / 2
        
        k2_y = self.vy[-1] + k1_vy * delta_t / 2
        
        k2_vx = -self.air_resistance_coefficient * k2_x / self.mass
        
        k2_vy = -self.air_resistance_coefficient * k2_y / self.mass - 9.81

        
        k3_x = self.vx[-1] + k2_vx * delta_t / 2
        
        k3_y = self.vy[-1] + k2_vy * delta_t / 2
        
        k3_vx = -self.air_resistance_coefficient * k3_x / self.mass
        
        k3_vy = -self.air_resistance_coefficient * k3_y / self.mass - 9.81

        
        k4_x = self.vx[-1] + k3_vx * delta_t
        
        k4_y = self.vy[-1] + k3_vy * delta_t
        
        k4_vx = -self.air_resistance_coefficient * k4_x / self.mass
        
        k4_vy = -self.air_resistance_coefficient * k4_y / self.mass - 9.81

        
        new_vx = self.vx[-1] + delta_t / 6 * (k1_vx + 2 * k2_vx + 2 * k3_vx + k4_vx)
        new_vy = self.vy[-1] + delta_t / 6 * (k1_vy + 2 * k2_vy + 2 * k3_vy + k4_vy)

    
        new_x = self.x[-1] + delta_t / 6 * (k1_x + 2 * k2_x + 2 * k3_x + k4_x)
        new_y = self.y[-1] + delta_t / 6 * (k1_y + 2 * k2_y + 2 * k3_y + k4_y)

    
        self.vx.append(new_vx)
        self.vy.append(new_vy)
        self.x.append(new_x)
        self.y.append(new_y)

    def simulate_euler(self, total_time, delta_t):
    
        self.dt = delta_t

    
        current_time = 0
        while current_time <= total_time:
            self.update_euler(delta_t)
            current_time += delta_t

    def simulate_runge_kutta(self, total_time, delta_t):
    
        self.dt = delta_t

        
        current_time = 0
        while current_time <= total_time:
            self.update_runge_kutta(delta_t)
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
    delta_t = 0.01  
    projektil.simulate_euler(totalno_vrijeme, delta_t)
    projektil.plot_trajectory()

    
    projektil.simulate_runge_kutta(totalno_vrijeme, delta_t)
    projektil.plot_trajectory()

if __name__ == "__main__":
    main()
