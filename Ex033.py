# Programa que lê 3 números e mostra qual é o maior e o menor

n1 = int(input("N1: "))
n2 = int(input("N2: "))
n3 = int(input("N3: "))

# Verificando o menor número 
menor = n1
if (n2 < n1) and (n2 < n3):
    menor = n3
if (n3 < n1) and (n3 < n2):
    menor = n3

# Verificando o maior número 
maior = n1
if (n2 > n1) and (n2 > n3):
    maior = n2
if (n3 > n1) and (n3 > n2):
    maior = n3

print("Todos os numeros sao iguais" if(n1 == n2 == n3) else "Maior Numero: {}\nMenor Numero: {}".format(maior, menor))