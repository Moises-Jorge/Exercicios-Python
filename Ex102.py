'''Crie um programa que tenha uma função factorial() que receba dois parâmetros: o primeiro que indique o número a calcular, e o outro chamado show, que será um valor lógico (opcional) indicando se será mostrado ou não na tela o processo de cálculo do factorial.'''
def factorial(num, show = False):
    """-> Calcula o factorial de um numero.

    Args:
        num (inteiro): O numero a ser calculado
        show (bool, optional): Paramaetro usado para mostrar ou nao a conta.

    Returns:
        Valor inteiro: O valor do factorial de um numero.
    """
    fact = 1
    for i in range(num, 0, -1):
        if show:
            print(i, end='')
            if i > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        fact *= i
    return fact


# Programa principal
print(factorial(5, True))
