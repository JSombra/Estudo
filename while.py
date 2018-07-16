idade = int(input('Digite sua idade: '))
altura = float(input('Digite sua altura: '))
peso = int(input('Digite seu peso: '))

if idade >= 18 and altura >= 1.80 and peso >= 60:
	print('Apto')
else:
	print('Inapto')