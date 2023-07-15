# Programa que lê 3 números e mostra qual é o maior e o menor

n1 = int(input("N1: "))
n2 = int(input("N2: "))
n3 = int(input("N3: "))

if(n1 >= n2) and (n1 >= n3) and (n2 > n3):
    maior = n1
    menor = n3
elif(n2 >= n1) and (n2 >= n3) and (n1 > n3):
    maior = n2
    menor = n3
elif(n3 >= n1) and (n3 >= n2) and (n1 > n2):
    maior = n3
    menor = n2
elif(n3 >= n1) and (n3 >= n2) and (n2 > n1):
    maior = n3
    menor = n1

print("Todos os numeros sao iguais" if(n1 == n2 == n3) else "Maior Numero: {}\nMenor Numero: {}".format(maior, menor))