# programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e último nome separadamente.

nomeCompleto = str(input('Digite o nome completo de alguem: '))

print('Primeiro Nome: ', nomeCompleto.split() [0]) # A função split() transforma uma string em uma lista de strings, eliminando todos os espaços vazio.
print('Segundo Nome: ', nomeCompleto.split() [len(nomeCompleto.split()) - 1])