''' Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores. '''

from datetime import date
ano_atual = date.today().year

#lista_anos = []    # A lista eh opcional, caso seja necessario armazenar os anos lidos.
maiores = 0
menores = 0

for i in range(7):
    ano = int(input(f'Informe o {i + 1} ano de nascimento: '))
    #lista_anos.append(ano)
    
    if (ano_atual - ano) < 18:
        menores += 1
    else:
        maiores += 1
#print(lista_anos)
print(f'menores: {menores}')
print(f'maiores: {maiores}')
