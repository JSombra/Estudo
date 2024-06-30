valor = 1
decrescente = True
anterior = int(input('Digite o primeiro número da sequência: '))
while valor != 0 and decrescente:
	valor = int(input('Digite o proximo número da sequência: '))
	if valor > anterior:
		decrescente = False
	anterior = valor

if decrescente: #== True
	print('A sequência em ordem decrescente ')
else:
	print('A sequência não está em ordem decrescente ')
