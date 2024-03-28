"""(a) Napišite program arithm.py koji računa aritmetičku sredinu i standardnu devijaciju za 10 točaka. 
Formula za aritmetičku sredinu je dana u 1, a za standardnu devijaciju u 2."""

import math



def aritmeticka_sredina (x):

    
    N = len(x)

    xi = sum(x)

    AS =  xi/N

    print ("Aritmeticka sredina je: ", AS)


def devijacija(y):

    
    N = len(y)
    yi = sum(y)
    AS =  yi/N
    yd = 0

    for i in range(N):

        yd = yd + (y[i] - AS)**2

        n = N*(N-1)


    s = yd/n
    
    SD = math.sqrt(yd / (N-1)) #NAPOMENA => U dokumentu vašem Vjezbe3 u formuli za devijaciju u nazivniku
                                #stoji N(N-1), a na internetu samo N-1, ja sam stavio kako je na internetu

    print ("Standarna devijacija je: ", SD)


