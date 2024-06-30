import os

mensagens = []

nome = input("Nome: ")

while True:
    # limpar terminal    
    os.system('clear')
    
    if len(mensagens) > 0:
        for m in mensagens:
            print(m['nome'], "-", m['texto'])
            
    print("__________________")
    
    texto = input("Mensagem: ")
    if texto.upper() == "FIM":
        break 
    
    mensagens.append({
        "nome": nome,
        "texto": texto
    })