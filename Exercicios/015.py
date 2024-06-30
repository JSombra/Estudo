import pygame

dias = int(input('Quantos dias você ficou com o carro :'))
km = float(input('Quantos km você rodou com o carro: '))
pago = (dias * 60) + (km * 0.15)
print('O total a pagar e de R${:.2f}'.format(pago))