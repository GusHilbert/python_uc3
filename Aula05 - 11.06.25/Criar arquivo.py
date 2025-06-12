#Funções - Manipulação de arquivos
#Criar uma função que cria e adiciona um texto no arquivo

def criar_arquivo(nome_arquivo: str,conteudo: str):
    """Cria um arquivo com nome e conteúdo fornecido"""
    with open(nome_arquivo,'w') as arquivo:
        arquivo.write(conteudo)
        print('Arquivo criado com sucesso!')

nome = input('Digite o nome do arquivo: ')
criar_arquivo(f'./Aula05 - 11.06.25/Arquivos/{nome}.txt',"Este é um exemplo de arquivo criado com Python")

