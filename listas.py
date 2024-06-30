lista_numeros = [2, 4, 9, 4, 7, 1]

print(lista_numeros[0])
print(lista_numeros[1])
print(lista_numeros[2])
print(lista_numeros[3])
print(lista_numeros[4])
print(lista_numeros[5])

lista_numeros.append(42)
print(lista_numeros[6])

# !lista_numeros.pop()
# !print("Último valor removido com pop()")

print("Lista Inicial: ", lista_numeros)
lista_numeros.sort()
print("Lista ordenada crescente: ", lista_numeros)
lista_numeros.reverse()
print("Lista ordenada decrescente: ", lista_numeros)

print("Tamanho lista: ", len(lista_numeros))
print("Menor valor: ", min(lista_numeros))
print("Maior valor: ", max(lista_numeros))