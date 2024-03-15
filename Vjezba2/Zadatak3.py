"""Zadatak 3
Napišite svoj modul "kinematika.py" koji će sadržavati funkcije jednoliko_gibanje() i kosi_hitac(). Neka
funkcije kao ulazne parametre primaju sve podatke neophodne za izračun (iznos sile, iznos brzine, 
kut otklona, masa, vrijeme, ...) i neka crtaju iste grafove kao i u prošlim zadatcima. 
Napravite novi program u kojem ćete uključiti razvijeni modul i pozvati obe funkcije."""


import numpy as np
import matplotlib.pyplot as plt
from math import radians, sin, cos

def derivacija(y, t):
    
    dydt = np.gradient(y, t)
    return dydt

def jednoliko_gibanje(v0, theta, vrijeme):
    
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

def kosi_hitac(v0, theta, vrijeme):
    
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
