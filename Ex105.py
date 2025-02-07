'''Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um dicionário com as seguintes informações:
    1. Quantidade de notas
    2. A maior nota
    3. A menor nota
    4. A média da turma
    5. A situação (opcional)
    
    Adicione também as docstrings da função'''
def notas(*notas, sit = False):
    """Funcao para analisar notas e situacoes de varios alunos.

    Args:
        notas (numerico): total de notas recebidas (sem limites)
        sit (bool, optional): valor opcional, indicando se deve ou nao adicionar a situacao.

    Returns:
        dicionario: contem varias informacoes sobre a situacao da turma
    """
    dict_notas = dict()
    dict_notas["total"] = len(notas)
    dict_notas["maior"] = max(notas)
    dict_notas["menor"] = min(notas)
    dict_notas["media"] = sum(notas) / dict_notas["total"]
    if sit:
        if dict_notas["media"] < 5:
            dict_notas["situacao"] = "RUIM"
        elif dict_notas["media"] <= 7:
            dict_notas["situacao"] = "RECUPERACAO"
        else:
            dict_notas["situacao"] = "BOA"
    return dict_notas
        
    
    
# Programa principal
resp = notas(5.5, 9.5, 10, 6.5, sit=True)
print(resp)