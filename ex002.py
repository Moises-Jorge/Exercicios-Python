# Programa que leh o dia, o mês e o ano de nascimento de uma passoa e mostra uma mensagem com a data fortmatada. Exemplo da solução: você nasceu no dia dd de mm de aaaa. Correto?

print('\nInforme sua data de nascimento!')
dia = int(input('dia: '))
mes = input('mes: ')
ano = int(input('ano: '))

print('Vc nasceu no dia {} de {} de {}. Correto?\n'.format(dia, mes, ano))