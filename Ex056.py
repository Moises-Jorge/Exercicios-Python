''' Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:
    - A média de idade do grupo;
    - Qual é o nome do Homem mais velho;
    - Quantas mulheres têm menos de 20 anos.
'''

somatorio_idades = 0
media_idades = 0

nome_homem_velho = ''
maior_idade = 0

tot_mulher_menos20 = 0

for p in range(1, 4+1):
    print(f'----- {p} PESSOA -----')
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    
    somatorio_idades += idade
    
    if p == 1 and sexo in 'Mm': # Primeira ocorrencia, o primeiro valor digitado eh o maior.
        maior_idade = idade
        nome_homem_velho = nome
    elif idade > maior_idade and sexo in 'Mm': # Verificacao do homem mais velho
        maior_idade = idade
        nome_homem_velho = nome
    if idade < 20 and sexo in 'Ff': # Calculo do total de mulheres com menos de 20 anos
        tot_mulher_menos20 += 1
    
    
media_idades = somatorio_idades / 4

print(f'\nA media de idade do grupo eh: {media_idades} anos')
print(f'O homem mais velho tem {maior_idade} anos e chama-se {nome_homem_velho}')
print(f'Ao todo sao {tot_mulher_menos20} mulheres com menos de 20 anos')
