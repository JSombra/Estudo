meuCartão = int(input('Digite o número do seu cartão de crédito: '))
cartãoLido = 1
encontreiMeuCartãoNaLista = False
while cartãoLido != 0 and not encontreiMeuCartãoNaLista:
	cartãoLido = int(input('Digite o próximo cartão de crédito: '))
	if cartãoLido == meuCartão:
		encontreiMeuCartãoNaLista = True
if encontreiMeuCartãoNaLista:
	print('Meu cartão está lá! ')
else:
	print('Meu cartão não está lá! ')
