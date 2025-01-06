'''Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final, mostre um boletim contendo a média de cada um e permita que o  usuário possa mostrar as notas de cada aluno individualmente.'''
dados_aluno = list()
lista_alunos = list()
while True:
    dados_aluno.append(str(input('Nome: ')))
    dados_aluno.append(float(input('Nota 1: ')))
    dados_aluno.append(float(input('Nota 2: ')))
    lista_alunos.append(dados_aluno[:])
    dados_aluno.clear()
    saida = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    while saida not in 'SN':
        saida = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if saida == 'N':
        break
print('-=' * 30)
print(f'{"Nº": <4}{"NOME": <10}{"MÉDIA": >8}') # Endireitar a formatacao aqui
print('-' * 25)
for num_aluno, aluno in enumerate(lista_alunos):
    media_aluno = (aluno[1] + aluno[2]) / 2
    print(f'{num_aluno: <4}{aluno[0]: <10}{media_aluno: >8}') # E aqui tambem
while True:
    print('-' * 35)
    numero_aluno = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if numero_aluno == 999:
        print('FINALIZANDO...\nVOLTE SEMPRE >>>')
        break
    if numero_aluno <= len(lista_alunos) - 1:
        print(f'Notas de {lista_alunos[numero_aluno][0]} são: {[lista_alunos[numero_aluno][1], lista_alunos[numero_aluno][2]]}')
