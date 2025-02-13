'''Crie um código em Python que teste se o site Pudim está acessível pelo computador usado.'''
from urllib import request, error

try:
    site = request.urlopen('http://www.pudim.com.br')
except error.URLError as erro:
    print(f'\033[0;31mO site Pudim nao esta acessivel no momento.\033[m\nO erro que ocorreu foi: {erro.reason}')
else:
    print('Consegui acessar o site Pudim com sucesso!')