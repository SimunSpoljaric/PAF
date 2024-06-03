import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random
import math

class Kuglica:
    def __init__(self, x=0, y=0, brzina=1, kut=None):
        self.x = x
        self.y = y
        self.brzina = brzina
        if kut is None:
            self.kut = random.uniform(0, 2 * math.pi)  # Nasumičan početni kut u radijanima
        else:
            self.kut = kut  # Kut kretanja u radijanima

    def pomakni(self, granica_lijevo, granica_desno, granica_dolje, granica_gore):
        # Provjera udara u granice i promjena kuta kretanja
        if self.x + self.brzina * math.cos(self.kut) > granica_desno or self.x + self.brzina * math.cos(self.kut) < granica_lijevo:
            self.kut = math.pi - self.kut  # Odbijanje od vertikalnih granica
        if self.y + self.brzina * math.sin(self.kut) > granica_gore or self.y + self.brzina * math.sin(self.kut) < granica_dolje:
            self.kut = -self.kut  # Odbijanje od horizontalnih granica

        self.x += self.brzina * math.cos(self.kut)
        self.y += self.brzina * math.sin(self.kut)

def azuriraj_okvir(num, kuglica, linija, granica_lijevo, granica_desno, granica_dolje, granica_gore):
    kuglica.pomakni(granica_lijevo, granica_desno, granica_dolje, granica_gore)
    linija.set_data([kuglica.x], [kuglica.y])
    return linija,

def animiraj_gibanje_kuglice(kuglica, trajanje, interval, granica_lijevo, granica_desno, granica_dolje, granica_gore):
    fig, ax = plt.subplots()
    ax.set_xlim(granica_lijevo, granica_desno)
    ax.set_ylim(granica_dolje, granica_gore)

    linija, = ax.plot([], [], 'ro')
    
    # Izračun broja frameova i intervala za postizanje željenog trajanja i FPS-a
    broj_frameova = int(trajanje / (interval / 1000))

    ani = animation.FuncAnimation(fig, azuriraj_okvir, frames=broj_frameova,
                                  fargs=(kuglica, linija, granica_lijevo, granica_desno, granica_dolje, granica_gore), interval=interval, blit=True)

    plt.show()

# Primjer korištenja
if __name__ == "__main__":
    kuglica = Kuglica()
    trajanje_animacije = 10  # u sekundama
    interval_animacije = 1000 / 60  # u milisekundama za 60 FPS
    granica_lijevo = 0
    granica_desno = 10
    granica_dolje = -1
    granica_gore = 10

    animiraj_gibanje_kuglice(kuglica, trajanje_animacije, interval_animacije, granica_lijevo, granica_desno, granica_dolje, granica_gore)
