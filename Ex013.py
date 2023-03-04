# Programa que leh o salario de um funcionario e mostra o novo salario do mesmo com um aumento de 15% 
salario = float(input("Informe o seu salario: "))

novoSalario = salario + (salario * (15/100))

print("O seu novo salario eh: {}kz\n".format(novoSalario))