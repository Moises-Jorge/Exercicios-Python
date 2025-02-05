from time import sleep

def contador(i, f, p): # Exemplo de docstrings
    """Faz uma contagem e mostra o resultado na tela

    Args:
        i (valor inteiro): valor inicial da contagem
        f (valor inteiro): valor final da contagem
        p (valor inteiro): valor do salto da contagem (o passo)
    """
    cont = i
    if cont <= f:
        while cont <= f:
            print(cont, end=' ', flush=True)
            sleep(.4)
            cont += p
        print('FIM!')
        

def teste(b): # Testando escopo de variaveis
    global a # Alterando o conteudo da variavel global dentro de um escopo local
    a = 8
    b += 4
    print(f'A dentro vale {a}')
    print(f'B dentro vale {b}')


# Programa Principal
#help(contador)
""" a = 5
teste(a)
print(f'A fora vale {a}') """
