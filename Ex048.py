''' Faça um programa que calcule a soma entre todos os números ímpares que são múltiplos de três e que se encontram no intervalo de 1 até 500. '''
soma_impares = 0
for n in range(1, 500, 2):
    if n % 3 == 0:
        soma_impares += n
print(f"\nA soma dos impares eh: {soma_impares}")