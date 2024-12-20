'''Crie uma tupla preenchida com os 20 primeiros colocados da tabela do campeonato brasileiro de futebol, na ordem de colocação. Depois mostre:
    1. Apenas os 5 primeiros colocados.
    2. Os 4 últimos colocados da tabela.
    3. Uma lista com os times em ordem alfabética
    4. Em que posição na tabela está o time do Vasco da Gama.'''
tbl_brasileirao = ('Botafogo', 'Palmeiras', 'Flamengo', 'Fortaleza', 'Internacional', 'Sao Paulo', 'Corinthias', 'Bahia', 'Cruzeiro', 'Vasco da Gama', 
                   'EC Vitoria', 'Atletico-MG', 'Fluminense', 'Gremio', 'Juventude', 'Bragantino', 'Athletico-PR', 'Criciuma', 'Atletico-GO', 'Cuiaba')
# Impressao da tabela classificativa
print('-=' * 30)
print(f'Lista de times do Brasileirão: {tbl_brasileirao}')
# Os 5 primeiros do campeonato
print('-=' * 30)
print(f'Os 5 primeiros são: {tbl_brasileirao[:5]}')
# Os 4 ultimos do campeonato
print('-=' * 30)
print(f'Os 4 últimos são: {tbl_brasileirao[16:]}') # print(tbl_brasileirao[-4])
# Ordenando-os em ordem alfabetica
print('-=' * 30)
print(f'Time em ordem alfabética: {sorted(tbl_brasileirao)}')
# Posicao de um determinado time na tabela
print('-=' * 30)
print(f'O Vasco da Gama está na {tbl_brasileirao.index("Vasco da Gama") + 1}ª posição')