''' Refaça o Desafio 009, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for. '''

num = int(input('Quer tabuada de que numero?: '))
for i in range(0, num + 1):
    print(f'{num} X {i} = {num * i}')