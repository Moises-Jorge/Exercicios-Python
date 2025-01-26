'''Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável.'''
def escreva(msg):
    tam_msg = len(msg) + 4
    print('~' * tam_msg)
    print(f'  {msg}')
    print('~' * tam_msg)
    
    
# Programa principal
msg = str(input())
escreva(msg)