def leia_dinheiro(msg):
    while True:
        entrada = str(input(msg)).replace(',', '.').strip()
        if entrada.isalpha() or entrada == '':
            print(f'\033[0;31mERRO: \"{entrada}\" eh um preco invalido!\033[m')
        else:
            return float(entrada)


def leia_int(msg_entrada):
    """-> Funcao que verifica se o valor de entrada eh mesmo um numero inteiro

    Args:
        msg_entrada (literal): Mensagem de entrada

    Returns:
        valor inteiro: o valor inteiro lido
    """
    while True:
        n = str(input(msg_entrada))
        if n.isnumeric():
            return n
        else:
            print('\033[0;31mERRO! Digite um numero inteiro valido.\033[m')