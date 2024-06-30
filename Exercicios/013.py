salario = float(input('Qual o funcionario recebe R$ '))
novo = salario + (salario * 15 / 100)
print('O funcionario que recebia {:.2f} com o reajuste de 15% passará a receber {:.2f}'.format(salario, novo))