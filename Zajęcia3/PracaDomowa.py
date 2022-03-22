import random

# zad2
ls1 = [random.randrange(0, 100) for x in range(0, 11)]
ls2 = [x for x in ls1 if x % 2 == 0]

print(ls1)
print(ls2)

# zad3
slownik = {
    "Truskawki": "G",
    "Ziemniaki": "KG",
    "Bułeczki": "Szt",
    "Jabłka": "Szt"
}

listaP = [key for key, value in slownik.items() if value == "Szt"]
print(listaP)


# zad4
def Sprawdz(a, b, c):
    return a ** 2 + b ** 2 == c ** 2


print(Sprawdz(6, 8, 10))


# zad5
def trapez_pole(a=8, b=2, h=7):
    return ((a + b) / 2) * h


print(trapez_pole(8, 2, 7))


# zad6

def il_elem(z, y, q):
    iloczyn = 1
    for x in range(1, q):
        z *= y
        iloczyn *= z
    return iloczyn


print(il_elem(3, 1, 5))
# zad7

def il_elem2(*arg):
    iloczyn = 1
    for x in arg:
        iloczyn *= x
    return iloczyn


print(il_elem2(3, 1, 5, 11))


# zad8


def liczba_produktow(** towary):
    ilosc = 0
    liczba = 0
    for pr in towary:
        ilosc += 1
        liczba += int(towary[pr])
    print('Ilosc: ' + str(ilosc) + ', suma: ' + str(liczba))



liczba_produktow(marchewki = 12, bulki = 6, cukierki = 60)
