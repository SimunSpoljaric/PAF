"""Zadatak 1
Napisite program u kojem korisnik definira iznos sile u N i masu cestice u kg, 
a program crta x - t, v - t i a - t graf za prvih 10 sekundi jednolikog gibanja u jednoj dimenziji.
Diferencijalne jednadzbe rjesavajte numericki. 
Pripazite na oznake i mjerne jedinice x i y osi na svim grafovima.
"""

import numpy as np
import matplotlib.pyplot as plt

def numericka_derivacija(y, t):
    
    dydt = np.gradient(y, t)
    return dydt

def jednoliko_gibanje(F, m, t):
    
    x = 0.0  
    v = 0.0  
    a = F / m  

    
    x_values = [x]
    v_values = [v]
    a_values = [a]
    t_values = [0.0]

    
    for t in np.arange(t, 10, t):
        
        x = x + v * t
        
        v = v + a * t
        
        a = F / m
        
        x_values.append(x)
        v_values.append(v)
        a_values.append(a)
        t_values.append(t)

    return x_values, v_values, a_values, t_values

def main():
    
    F = float(input("Unesite iznos sile (u N): "))
    m = float(input("Unesite masu čestice (u kg): "))
    t = float(input("Unesite vrijeme (u sekundama): "))


    x_values, v_values, a_values, t_values = jednoliko_gibanje(F, m, t)

    plt.figure(figsize=(15, 5))

    # x - t graf
    plt.subplot(1, 3, 1)
    plt.plot(t_values, x_values, 'b-')
    plt.title('x - t graf')
    plt.xlabel('Vrijeme (s)')
    plt.ylabel('Položaj (m)')

    # v - t graf
    plt.subplot(1, 3, 2)
    plt.plot(t_values, v_values, 'r-')
    plt.title('v - t graf')
    plt.xlabel('Vrijeme (s)')
    plt.ylabel('Brzina (m/s)')

    # a - t graf
    plt.subplot(1, 3, 3)
    plt.plot(t_values, a_values, 'g-')
    plt.title('a - t graf')
    plt.xlabel('Vrijeme (s)')
    plt.ylabel('Ubrzanje (m/s^2)')

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()

