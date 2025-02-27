class Jogador:
    def __init__(self, nome: str, idade: int) -> None:
        self.nome = nome.title()
        self.idade = idade

    def jogar(self) -> None:
        print(f'⚽ O jogador {self.nome} está jogando!')


class Estadio:
    def __init__(self, nome: str) -> None:
        self.nome = nome

    def exibir_info(self) -> None:
        print(f'🏟️ Estádio: {self.nome}')


class Time:
    def __init__(self, nome: str, nome_estadio: str) -> None:
        self.nome = nome.title()
        self.estadio = Estadio(nome_estadio)  # Composição: O estádio pertence ao time
        self.jogadores = []  # Lista para armazenar os jogadores

    def adicionar_jogador(self, jogador: Jogador) -> None:
        self.jogadores.append(jogador)
        print(f'✅ O jogador {jogador.nome} foi adicionado ao {self.nome}.')

    def listar_jogadores(self) -> None:
        print(f'\n🏆 Jogadores do {self.nome}:')
        if not self.jogadores:
            print("⚠️ Nenhum jogador no time ainda.")
        else:
            for indice, jogador in enumerate(self.jogadores, 1):
                print(f'{indice}. {jogador.nome} ({jogador.idade} anos)')

    def exibir_info(self) -> None:
        print(f'\n📢 Informações do {self.nome}:')
        self.estadio.exibir_info()
        self.listar_jogadores()


# 🎮 Programa Principal
jogador1 = Jogador('Lamine Yamal', 17)
jogador2 = Jogador('Raphinha', 27)
jogador3 = Jogador('Lewandowski', 38)

barcelona = Time('FC Barcelona', 'Spotify Camp Nou')
barcelona.adicionar_jogador(jogador1)
barcelona.adicionar_jogador(jogador2)
barcelona.adicionar_jogador(jogador3)

# Exibir informações completas do time
barcelona.exibir_info()
