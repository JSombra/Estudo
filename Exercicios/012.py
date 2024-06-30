preço = float(input('Qual o preço do produto R$ '))
novo = preço - (preço * 51 / 100)
print('O produto que custava {:.2f} com o desconto de 76% passou a custar {:.2f}'.format(preço, novo))