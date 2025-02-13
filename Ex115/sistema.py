from lib.interface import cabecalho, menu
from time import sleep

while True:
    opcao = menu(['Ver pessoas cadastradas', 'Cadastrar nova pessoa', 'Sair do Sistema'])
    if opcao == 1:
        cabecalho('Opcao 1')
    elif opcao == 2:
        cabecalho('Opcao 2')
    elif opcao == 3:
        cabecalho('Saindo do programa... Ate logo!')
        break
    else:
        print('\033[0;31mERRO! Digite uma opcao valida!\033[m')
    sleep(2)
