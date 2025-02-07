'''Faça um mini-sistema que utilize o interactive help do python. O usuário vai digitar o comando e o manual vai aparecer. Quando o usuário digitar a palavra FIM, o programa se encerrará.
OBS: Use cores.'''
cores = ('\033[m',        # Pos: 0 - sem cores
         '\033[0;30;41m', # Pos: 1 - vermelho
         '\033[0;30;42m', # Pos: 2 - Verde
         '\033[0;30;43m', # Pos: 3 - Amarelo
         '\033[0;30;44m', # Pos: 4 - Azul
         '\033[0;30;45m', # Pos: 5 - Roxo
         '\033[7;30m'     # Pos: 6 - Branco
        )

def ajuda(comando):
    titulo(f'Acessando o manual do comando \'{comando}\'', 4)
    print(cores[6], end='')
    help(comando)
    print(cores[0], end='')


def titulo(msg, cor = 0):
    tam_msg = len(msg) + 4
    print(cores[cor], end='') # Adicionar a cor que esta vindo do parametro
    print('~' * tam_msg)
    print(f'  {msg}')
    print('~' * tam_msg)
    print(cores[0], end='') # Limpando a cor que veio do parametro. Deixando a cor padrao de novo


# Programa Principal
comando = ''
while True:
    titulo('SISTEMA DE AJUDA PyHELP', 2)
    comando = str(input('Funcao ou Biblioteca> '))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
titulo('ATE LOGO!', 1)