'''Crie um programa que tenha uma função leia_int(), que vai funcionar de forma semelhante à função input() do python, só que fazendo a validação para aceitar apenas valores numéricos'''
def leia_int(msg_entrada):
    while True:
        n = str(input(msg_entrada))
        if n.isnumeric():
            return n
        else:
            print('\033[0;31mERRO! Digite um numero inteiro valido.\033[m')


# Programa principal
n = leia_int('Digite um numero: ')
print(f'Voce acabou de digitar o numero {n}')