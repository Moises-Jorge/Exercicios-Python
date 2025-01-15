'''Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre:
    1. Quantas pessoas foram cadastradas
    2. A média de idade do grupo
    3. Uma lista com todas as mulheres
    4. Uma lista com todas as pessoas com idade acima da média.'''
dados_pessoa = dict()
lista_pessoas = list()
while True:
    dados_pessoa['nome'] = str(input('Nome: '))
    dados_pessoa['sexo'] = str(input('Sexo: [M/F] ')).strip().upper()[0]
    while dados_pessoa['sexo'] not in 'MF':
        print('ERRO! Por favor, digite apenas M ou F.')
        dados_pessoa['sexo'] = str(input('Sexo: [M/F]')).strip().upper()[0]
    dados_pessoa['idade'] = int(input('Idade: '))
    lista_pessoas.append(dados_pessoa.copy())
    saida = str(input('Quer continuar?: [S/N] ')).strip().upper()[0]
    while saida not in 'SN':
        print('ERRO! Responda apenas S ou N.')
        saida = str(input('Quer continuar?: [S/N] ')).strip().upper()[0]
    if saida == 'N':
        break
print('-=' * 30)
print(f'A) Ao todo temos {len(lista_pessoas)} pessoas cadastradas.')
tot_idade = sum(pessoa['idade'] for pessoa in lista_pessoas)
media_idades = tot_idade / len(lista_pessoas)
print(f'B) A media de idade eh de {media_idades:.2f} anos')
lista_mulheres = [pessoa for pessoa in lista_pessoas if pessoa['sexo'] == 'F']
print(f'C) As mulheres cadastradas foram ', end='')
for mulher in lista_mulheres:
    for k, v in mulher.items():
        if k == 'nome':
            print(v, end=' ')
lista_mais_velhos = [pessoa for pessoa in lista_pessoas if pessoa['idade'] > media_idades]
print(f'\nD) Lista das pessoas que estao acima da media:')
for pessoa in lista_mais_velhos:
    for k, v in pessoa.items():
        print(f'    {k} = {v};', end='')
    print()
print('<< ENCERRADO >>')
