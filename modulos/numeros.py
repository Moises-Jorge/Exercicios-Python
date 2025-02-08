from uteis.numeros import factorial, dobro # Funcoes dentro do Sub_pacote "numeros", construidas dentro do modulo "__init__.py"
from uteis.teste import abc, xyz # Funcoes dentro do modulo "teste.py"! A forma de importacao eh a mesma
from uteis.numeros.teste_num import aaa, bbb # Funcoes dentro do modulo "teste_num" que esta dentro do sub_pacote "numeros"


# Programa Principal
num = int(input('Digite um numero: '))
fat = factorial(num)
print(f'O factorial de {num} eh {fat}')
print(f'O dobro de {num} eh {dobro(num)}')