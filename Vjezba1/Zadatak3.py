'''Zadatak 3
Napišite program koji će korisnika tražiti da upiše (x, y) koordinate za dvije točke. Ako korisnik pogriješi prilikom unosa koordinate opomenite ga da ponovi upis. Nakon što je korisnik uspješno upisao dvije koordinate
ispišite na ekran jednadžbu pravca koji prolazi kroz te dvije točke.
'''

def unos_tocke():
    while True:
        try:
            x = int(input("Unesite x koordinatu točke: "))
            y = int(input("Unesite y koordinatu točke: "))
            return x, y
        except ValueError:
            print("Neispravan unos. Molimo unesite decimalni broj.")

def jednadzba_pravca(T1, T2):
    x1, y1 = T1
    x2, y2 = T2

    if x1 == x2:
        print(f"Jednadžba pravca: x = {x1}")
    else:
        a = (y2 - y1) / (x2 - x1)
        b = y1 - a * x1
        print(f"Jednadžba pravca: y = {a}x + {b}")

def main():
    print("Unesite koordinate prve točke:")
    tocka1 = unos_tocke()

    print("\nUnesite koordinate druge točke:")
    tocka2 = unos_tocke()

    print("\nIzračunavanje jednadžbe pravca...")
    jednadzba_pravca(tocka1, tocka2)

if __name__ == "__main__":
    main()
