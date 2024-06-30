def cadastrar_pessoa():
    nome = input("Digite o nome da pessoa: ")
    idade = int(input("Digite a idade da pessoa: "))
    cpf = input("Digite o CPF da pessoa: ")
    return {"nome": nome, "idade": idade, "cpf": cpf}

pessoas = []
while True:
    print("\n=== Cadastro de Pessoa ===")
    pessoa = cadastrar_pessoa()
    pessoas.append(pessoa)
    continuar = input("Deseja cadastrar outra pessoa? (s/n): ")
    if continuar.lower() != 's':
        break
    
    
    
print("\n=== Pessoas Cadastradas ===")

for pessoa in pessoas:
    print(pessoa)
    
menores_de_idade = []
maiores_de_idade = []

for pessoa in pessoas:
    if pessoa['idade'] < 18:
        menores_de_idade.append(pessoa)
    else:
        maiores_de_idade.append(pessoa)

print("\n=== Pessoas Menores de 18 Anos ===")
for pessoa in menores_de_idade:
    print(pessoa)

print("\n=== Pessoas Maiores de 18 Anos ===")
for pessoa in maiores_de_idade:
    print(pessoa)