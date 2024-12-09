''' Crie um programa que leia dois valores a mostra um menu no tela:
    1. somar
    2. multiplicar
    3. maior
    4. novos números
    5. sair do programa
'''
from time import sleep

n1 = int(input('1º Valor: '))
n2 = int(input('2º Valor: '))

opcao = 0
while opcao != 5:
    # MENU
    print('''   
    [ 1 ] - Somar
    [ 2 ] - Multiplicar
    [ 3 ] - Maior
    [ 4 ] - Novos numeros
    [ 5 ] - Sair do programa
    ''')
    opcao = int(input('>>>>> Qual eh a sua opcao?: '))
    
    if opcao == 1:
        print(f'A soma entre {n1} + {n2} = {n1 + n2}')
    elif opcao == 2:
        print(f'O resultado de {n1} x {n2} = {n1 * n2}')
    elif opcao == 3:
        if n1 > n2:
            print(f'Entre {n1} e {n2} o maior valor eh {n1}')
        elif n1 < n2:
            print(f'Entre {n1} e {n2} o maior valor eh: {n2}')
        else:
            print('Os dois numeros sao iguais!')
    elif opcao == 4:
        print('Informe os numeros novamente.')
        n1 = int(input('1º Valor: '))
        n2 = int(input('2º Valor: '))
    elif opcao == 5:
        print('Finalizando...')
    else:
        print('OPCAO INVALIDA. Tente novamente!')
    print('=-=' * 10)
    sleep(1.5)
print('Fim do programa! Volte Sempre!')