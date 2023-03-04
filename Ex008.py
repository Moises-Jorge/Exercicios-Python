#Programa que recebe um valor em metros e o exibe em cm e mm
valor = float(input("Informe um valor(em metros): "))

print("{}m = {}km".format(valor, valor * 1000))
print("{}m = {}cm".format(valor, valor / 100))
print("{}m = {}mm\n".format(valor, valor / 1000))