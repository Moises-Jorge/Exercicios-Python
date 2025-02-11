try:
    a = int(input('Numerador: ')) # Para cada valor que estou tentando ler, pode ter um "try" para tratar do erro logo de cara.
    b = int(input('Denominador: '))
    res = a / b
except (TypeError, ValueError): # Capturando dois erros especificos
    print('Tivemos um problema com os tipos de dados que vc digitou.')
except ZeroDivisionError: # Capturando um erro especifico
    print('Nao eh possivel dividir um numero por zero')
except KeyboardInterrupt: # Capturando um erro especifico (quando o usuario abandona a execucao)
    print('O usuario preferiu nao informar os dados')
except Exception as erro: # Capturando um erro qualquer que possa ocorrer e atribuir a uma var para tratar.(captura generica de erros)
    print(f'O erro encontrado foi {erro.__cause__}')
else:
    print(f'O resultado eh {res:.1f}')
finally:
    print('Volte sempre! Muito obrigado!')