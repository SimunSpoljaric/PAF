class HarmonicOscillator:
    def __init__(self, masa, konstanta_opruge, pocetni_polozaj, pocetna_brzina):
        self.masa = masa
        self.konstanta_opruge = konstanta_opruge
        self.polozaj = pocetni_polozaj
        self.brzina = pocetna_brzina

    def azuriraj(self, delta_t):
        ubrzanje = -self.konstanta_opruge * self.polozaj / self.masa
        self.brzina += ubrzanje * delta_t
        self.polozaj += self.brzina * delta_t

    def dohvati_polozaj(self):
        return self.polozaj

    def dohvati_brzinu(self):
        return self.brzina

    def dohvati_ubrzanje(self):
        return -self.konstanta_opruge * self.polozaj / self.masa
    

    def period_titranja(self, delta_t, epsilon=0.01):
        # Postavljamo početni položaj i brzinu
        self.polozaj = 0
        self.brzina = 0
        # Inicijaliziramo brojač titranja i vremenski brojač
        brojac_titranja = 0
        vremenski_brojac = 0
        while True:
            # Ažuriramo stanje oscilatora
            self.azuriraj(delta_t)
            # Ako je promjena smjera (priješli smo nula)
            if self.polozaj * (self.polozaj - self.brzina * delta_t) < 0:
                # Povećavamo brojač titranja
                brojac_titranja += 1
                # Ako smo prešli epsilon nakon nule, to je period titranja
                if abs(self.polozaj) < epsilon:
                    # Povrat perioda titranja
                    return 2 * brojac_titranja * delta_t
            # Povećavamo vremenski brojač
            vremenski_brojac += delta_t

    def period_titranja_test(self, delta_t_values):
        periodi = []
        for delta_t in delta_t_values:
            period = self.period_titranja(delta_t)
            periodi.append(period)
        return periodi
