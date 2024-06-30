from math import hypot
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjascente: '))
hi = hypot(co, ca)
print('A hipotenusa mede {:.2f}'.format(hi))