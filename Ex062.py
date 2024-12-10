''' Melhore o Desafio 061, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerra quando ele disser que quer mostrar 0 termos '''
print('-=' * 10)
print('    Gerador de PA')
print('-=' * 10)

primeiro_termo = int(input('Digite o primeiro termo: '))
razao = int(input('Razao da PA: '))
termo = primeiro_termo
total_termos = 0
n_termos = 10 # Comeca 10 porque no principio soh queremos mostrar os 10 primeiros termos

cont = 1
while n_termos != 0:
    total_termos += n_termos
    while cont <= total_termos:
        print(termo, end='-> ')
        termo += razao
        cont += 1
    print('PAUSA')

    n_termos = int(input('Quantos termos voce quer mostrar mais?: '))
print(f'Progressao finalizada com {total_termos} termos mostrados.')