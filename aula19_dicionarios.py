estado = dict()
pais = list()
for c in range(3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    pais.append(estado.copy())
for estadu in pais: # Ciclo que vai iterar sobre os elementos da lista
    for key, value in estadu.items(): # Ciclo que vai iterar sobre os elementos do dicionario
        print(f'{value}', end=' ')
    print()