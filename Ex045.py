''' Crie um programa que faca o computador jogar Jokenpô(PEDRA, PAPEL e TESOURA) com você. '''
from random import choice

lista_opcoes = ["PEDRA", "PAPEL", "TESOURA"]
escolha_pc = choice(lista_opcoes)
escolha_humano = str(input("Qual eh a sua escolha?: ")).upper()

print(f"O PC escolheu '{escolha_pc}'. Portanto:")

if escolha_pc == escolha_humano:
    print("EMPATE!")
elif (escolha_pc == "PEDRA" and escolha_humano == "PAPEL") or (escolha_pc == "PAPEL" and escolha_humano == "TESOURA") or (escolha_pc == "TESOURA" and escolha_humano == "PEDRA"):
    print("VC GANHOU!")
else:
    print("VC PERDEU!") # Se nao calhou na opcao de EMPATE ou na opcao em que o humano GANHA, entao o humano PERDEU!
