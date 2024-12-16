''' Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo. '''
while True:
    numero = int(input('Quer ver tabuada de qual valor?: '))
    if numero < 0:
        break
    print('-' * 30)
    for i in range(1,11):
        print(f'{numero} x {i} = {numero * i}')
    print('-' * 30)
print('PROGRAMA TABUADA ENCERRADO. Volte sempre!')