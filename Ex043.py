''' Desenvolva uma logica que leia o peso e altura de uma pessoa, calcule seu IMC e mostre seu status, de acordo com a tabela abaixo
    - Abaixo de 18.5: Abaixo do Peso
    - Entre 18.5 e 25: Peso ideal
    - 25 ate 30: Sobrepeso
    - 30 ate 40: Obesidade
    - Acima de 40: Obesidade mórbida
'''

peso = float(input("Informe o peso: "))
altura = float(input("Informe a altura: "))
imc = peso / pow(altura, 2)

print(f'IMC = {imc:.2f}')

if imc < 18.5:
    print("Esta abaixo do peso!")
elif imc < 25:
    print("Peso ideal, continue assim!")
elif imc < 30:
    print("Esta sobrepeso, precisa se exercitar!")
elif imc < 40:
    print("Obesidade. Precisa fazer dieta e se exercitar!")
else:
    print("Obesidade Morbida. Precisa de uma cirurgia!")