''' Refaça o desafio 051, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while '''
primeiro_termo = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Qual a razao?: '))
#decimo_termo = primeiro_termo + (10 - 1) * razao

# Resolvendo o problema sem usar a formula
termo = primeiro_termo
cont = 1
while cont <= 10: # 10 eh limite de paragem porque soh queremos os 10 primeiros termos
    print(termo, end='-> ')
    termo += razao # Depois de imprimir o termo, actualizamos o termo com o valor da razao (o salto)
    cont += 1
print('ACABOU')