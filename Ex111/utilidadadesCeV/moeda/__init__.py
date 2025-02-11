def aumentar(preco, taxa, formatacao = False):
    resp = preco + (preco * (taxa / 100))
    return resp if formatacao is False else moeda_format(resp)


def diminuir(preco, taxa, formatacao = False):
    resp = preco - (preco * (taxa / 100))
    return resp if formatacao is False else moeda_format(resp)


def dobro(preco, formatacao = False):
    resp = preco * 2
    return resp if formatacao is False else moeda_format(resp)


def metade(preco, formatacao = False):
    resp = preco / 2
    return resp if formatacao is False else moeda_format(resp)


def moeda_format(preco=0, simbolo='R$'):
    return f'{simbolo}{preco:.2f}'.replace('.', ',')


def resumo(preco=0, taxa_aumento=0, taxa_reducao=0):
    print('-' * 30)
    print('RESUMO DO VALOR'.center(30))
    print('-' * 30)
    print(f'Preco analisado: \t{moeda_format(preco)}')
    print(f'Dobro do preco: \t{dobro(preco, True)}')
    print(f'Metade do preco: \t{metade(preco, True)}')
    print(f'{taxa_aumento}% de aumento: \t{aumentar(preco, taxa_aumento, True)}')
    print(f'{taxa_reducao}% de reducao: \t{diminuir(preco, taxa_reducao, True)}')
    print('-' * 30)