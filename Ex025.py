# Programa que leh o nome completo de uma pessaoa e diga se ela tem "SILVA" no nome.

nome = str(input("Digite o nome completo de alguem: ")).upper()
const = "SILVA"

print("Existe {} no nome digitado?: {}".format(const, (const in nome)))