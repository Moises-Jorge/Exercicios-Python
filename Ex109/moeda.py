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