"""Zadatak 2
Napišite program u kojem korisnik definira iznos početne brzine v0 u m/s
i kut otklona θ u stupnjevima. Neka
program crta x - y, x - t i y - t graf za prvih 10 sekundi gibanja u dvije dimenzije. 
Diferencijalne jednadžbe rješavajte numerički. Pripazite na oznake i mjerne jedinice x i y osi 
na svim grafovima.
"""

import numpy as np
import matplotlib.pyplot as plt
from math import radians, sin, cos

def numericka_derivacija(y, t):
    
    dydt = np.gradient(y, t)
    return dydt

def gibanje(v0, theta, vrijeme):
    
    theta_rad = radians(theta)

    
    x = 0.0  
    y = 0.0  
    vx = v0 * cos(theta_rad)  
    vy = v0 * sin(theta_rad)  

    
    x_values = [x]
    y_values = [y]
    t_values = [0.0]

    
    for t in np.arange(vrijeme, 10, vrijeme):
        
        ay = -9.81
        
        
        ax = 0.0

        
        vx = vx + ax * vrijeme
        vy = vy + ay * vrijeme

        
        x = x + vx * vrijeme
        y = y + vy * vrijeme

        
        x_values.append(x)
        y_values.append(y)
        t_values.append(t)

    return x_values, y_values, t_values

def main():
    
    v0 = float(input("Unesite iznos početne brzine (u m/s): "))
    theta = float(input("Unesite kut otklona (u stupnjevima): "))
    vrijeme = float(input("Unesite vremenski korak (u sekundama): "))

    
    x_values, y_values, t_values = gibanje(v0, theta, vrijeme)

    
    plt.figure(figsize=(15, 5))

    # x - y graf
    plt.subplot(1, 3, 1)
    plt.plot(x_values, y_values, 'b-')
    plt.title('x - y graf')
    plt.xlabel('x (m)')
    plt.ylabel('y (m)')

    # x - t graf
    plt.subplot(1, 3, 2)
    plt.plot(t_values, x_values, 'r-')
    plt.title('x - t graf')
    plt.xlabel('Vrijeme (s)')
    plt.ylabel('x (m)')

    # y - t graf
    plt.subplot(1, 3, 3)
    plt.plot(t_values, y_values, 'g-')
    plt.title('y - t graf')
    plt.xlabel('Vrijeme (s)')
    plt.ylabel('y (m)')

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()

