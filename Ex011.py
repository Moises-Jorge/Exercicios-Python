# Programa que leh a largura e altura de uma parede em metros, calcula a sua area e a quantidade de tinta necessaria para pinta-la, sabendo que cada litro de tinta, pinta uma area de 2m^2
largura = float(input("Informe a largura da parede(em metros): "))
altura = float(input("Informe a altura da parede(em metros): "))

area = largura * altura
qtdTintas = area / 2

print("\nA Area da parede eh: {}m^2\nE sera necessario {}L de tinta para pinta-la\n".format(area, qtdTintas))