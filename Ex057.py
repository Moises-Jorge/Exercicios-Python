''' Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores M ou F. Caso esteja errado, peça a digitação novamente até ter um valor correto. '''

# PRIMEIRA LOGICA
sexo = str(input('Informe seu sexo [M/F]: ')).upper().strip()[0]
while sexo not in 'MF':
    sexo = str(input('Dados Invalidos. Por favor, informe seu sexo [M/F]:')).upper().strip()[0]
print(f'Sexo {sexo} registrado com sucesso')
    
""" # SEGUNDA LOGICA
sexo_valido = True
while sexo_valido:
    sexo = str(input('Informe seu sexo [M/F]: ')).upper().strip()[0]
    if sexo == 'M' or sexo == 'F':
        sexo_valido = False
    elif sexo not in 'MF':
        print('Dados invalidos. Por favor, ', end='')
print(f'Sexo {sexo} registrado com sucesso') """