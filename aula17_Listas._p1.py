valores = list() # == valores = []
for c in range(3):
    valores.append(int(input(f'{c+1}º valor: ')))

for chave, valor in enumerate(valores):
    print(f'N posicao {chave} encontrei o valor {valor}!')
print('Cheguei ao final da lista.')