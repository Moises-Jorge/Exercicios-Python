""" Programa que leh um numero no intervalo de [0, 9999] e mostra na tela cada um dos digitos separados. Ex:1834
    
    * Undidade: 4
    * Dezena: 3
    * Centena: 8
    * Milhar: 1
"""
numero = int(input("Digite um numero no intervalo [0, 9999]: "))
unidade = numero / 1 % 10
dezena = numero / 10 % 10
centena = numero / 100 % 10
milhar = numero / 1000 % 10

print("Unidade: ", int(unidade))
print("Dezena: " , int(dezena))
print("Centena: ", int(centena))
print("Milhar: " , int(milhar))