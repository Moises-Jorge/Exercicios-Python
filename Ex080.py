'''Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.'''
lista = list()
for i in range(5):
    num = int(input('Digite um valor: '))
    if i == 0 or num > lista[-1]:
        lista.append(num)
        print('Adicionado ao final da lista')
    else:
        for p,n in enumerate(lista):
            if num <= lista[p]:
                lista.insert(p, num)
                print(f'Adicionado na posicao {p} da lista')
                break
print('-=' * 30)
print(f'Os valores digitados em ordem foram: {lista}')