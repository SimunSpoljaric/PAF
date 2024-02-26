"""Zadatak 3
Napisite program koji ce korisnika traziti da upise (x, y) koordinate za dvije tocke. Ako korisnik pogrijesi prilikom unosa koordinate opomenite ga da ponovi upis. 
Nakon sto je korisnik uspjesno upisao dvije koordinate ispisite na ekran jednadzbu pravca koji prolazi kroz te dvije tocke."""

def unos_tocke():
    while True:
        try:
            x = int(input("Unesite x koordinatu tocke: "))
            y = int(input("Unesite y koordinatu tocke: "))
            return x, y
        except ValueError:
            print("Neispravan unos. Molimo unesite decimalni broj.")

def jednadzba_pravca(T1, T2):
    x1, y1 = T1
    x2, y2 = T2

    if x1 == x2:
        print("Jednadzba pravca: x = {}".format(x1))
    else:
        a = (y2 - y1) / (x2 - x1)
        b = y1 - a * x1
        print("Jednadzba pravca: y = {}x + {}".format(a, b))

def main():
    print("Unesite koordinate prve tocke:")
    tocka1 = unos_tocke()

    print("\nUnesite koordinate druge tocke:")
    tocka2 = unos_tocke()

    print("\nIzracunavanje jednadzbe pravca...")
    jednadzba_pravca(tocka1, tocka2)

if __name__ == "__main__":
    main()

