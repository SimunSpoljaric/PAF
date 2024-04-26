"""Zadatak 1
Napišite modul "harmonic_oscillator.py" koji će sadržavati klasu HarmonicOscillator s raznim metodama
potrebnim za opis gibanja jednostavnog harmoničkog oscilatora u jednoj dimenziji. Koristeći razvijeni modul
nacrtajte x - t, v - t i a - t graf za neke proizvoljno odabrane početne parametre. Ispitajte preciznost
numeričkog rješenja za različite korake ∆t."""

import matplotlib.pyplot as plt
from harmonic_oscillator import HarmonicOscillator

def main():
    masa = 1  # kg
    konstanta_opruge = 1  # N/m
    pocetni_polozaj = 1  # m
    pocetna_brzina = 0  # m/s
    delta_t_vrijednosti = [0.1, 0.01, 0.001]

    for delta_t in delta_t_vrijednosti:
        oscilator = HarmonicOscillator(masa, konstanta_opruge, pocetni_polozaj, pocetna_brzina)
        polozaji = []
        brzine = []
        ubrzanja = []
        vremena = []
        vrijeme = 0

        while vrijeme <= 10:
            polozaji.append(oscilator.dohvati_polozaj())
            brzine.append(oscilator.dohvati_brzinu())
            ubrzanja.append(oscilator.dohvati_ubrzanje())
            vremena.append(vrijeme)
            oscilator.azuriraj(delta_t)
            vrijeme += delta_t

        plt.figure(figsize=(12, 4))

        plt.subplot(131)
        plt.plot(vremena, polozaji)
        plt.xlabel('Vrijeme (s)')
        plt.ylabel('Polozaj (m)')
        plt.title('x - t Graf (Δt={})'.format(delta_t))

        plt.subplot(132)
        plt.plot(vremena, brzine)
        plt.xlabel('Vrijeme (s)')
        plt.ylabel('Brzina (m/s)')
        plt.title('v - t Graf (Δt={})'.format(delta_t))

        plt.subplot(133)
        plt.plot(vremena, ubrzanja)
        plt.xlabel('Vrijeme (s)')
        plt.ylabel('Ubrzanje (m/s^2)')
        plt.title('a - t Graf (Δt={})'.format(delta_t))

        plt.tight_layout()
        plt.show()

if __name__ == "__main__":
    main()
