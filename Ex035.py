# Programa que lê o comprimento de 3 retas e diga ao usuário se elas podem ou não formar um triângulo
a = float(input("Informe a primeira reta: "))
b = float(input("Informe a segunda reta: "))
c = float(input("Informe a terceira reta: "))

if(a + b > c) and (a + c > b) and (b + c > a):
    print("Essas retas podem formar um triângulo!")
else:
    print("Essas retas nao podem formar um triângulo!")