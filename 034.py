salario = float(input('Qual o salário do funcionario: R$ '))
if salario <= 1250:
	novo = salario + (salario * 15 / 100)
else:
	novo = salario + (salario * 10 / 100)
print('Quem ganhava R${:.2f} agora passa a ganhar R${:.2f}'.format(salario, novo))