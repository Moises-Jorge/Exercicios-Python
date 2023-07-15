# Programa que pergunta o salário de um funcionário e calcula o seu aumento. Se o salário for superior à 100 000, o aumento é de 10%. Se for inferior, o aumento é de 15%

salario = float(input("Informe seu salario: "))

if(salario > 100000):
    salario = salario + (salario * 0.1)
else:
    salario = salario + (salario * 0.15)
print("Seu novo salario eh: ", salario)