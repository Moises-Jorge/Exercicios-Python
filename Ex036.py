# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. O programa vai perguntar o valor da casa, o salario do comprador e em quantos anos ele vai pagar.
valor_casa = float(input('Informe o valor da casa: ')) # Valor da Casa = Valor Financiado (VF)
salario = float(input('Informe o salario: '))
anos_a_pagar = int(input('Em quantos anos pretende pagar?: '))

num_parcelas = anos_a_pagar * 12 # 1 ano = 12 meses. Transformando em meses a quantidade de anos
prestacao = valor_casa / num_parcelas
print(f"Prestacao Mensal: {prestacao:.2f}")

if prestacao > salario * 0.3:
    print("Emprestimo NEGADO!")
else:
    print("Emprestimo CONCEDIDO!")