fluxo_caixa = []

print('----------------')
print('Fluxo de Caixa')
print('----------------')
print('1 - Adicionar receita')
print('2 - Adicionar despesa')
print('\n# Digite outro numero para encerrar #\n')

def operacao(codigo):
    if codigo == 1:
        nome = input("Nome: ")
        valor = float(input("Valor: "))
        fluxo_caixa.append({
        "nome": nome,
        "valor": valor,
        "operacao": "Receita"
        })
    else:
        nome = input("Nome: ")
        valor = float(input("Valor: "))
        fluxo_caixa.append({
        "nome": nome,
        "valor": valor,
        "operacao": "Despesa"
        })

# ! Não utilizado mais
# def receita():
#     nome = input("Nome: ")
#     valor = float(input("Valor: "))
#     fluxo_caixa.append({
#         "nome": nome,
#         "valor": valor,
#         "operacao": "Receita"
#     })
#     return True
    
# def despesa():
#     nome = input("Nome: ")
#     valor = float(input("Valor: "))
#     fluxo_caixa.append({
#         "nome": nome,
#         "valor": valor,
#         "operacao": "Despesa"
#     })
#     return True
    

while True:
    opcao = int(input("Digite a opção: "))
       
    if opcao == 1:
        operacao(opcao)
        print("\n")
    elif opcao == 2:
        operacao(opcao)
        print("\n")
    else:
        break
    
total = 0

for fc in fluxo_caixa:
    print("Nome:", fc['nome'], ", Valor: R$", fc['valor'], ", Tipo de operação:", fc['operacao'])
    if fc['operacao'] == "Receita":
        total = total + fc['valor']
    else:
        total = total - fc['valor']

print("Saldo atual: R$",total)