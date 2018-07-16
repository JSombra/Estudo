from math import sqrt
a = int(input('Qual o valor de A: '))
b = int(input('Qual o valor de B: '))
c = int(input('Qual o valor de C: '))
x = (b**2) - (4*a*c)

if x < 0:
	print('Raiz negativa não pode ser extraida. ')
else :
	x = math.sqrt(x)
	x1 = (-b+x)/(2*a)
	x2 = (-b+x)/(2*a)
print("\n  X1 = {} \n X2 = {}".format(x1, x2))
