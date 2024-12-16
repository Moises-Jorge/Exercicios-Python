''' Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
    1. Quantas pessoas têm mais de 18 anos.
    2. Quantos homens foram cadastrados.
    3. Quantas mulheres têm menos de 20 anos.'''
maiores_idade = homens = mulheres_menor_20 = 0
while True:
    print('-' * 30)
    print('    CADASTRE UMA PESSOA')
    print('-' * 30)
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip().upper()[0]
    while sexo not in 'MF':
        sexo = str(input('Sexo [M/F]: ')).strip().upper()[0]
    if idade >= 18:
        maiores_idade += 1
    if sexo == 'M':
        homens += 1
    elif sexo == 'F' and idade < 20:
        mulheres_menor_20 += 1
    print('-' * 30)
    cond_saida = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    while cond_saida not in 'SN':
        cond_saida = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if cond_saida == 'N':
        break
print('====== FIM DO PROGRAMA ======')
print(f'Total de pessoas com mais de 18 anos: {maiores_idade}\nAo todo temos {homens} homens cadastrados\nE temos {mulheres_menor_20} mulheres com menos de 20 anos.')