from lib.interface import cabecalho, menu, leia_int
from lib.arquivo import *
from time import sleep

arquivo = 'Ex115/curso_em_video.txt'

if not arquivo_existe(arquivo): # Verificar se o arquivo existe antes de prosseguir com o programa.
    criar_arquivo(arquivo)

while True:
    opcao = menu(['Ver pessoas cadastradas', 'Cadastrar nova pessoa', 'Sair do Sistema'])
    if opcao == 1: # Opcao para listar o coteudo de um arquivo (pessoas cadastrada)
        ler_arquivo(arquivo)
    elif opcao == 2: # Opcao para cadastrar uma nova pessoa
        cabecalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = leia_int('Idade: ')
        cadastrar_pessoa(arquivo, nome, idade)
    elif opcao == 3: # Opcao para sair do sitema
        cabecalho('Saindo do programa... Ate logo!')
        break
    else:
        print('\033[0;31mERRO! Digite uma opcao valida!\033[m')
    sleep(2)
