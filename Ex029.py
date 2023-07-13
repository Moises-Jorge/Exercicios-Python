# programa que lê a velocidade de um carro. Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar 100kz por cada km acima do limite.

velocidade = float(input('Informe a velocidade do carro: '))

if(velocidade > 80):
    multa = (velocidade - 80) * 100
    print('MULTADO!\nA sua multa eh de {}kz por ter excedido {}km da velocidade limite!'.format(multa, (velocidade - 80)))