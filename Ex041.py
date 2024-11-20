''' A confederação nacional de natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
    - Ate 9 anos: MIRIM
    - Ate 14 anos: INFANTIL
    - Ate 19 anos: JUNIOR
    - Ate 20 anos: SENIOR
    - Acima: MASTER
'''
from datetime import datetime

ano_nascimento = int(input("Em que ano o atleta nasceu?: "))
ano_atual = datetime.now().year
idade = ano_atual - ano_nascimento

if idade <= 9:
    print(f"O Atleta tem {idade} anos de idade e pertence a Categoria MIRIM!")
elif idade <= 14:
    print(f"O Atleta tem {idade} anos de idade e pertence a Categoria INFANTIL!")
elif idade <= 19:
    print(f"O Atleta tem {idade} anos de idade e pertence a Categoria JUNIOR!")
elif idade <= 20:
    print(f"O Atleta tem {idade} anos de idade e pertence a Categoria SENIOR!")
else:
    print(f"O Atleta tem {idade} anos de idade e pertence a Categoria MASTER!")