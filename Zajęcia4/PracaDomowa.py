#zad 1
lista = [x * 2 for x in range(0, 31)]
plik = open('zad1.txt', 'w+')
plik.writelines(str(lista))
plik.close()

#zad 2
plik = open('zad1.txt', 'r')
print(plik.readlines())
plik.close()


# zad3
with open('zad3.txt', 'a+') as plik:
    for x in range(0, 5):
        plik.writelines('Jakis tekst:  ' + str(x))
plik = open('zad3.txt', 'r')
print(plik.readlines())
plik.close()
