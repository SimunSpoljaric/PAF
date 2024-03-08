"""Zadatak 4
Napisite funkciju koja kao ulazne parametre prima (x, y) koordinate za dvije tocke. 
Neka ta funkcija na ekran ispisuje jednadzbu pravca koji prolazi kroz te dvije tocke. 
Pozovite tu funkciju u svom programu.
"""

def jednadzba_pravca(T1, T2):
    x1, y1 = T1
    x2, y2 = T2

    if x1 == x2:
        print(f"Jednadžba pravca: x = {x1}")
    else:
        a = (y2 - y1) / (x2 - x1)
        b = y1 - a * x1
        print(f"Jednadžba pravca: y = {a}x + {b}")

jednadzba_pravca((1, 2), (3, 4))


