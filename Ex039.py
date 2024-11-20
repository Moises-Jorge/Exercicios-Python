''' Faca um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade: 
    - Se ele ainda vai se alistar (se tiver menos de 18)
    - Se esta na hora de se alistar (se tiver 18)
    - Se ja passou do tempo do alistamento (se tiver mais de 18)
'''
from datetime import date

ano_nascimento = int(input("Em que ano vc nasceu?: "))
ano_actual = date.today().year
idade = ano_actual - ano_nascimento

if idade < 18:
    print(f"Voce ainda pode se alistar, faltam {18 - idade}", "anos" if ((18 - idade) > 1) else "ano", "para o seu alistamento.")
elif idade == 18:
    print(f"Esta na hora de se alistar, voce ja tem 18 anos!")
else:
    print(f"Voce ja passou do tempo do alistamento, ja se passaram {idade - 18} anos do prazo do seu alistamento!")
