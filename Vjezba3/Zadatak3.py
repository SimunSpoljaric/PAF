"""Zadatak 3
(a) Napišite program arithm.py koji računa aritmetičku sredinu i standardnu devijaciju za 10 točaka. 
Formula za aritmetičku sredinu je dana u 1, a za standardnu devijaciju u 2.
(b) Napišite program pod (a) koristeći gotove module.
"""

from arthm import aritmeticka_sredina
from arthm import devijacija


x = [3, 5, 7, 9, 11, 13, 15, 17, 19, 21]
y = [3, 5, 7, 9, 11, 13, 15, 17, 19, 21]

aritmeticka_sredina(x)
devijacija(y)