n = int(input('Digite um numero para\ncalcular o seu Fatorial: '))
factorial = 1

print(f'Calculando {n}! = ', end='')
while n >= 1:
    print(f'{n}', end='')
    print(' x ' if n > 1 else ' = ', end='')
    factorial *= n
    n -= 1
print(factorial)

""" # COM FOR
print(f'Calculando {n}! = ', end='')
for i in range(n, 0, -1):
    print(f'{i}', end='')
    print(' x ' if i > 1 else ' = ', end='')
    factorial *= i
print(factorial) """