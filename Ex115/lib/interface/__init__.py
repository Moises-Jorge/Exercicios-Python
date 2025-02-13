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


def linha(tam: int = 42) -> None:
    """ -> Funcao que exibe uma linha horizontal na tela

    Args:
        tam (int, optional): Esse parametro define o tamanho da linha. Por padrao o tamanho eh 42.
    """
    print('-' * tam)
    
    
def cabecalho(texto: str) -> None:
    linha()
    print(texto.center(42))
    linha()


def menu(lista: list()) -> int:
    cabecalho('MENU PRINCIPAL')
    cont = 1
    for indice, item in enumerate(lista):
        print(f'\033[33m{cont}\033[m - \033[34m{item}\033[m')
        cont += 1
    linha()
    opcao = leia_int('\033[32mSua Opcao: \033[m')
    return opcao
    