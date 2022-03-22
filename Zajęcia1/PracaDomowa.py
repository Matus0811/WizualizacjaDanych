
#zad1
a=1
b=3
print(a)
print(b)
c=3,14
d=2,18
print(c)
print(d)
e = 5 + 1j
f = 8 - 4j
print(e)
print(f)
g = 'Napis'
h = 'tekścik'
print(g)
print(h)

#zad2
i = 8
j = 2
print('{0} + {1} = {2}'.format(i, j, i + j))
print('{0} - {1} = {2}'.format(i, j, i - j))
print('{0} * {1} = {2}'.format(i, j, i * j))
print('{0} / {1} = {2}'.format(i, j, i / j))

#zad 3
a=1
a+=5
print(a)
b=12
b-=3
print(b)
c=5
c*=4
print(c)
d=8
d/=2
print(d)
e=10
e**=2
print(e)
f=20
f%=3
print(f)

#zad4
import math
print('{0} ^ 10 = {1}'.format(math.e, math.e ** 15))
a = (math.log(4 + math.sin(10) ** 3, math.e)) ** (4 / 7)
print('{0} = {1}'.format('a', a))
print('floor({0}) = {1}'.format(2.67, math.floor(2.67)))
print('floor({0}) = {1}'.format(2.67, math.ceil(2.67)))

#zad5
import string
imie = 'KAMIL'
nazw = 'MATUSIAK'
print('{0} {1}'.format(imie.capitalize(), nazw.capitalize()))

#zad6
tekst = 'O la la O la la O la la'
zlicz = tekst.count('la')
print(zlicz)

#zad7
tekst = 'Kamil'
print(tekst[0])
print(tekst[tekst.__len__() - 1])


#zad8
tekst = 'Dowolny wymyslony tekst'
x = tekst.split(' ')
print(x)

#zad9
tekst = 'Tekst'
Lzp = 21.5
Lhd = 0xff
print("{0} {1} {2}".format(tekst, Lzp, Lhd))
