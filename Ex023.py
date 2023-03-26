""" Programa que leh um numero no intervalo de [0, 9999] e mostra na tela cada um dos digitos separados. Ex:1834
    
    * Undidade: 4
    * Dezena: 3
    * Centena: 8
    * Milhar: 1
"""
numero = input("Digite um numero no intervalo [0, 9999]: ")

print("Unidade: " + numero[3])
print("Dezena: "  + numero[2])
print("Centena: " + numero[1])
print("Milhar: "  + numero[0])