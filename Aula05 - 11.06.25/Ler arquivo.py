#Funções - Manipulação de arquivos
#Criar uma função que lê um arquivo

def ler_arquivo(nome_arquivo: str):
    """Retorna o conteúdo de um arquivo"""
    with open(nome_arquivo,'r') as arquivo:
        return arquivo.read()

nome = input('Digite o nome do arquivo a ser lido: ')
print(ler_arquivo(f'./Aula05 - 11.06.25/Arquivos/{nome}.txt'))

