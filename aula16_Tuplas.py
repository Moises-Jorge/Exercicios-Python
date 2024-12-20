lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim', 'Batata Frita')

# Forma classica de usar o for para iterar sobre os valores da variavel composta (Nao eh possivel pegar a posicao do elemento com essa forma)
for comida in lanche:
    print(f'Eu vou comer {comida}')
print('*' * 30)
# Segunda Forma de iterar sobre os elementos de uma variavel composta (aqui ja eh possivel pegar a posicao)
for posicao, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posicao {posicao}')
print('*' * 30)
# Terceira Forma de iterar sobre os elementos. Aqui ja eh mais no braco. Tambem ja eh possivel pegar a posicao do elemento
for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]} na posicao {cont}')