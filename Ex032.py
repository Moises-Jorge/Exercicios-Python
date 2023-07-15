"""
    programa que leh um ano qualquer e mostra se ele é BISSEXTO.
        CONDIÇÕES PARA UM ANO BISSEXTO:
        * Deve ser divisível por 4;
        * Não pode terminar em 00(ex: 2100, 2200, 2300);
        * E se terminar com 00, deve ser divisível por 400 (ex: 2000)
"""
ano = int(input("Em que ano estamos?: "))

unidade = ano / 1 % 10
dezena = ano / 10 % 10

if (ano % 4 == 0) and (unidade != 0) or (dezena != 0) or (ano % 400 == 0):
    print("Este ano é BISSEXTO")
else:
    print("Este ano não é BISSEXTO")