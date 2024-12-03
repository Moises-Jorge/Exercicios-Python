''' Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos. '''
maior_peso = 0 # Poderia se usar uma lista caso fosse necessario armazenar os pesos.
menor_peso = 0

for c in range(1, 5+1):
    peso = float(input(f'Digite o {c} peso: '))
    
    if c == 1: # Na primeira iteracao, o peso lido sera tanto o maior peso quanto o menor peso
        maior_peso = peso
        menor_peso = peso
    else:
        if peso > maior_peso:
            maior_peso = peso
        elif peso < menor_peso:
            menor_peso = peso
print(f'O maior peso digitado foi: {maior_peso:.2f}')
print(f'O menor peso digitado foi: {menor_peso:.2f}')