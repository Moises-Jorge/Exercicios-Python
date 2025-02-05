'''Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa, retornando um literal indicando se uma pessoa tem voto NEGADO, OPCIONAL ou OBRIGATÓRIO nas eleições.'''
def  voto(ano_nasci):
    from datetime import datetime
    ano_actual = 2018#datetime.now().year
    idade = ano_actual - ano_nasci
    msg = ''
    if idade < 18:
        msg = f'Com {idade} anos: VOTO NEGADO'
    elif idade > 65:
        msg = f'Com {idade} anos: VOTO OPCIONAL'
    else:
        msg = f'Com {idade} anos: VOTO OBRIGATORIO'
    return msg



# Programa Principal
print('-' * 30)
ano_nascimento = int(input('Em que ano vc nasceu?: '))
print(voto(ano_nascimento))