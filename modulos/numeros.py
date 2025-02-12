from uteis.numeros import factorial, dobro # Funcoes dentro do Sub_pacote "numeros", construidas dentro do modulo "__init__.py"


# Programa Principal
num = int(input('Digite um numero: '))
fat = factorial(num)
print(f'O factorial de {num} eh {fat}')
print(f'O dobro de {num} eh {dobro(num)}')