'''Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência. '''
print('-' * 40)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('-' * 40)
tbl_precos = ('Lapis', 1.75,
              'Borracha', 2,
              'Caderno', 15.9,
              'Estojo', 25,
              'Transferidor', 4.2,
              'Compasso', 9.99,
              'Mochila', 120.32,
              'Canetas', 22.30,
              'Livro', 34.9)
for pos, item in enumerate(tbl_precos):
    if pos % 2 == 0: # Na posicao PAR so temos os PRODUTOS, na IMPAR so temos os PRECOS.
        print(f'{item:.<30}', end='')
    else:
        print(f'R${item:>7.2f}')
print('-' * 40)
