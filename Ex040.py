''' Crie um programa que leia duas notas de um aluno e calcule sua media, mostrando uma mensagem no final, de acordo com a media    atingida:
    - Media abaixo de 5: REPROVADO
    - Media entre 5 e 6.9: RECUPERACAO
    - Media 7 ou superior: APROVADO
'''

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
media = (nota1 + nota2) / 2

print(f"A sua Media foi: {media:.1f}")
if media < 5:
    print("REPROVADO")
elif media >= 5 and media < 7:
    print("RECUPERACAO")
else:
    print("APROVADO")
