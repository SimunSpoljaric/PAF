"""Zadatak 5
Unaprijedite kod iz prethodnog zadatka koristeci modul matplotlib.pyplot tako da nacrtate unesene 
koordinate i pravac koji prolazi kroz njih. 
Ponudite u funkciji opciju da se graf prikaze na ekranu ili da se spremi
kao PDF. Dopustite korisniku da bira ime pod kojim ce se spremiti graf.
"""

import matplotlib.pyplot as plt

def unos_tocke(oznaka):
    while True:
        try:
            x = float(input(f"Unesite x koordinatu točke {oznaka}: "))
            y = float(input(f"Unesite y koordinatu točke {oznaka}: "))
            return x, y
        except ValueError:
            print("Neispravan unos. Molimo unesite decimalni broj.")

def jednadzba_pravca(tocka1, tocka2, prikazi_graf=True, ime_pdf=None):
    x1, y1 = tocka1
    x2, y2 = tocka2

    if x1 == x2:
        print(f"Jednadžba pravca: x = {x1}")
        a = None
        b = None
    else:
        a = (y2 - y1) / (x2 - x1)
        b = y1 - a * x1
        print(f"Jednadžba pravca: y = {a}x + {b}")

    if prikazi_graf:
        plt.figure()
        plt.plot([x1, x2], [y1, y2], marker='o', label='Točke')
        if a is not None:
            x_values = [x1, x2]
            y_values = [a * x + b for x in x_values]
            plt.plot(x_values, y_values, label=f'Pravac: y = {a}x + {b}')
        plt.xlabel('x')
        plt.ylabel('y')
        plt.title('Graf točaka i pravca')
        plt.legend()
        if ime_pdf:
            plt.savefig(f'{ime_pdf}.pdf')
            print(f"Graf je spremljen kao '{ime_pdf}.pdf'")
        else:
            plt.show()

def main():
    print("Unesite koordinate prve točke:")
    tocka1 = unos_tocke("1")

    print("\nUnesite koordinate druge točke:")
    tocka2 = unos_tocke("2")

    print("\nIzračunavanje jednadžbe pravca...")
    jednadzba_pravca(tocka1, tocka2, prikazi_graf=True, ime_pdf=input("Unesite ime PDF datoteke za spremanje (prazno za prikaz na ekranu): ").strip())

if __name__ == "__main__":
    main()
