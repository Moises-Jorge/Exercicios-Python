'''Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-os (com idade) em um dicionário. se por acaso a CTPS for diferente de zero, o dicionário receberá também o ano de contratação e o salário. Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.'''
from datetime import datetime
ano_actual = 2018 #datetime.now().year
dict_profissional = dict()
dict_profissional['nome'] = str(input('Nome: '))
ano_nascimento = int(input('Ano de Nascimento: '))
dict_profissional['idade'] = ano_actual - ano_nascimento
dict_profissional['ctps'] = int(input('Carteira de Trabalho (0 nao tem): '))
if dict_profissional['ctps'] != 0:
    dict_profissional['cotratacao'] = int(input('Ano de Contratacao: '))
    dict_profissional['salario'] = float(input('Salario: R$'))
    dict_profissional['aposentadoria'] = dict_profissional['idade'] + ((dict_profissional['cotratacao'] + 35) - ano_actual)
print('-=' * 30)
for k, v in dict_profissional.items():
    print(f' - {k} tem o valor {v}')