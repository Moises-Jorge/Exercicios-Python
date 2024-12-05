''' Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores M ou F. Caso esteja errado, peça a digitação novamente até ter um valor correto. '''

""" PRIMEIRA LOGICA
sexo = ''
while (sexo != 'M') or (sexo != 'F') :
    sexo = str(input('Digite o sexo: ')).upper() """
    
sexo_valido = True
while sexo_valido:
    sexo = str(input('Digite o sexo [M/F]: ')).upper()
    if sexo == 'M' or sexo == 'F':
        sexo_valido = False