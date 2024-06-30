velocidade = int(input('A quantos Km/h o carro está: '))
if velocidade > 80:
	print('Multado! Você excedeu o limite que é de 80km/h')
	multa = (velocidade - 80) * 7
	print('Você terá que pagar uma multa de R${:.2f}'.format(multa))
else:
	print('Tenha um bom dia dirija com segurança.')