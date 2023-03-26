# Programa que leh o nome de uma cidade e diga se ela comeca com o nome "SANTO"

cityName = str(input("Digite o nome de uma cidade: ")).upper()
cityNameToList = cityName.split() # Dividir o nome da cidade em uma lista strings para pegar o primeiro nome da cidade
const = "SANTO"

print(cityNameToList[0] in const)