'''Rescreva a função leia_int() que fizemos no desafio 104, incluindo agora a possibilidade da digitação de um numero invalido. Aproveite e crie também uma função leia_float() com a mesma funcionalidade.'''
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
        


# programa principal
numero = leia_int('Digite um Inteiro: ')
numero2 = leia_float('Digite um Real: ')
print(f'O numero inteiro digitado foi {numero} e o real foi {numero2}')