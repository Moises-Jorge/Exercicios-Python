'''Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. No final, mostre o conteúdo da estrutura na tela.'''
dados_aluno = dict()
dados_aluno['nome'] = str(input('Nome: '))
dados_aluno['media'] = float(input(f'Media de {dados_aluno["nome"]}: '))
if dados_aluno['media'] < 5:
    dados_aluno['situacao'] = 'Reprovado'
elif dados_aluno['media'] < 7:
    dados_aluno['situacao'] = 'Recuperacao'
else:
    dados_aluno['situacao'] = 'Aprovado'
print('-=' * 30)
for chave, valor in dados_aluno.items():
    print(f'  - {chave} eh igual a {valor}')
