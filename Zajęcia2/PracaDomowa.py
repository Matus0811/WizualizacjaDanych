"""
#zad1
lista = ['Piłka Nożna', 'Koszykówka']
lista.reverse()
lista.append('Boks')
print(lista)
"""
"""
#zad2
dic = {
    'FB' : 'Facebook',
    'IG' : 'Instagram',
    'YT' : 'Youtoube'
}
print(dic)
"""
"""
#zad3
dic = {
    'W3' : 'Wiedźmin 3 Dziki Gon',
    'AC' : 'Assassins Creed',
    'CP77' : 'Cyberpunk 2077'
}
print(dic)
"""
"""
#zad4
tekst = input('Podaj tekst: \n')
print('Liczba wystapien litery a: {0}'.format(tekst.count('a')))
"""
"""
#zad6
a = input("Podaj liczbe a: ")
b = input("Podaj liczbe b: ")
c = input("Podaj liczbe c: ")
if (a > b):
    if (a > c):
        print(a)
    else:
        print(c)
else:
    if (b > c):
        print(b)
    else:
        print(c)
"""
"""
#zad7
lista = [8, 1, 4.5, 1.5]
for x in range(0, lista.__len__(), 1):
    lista[x] **= 2
print(lista)
"""
"""
#zad8
lista = []
z = 0
while (z < 10):
    y = int(input('Podaj liczbe: '))
    z = z + 1
    if (y % 2 == 0):
        lista.append(y)
print(lista)
"""

#zad9
x = int(input('Podaj liczbe dodatnią : '))
if (x < 0):
    print('Nie jest to liczba dodatnia')
else:
    print('Pierwiastek z {0} = {1}'.format(x, x ** 0.5))
