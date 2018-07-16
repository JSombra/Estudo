soma = 0
valor = 1
tamanho = int(input('Quantos valores tem na sequencia: '))
i = 0

while i < tamanho:
	valor = int(input('Digite o valor a ser somado: '))
	soma = soma + valor
	i = i + 1
print('A soma dos valores digitados é: {}'.format(soma))
