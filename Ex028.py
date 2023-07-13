# programa que faça o computador “pensar” em número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu(acertou) ou perdeu(errou)

from random import randint
numPC = randint(0, 5)
numUsuario = int(input('Qual eh o numero escolhido pelo computador?: '))
print('\nO Computador escolheu o numero {}. Portanto...'.format(numPC))
print("Resposta Certa" if(numPC == numUsuario) else "Resposta Errada")