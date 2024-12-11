''' Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual é a soma entre eles (desconsiderando o flag → 999). '''
total_num_digitado = 0
soma_todos_num = 0
num = 0
while num != 999:
    num = int(input('Digite um numero: '))
    if num != 999:
       total_num_digitado += 1
       soma_todos_num += num
print(f'\nForam digitados {total_num_digitado} numeros no total.\nE a soma de todos eles eh: {soma_todos_num}')