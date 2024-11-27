''' Refaça o desafio 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triangulo sera formado:
    - Equilátero: todos os lados iguais
    - Isosceles: dois lados iguais
    - Escaleno: todos os lados diferentes
'''
a = float(input('Informe a primeira recta: '))
b = float(input('Informe a segunda recta: '))
c = float(input('Informe a terceira recta: '))

if (a + b > c) and (a + c > b) and (b + c > a):
    if a == b and b == c: # Poderia ser da seguinte forma: a == b == c ...
        print('Essas rectas podem formar um triangulo: Equilatero')
    elif a != b and b != c and a != c: # Poderia ser da seguinte forma: a != b != c != a ...
        print('Essas rectas podem formar um triangulo: Escaleno')
    else:
        print('Essas rectas podem formar um triangulo: Isosceles')
else:
    print('As rectas nao podem formar um triangulo')