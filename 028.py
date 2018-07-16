from random import randint
computador = randint(0, 10) #Faz o computador 'PENSAR'
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 10. Tente advinhar...')
print('-=-' * 20)
jogador = int(input('Em que número eu pensei: ')) #O jogador tenta advinhar
if jogador == computador:
	print('Parabéns! Você conseguiu me vencer! ')
else:
	print('Ganhei! Eu pensei no número {} e não no {}'.format(computador, jogador))