def factorial(n):
    f = 1
    for cont in range(1, n+1):
        f *= cont
    return f


def dobro(n):
    return n * 2


def triplo(n):
    return n * 3


def leia_int(msg):
    """ -> Funcao responsavel por ler e validar somente numeros inteiros

    Args:
        msg (string): mensagem de entrada (que pede para o usuario informar o valor)

    Returns:
        inteiro: retorna o numero inteiro lido
    """
    while True:
        try:
            num = int(input(msg))
        except (ValueError, TypeError):
            print(f'\033[0;31mERRO: por favor, digite um numero inteiro valido.\033[m')
        except (KeyboardInterrupt):
            print('\033[0;Usuario preferiu nao digitar esse numero.\033[m')
            return 0
        else:
            return num
        
        
def leia_float(msg):
    """-> Funcao responsavel por ler e validar somente numeros com ponto flutuante

    Args:
        msg (string): mensagem de entrada (que pede para o usuario informar o valor)

    Returns:
        float: retorna o numero real lido
    """
    while True:
        try:
            num = float(input(msg))
        except (ValueError, TypeError):
            print(f'\033[0;31mERRO: por favor, digite um numero real valido.\033[m')
        except (KeyboardInterrupt):
            print('\033[0;Usuario preferiu nao digitar esse numero.\033[m')
            return 0
        else:
            return num