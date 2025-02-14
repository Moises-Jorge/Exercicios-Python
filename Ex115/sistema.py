from lib.interface import cabecalho, menu
from lib.arquivo import *
from time import sleep

arquivo = 'Ex115/curso_em_video.txt'

if not arquivo_existe(arquivo): # Verificar se o arquivo existe antes de prosseguir com o programa.
    criar_arquivo(arquivo)

while True:
    opcao = menu(['Ver pessoas cadastradas', 'Cadastrar nova pessoa', 'Sair do Sistema'])
    if opcao == 1:
        ler_arquivo(arquivo)
    elif opcao == 2:
        cabecalho('Opcao 2')
    elif opcao == 3:
        cabecalho('Saindo do programa... Ate logo!')
        break
    else:
        print('\033[0;31mERRO! Digite uma opcao valida!\033[m')
    sleep(2)
