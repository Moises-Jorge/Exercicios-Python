''' Crie um programa que leia um frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços. '''

frase = str(input('Digite uma frase: ')).upper().strip().split()
frase = ''.join(frase)
inversa = frase[::-1] # Estrategia sem uso de um ciclo para inverter uma string.
frase_inversa = ''

# Estrategia usando um Ciclo
""" for letra in range(len(frase) - 1, -1, -1):
    frase_inversa = frase_inversa + frase[letra] """

print(frase, inversa)

if frase == inversa:
    print('A frase digitada eh um PALINDROMO')
else:
    print('A frase digitada NAO eh um PALINDROMO')