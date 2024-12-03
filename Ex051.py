''' Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão. '''
primeiro_termo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razao: '))  # Razao eh o numero de saltos/pulos
decimo_termo = primeiro_termo + (10 - 1) * razao # Soh eh (10 - 1) porque queremos o decimo termo. Se fosse o vigesimo termo seria (20 - 1)
for c in range(primeiro_termo, decimo_termo + razao, razao):
    print(c, end='-> ')
print('ACABOU')