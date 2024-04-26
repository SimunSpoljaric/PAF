"""Zadatak 2
Razvijenom modulu dodajte metodu koja za zadane početne uvijete numerički računa period titranja. 
Ispitajte preciznost metode u ovisnosti o veličini koraka ∆t."""

import matplotlib.pyplot as plt
from harmonic_oscillator import HarmonicOscillator

def main():
    masa = 1  # kg
    konstanta_opruge = 1  # N/m
    pocetni_polozaj = 1  # m
    pocetna_brzina = 0  # m/s
    delta_t_values = [0.1, 0.01, 0.001, 0.0001]

    oscillator = HarmonicOscillator(masa, konstanta_opruge, pocetni_polozaj, pocetna_brzina)
    periodi = oscillator.period_titranja_test(delta_t_values)

    plt.plot(delta_t_values, periodi, marker='o')
    plt.xlabel('Veličina koraka (∆t)')
    plt.ylabel('Period titranja')
    plt.title('Preciznost metode u ovisnosti o veličini koraka ∆t')
    plt.xscale('log')
    plt.yscale('log')
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    main()
