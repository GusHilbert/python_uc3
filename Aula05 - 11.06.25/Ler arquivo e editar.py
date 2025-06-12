#Funções - Manipulação de arquivos
#Criar uma função que lê um arquivo e edita se o usuário quiser

import os

def ler_arquivo(nome_arquivo: str):
    with open(nome_arquivo,'r') as arquivo:
        return arquivo.read()

def sobrescrever_arquivo(nome_arquivo: str,conteudo: str):
        with open(nome_arquivo,'w') as arquivo:
            arquivo.write(conteudo)

def editar_arquivo(nome_arquivo: str,conteudo: str):
        with open(nome_arquivo,'a') as arquivo:
            arquivo.write(conteudo)

def remover_arquivo(nome_arquivo:str):
    if os.path.exists(nome_arquivo):
        os.remove(nome_arquivo)
    else:
        print("Não existe um arquivo com esse nome")

def contar_linhas (nome_arquivo:str) -> int:
    with open(nome_arquivo, 'r') as arquivo:
        return len(arquivo.readlines())

def procurar_palavra (nome_arquivo:str,palavra:str) ->bool:
    with open(nome_arquivo, 'r') as arquivo:
        return palavra in arquivo.read()

etapa1 = input('Você quer criar um novo arquivo? (s/n)')

if etapa1 == "s":
    nome_arquivo = input("Qual o nome do arquivo que você deseja criar? ")
    conteudo_sobrescrito = input('Digite o novo conteúdo do arquivo: ')
    sobrescrever_arquivo(f'./Aula05 - 11.06.25/Arquivos/{nome_arquivo}.txt',f'{conteudo_sobrescrito}')
    print(ler_arquivo(f'./Aula05 - 11.06.25/Arquivos/{nome_arquivo}.txt'))
    print("Seu arquivo foi criado com sucesso!")

elif etapa1 == "n":

    nome = input('Digite o nome do arquivo a ser lido: ')
    print(ler_arquivo(f'./Aula05 - 11.06.25/Arquivos/{nome}.txt'))
    etapa2 = input("Você deseja procurar uma palavra no arquivo, contar a quantidade de linhas ou outros? (p|c|o)")
    if etapa2 == "p":
        palavra = input("Informe a palavra a ser procurada no arquivo: ")
        print(procurar_palavra(f'./Aula05 - 11.06.25/Arquivos/{nome}.txt',f'{palavra}'))


    elif etapa2 == "c":
        print(contar_linhas(f'./Aula05 - 11.06.25/Arquivos/{nome}.txt'))


    elif etapa2 == "o":
            etapa3 = input("Quer sobrescrever, adicionar ou apagar o conteúdo do arquivo ou remover o arquivo? (s|e|a|r) ")

            if etapa3 == "s":
                conteudo_sobrescrito = input('Digite o novo conteúdo do arquivo: ')
                sobrescrever_arquivo(f'./Aula05 - 11.06.25/Arquivos/{nome}.txt',f'{conteudo_sobrescrito}')
                print(ler_arquivo(f'./Aula05 - 11.06.25/Arquivos/{nome}.txt'))
                print("Seu arquivo foi sobrescrito")

            elif etapa3 == "e":
                conteudo_editado = input('Digite o novo conteúdo do arquivo: ')
                editar_arquivo(f'./Aula05 - 11.06.25/Arquivos/{nome}.txt',f'\n{conteudo_editado}')
                print(ler_arquivo(f'./Aula05 - 11.06.25/Arquivos/{nome}.txt'))
                print("Seu arquivo foi editado!")

            elif etapa3 == "a":
                apagar = ""
                sobrescrever_arquivo(f'./Aula05 - 11.06.25/Arquivos/{nome}.txt',f'{apagar}')
                print(ler_arquivo(f'./Aula05 - 11.06.25/Arquivos/{nome}.txt'))
                print("Seu conteúdo foi apagado!")

            elif etapa3 == "r":
                remover_arquivo(f'./Aula05 - 11.06.25/Arquivos/{nome}.txt')
                print("Seu arquivo foi apagado!")

            else :
                print("Não entendi o seu pedido!")

    else:
        print("Não entendi o seu pedido!")