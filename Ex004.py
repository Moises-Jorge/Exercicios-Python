#Programa que leh um dado e mostra na tela informacoes previas sobre o mesmo
dado = input("\nDigite alguma coisa: ")

print("\n{} eh do tipo {}".format(dado, type(dado)))
print("Numero: ", dado.isnumeric())
print("Alfabeto: ", dado.isalpha())
print("Alfanumerico: ", dado.isalnum())