"""Zadatak 2
Napišite funkciju koja uzima broj iteracija N te N puta zbraja 1/3 pa zatim N puta oduzima 1/3 broju 5.
Ispišite konačni rezultat za 200, 2000 i 20000 iteracija. Objasnite rezultat koji ste dobili.
"""

def funkcija():

    N1 = 200
    N2 = 2000
    N3 = 20000

    R1 = R2 = R3 = 0
    R12 = R22 = R32 = 5


    for i in range(N1):
        R1 = R1 + 1/3
    print("Rezultat za 200 iteracija je: ",R1)

    for i in range(N1):
        R12 = R12 - 1/3
    print("Rezultat za 200 iteracija je: ",R12)

##################################################

    for i in range(N2):
        R2 = R2 + 1/3
    print("Rezultat za 200 iteracija je: ",R2)

    for i in range(N2):
        R22 = R22 - 1/3
    print("Rezultat za 200 iteracija je: ",R22)

##################################################

    for i in range(N3):
        R3 = R3 + 1/3
    print("Rezultat za 200 iteracija je: ",R3)


    for i in range(N3):
        R32 = R32 - 1/3
    print("Rezultat za 200 iteracija je: ",R32)


funkcija()