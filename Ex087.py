'''Aprimore o desafio anterior, mostrando no final:
    1. A soma de todos os valores pares digitados.
    2. A soma dos valores da terceira coluna.
    3. O maior valor da segunda linha
    Extra: Soma dos elementos da diagonal principal (basta igualar a linha e a coluna)'''
matriz = [[], [], []]
soma_total = soma_pares = soma_col_3 = maior_linha_2 = soma_diag_principal = 0
# Ciclo de leitura
for linha in range(3):
    for col in range(3):
        matriz[linha].append(int(input(f'Digite um valor para {[linha, col]}: ')))
print('-=' * 30)
# Ciclo para calculo e apresentacao dos resultados
for pos_mat, linha in enumerate(matriz):
    for pos_linha, num in enumerate(linha):
        print(f'[{num: ^5}] ', end='')
        soma_total += num
        if num % 2 == 0:
            soma_pares += num
        if pos_linha == 2: # equivale a coluna 3
            soma_col_3 += num
        if pos_mat == 1 and pos_linha == 0:
            maior_linha_2 = num
        elif pos_mat == 1 and num > maior_linha_2:
            maior_linha_2 = num
        if pos_mat == pos_linha: # somando soh os elementos da diagonal principal
            soma_diag_principal += num
    print()
print('-=' * 30)
print(f'A soma de todos os valores da matriz eh: {soma_total}')
print(f'A soma dos valores pares eh: {soma_pares}')
print(f'A soma dos valores da terceira coluna eh: {soma_col_3}')
print(f'O maior valor da segunda linha eh: {maior_linha_2}')
print(f'A soma dos elementos da diagonal principal eh: {soma_diag_principal}')