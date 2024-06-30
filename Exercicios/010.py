real = float(input('Quantos reais você tem na carteira R$ '))
dolar = real / 3.27
print('Com R${:.2f} você pode comemorar US${:.2f}'.format(real, dolar))