""" Programa que leh o nome completo de uma pessoa e mostra: 

    * O nome com todas as letras maiúsculas;
    * O nome com todas as letras minúsculas;
    * Quantas letras ao todo(sem considerar os espaços)
    * Quantas letras tem o primeiro nome
"""
nome = str(input("Digite seu nome completo: "))
nameToList = nome.split()

print("1-", nome.upper())
print("2-", nome.lower())
print("3- {} letras ao todo".format(len(''.join(nome.split()))))
print("4- {} letras no primeiro nome!".format(len(nameToList[0])))