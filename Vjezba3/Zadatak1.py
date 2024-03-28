"""Zadatak 1
(a) Oduzmite 5.0 i 4.935. Koji rezultat očekujete? Koji rezultat dobijete koristeći Python? Objasnite.
(b) Provjerite iznosi li suma brojeva 0.1, 0.2 i 0.3 broj 0.6. Objasnite rezultat koji ste dobili.
"""


#(a)

a = 5.0
b = 4.935
ocekivano = 0.065
python = a - b

print("(a)\n", python)

"""Ovo se događa zbog načina na koji računalni sustavi pohranjuju decimalne brojeve 
s pomičnim zarezom. Budući da računalni sustavi koriste binarni sustav za pohranu brojeva, 
neki decimalni brojevi nemaju točan zapis u binarnom sustavu, što može rezultirati malim 
greškama u točnosti pri računanju."""

#(b)

x = 0.1
y = 0.2
z = 0.3

uk = x + y + z

print("(b)\n",uk)

"""Ovo se događa zbog nesavršenosti u pohrani decimalnih brojeva u računalima. 
Brojevi poput 0.1, 0.2 i 0.3 nemaju točan binarni ekvivalent koji se može pohraniti u računalu, 
pa se prilikom izvođenja aritmetičkih operacija može doći do malih grešaka u točnosti.
Stoga, iako bismo očekivali da je rezultat 0.6, zbog nesavršenosti pohrane decimalnih brojeva 
u računalima, Python vraća 0.6000000000000001."""
