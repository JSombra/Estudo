notas = []
i = 1
for x in range(5):
    print("Nota do Aluno", i)
    codigo_aluno = input("RA: ")
    nota = float(input("Nota: "))
    resultado = [codigo_aluno, nota]
    notas.append(resultado)
    i += 1
    
    
for n in notas:
    codigo_aluno = n[0]
    nota = n[1]
    print("O RA", codigo_aluno, "tirou a nota", nota)


#! Opçao de fazer o loop com While
while i <= 5:
    print("Nota do Aluno", i)
    codigo_aluno = input("RA: ")
    nota = float(input("Nota: "))
    resultado = [codigo_aluno, nota]
    notas.append(resultado)
    i += 1


for n in notas:
    codigo_aluno = n[0]
    nota = n[1]
    print("O RA", codigo_aluno, "tirou a nota", nota)