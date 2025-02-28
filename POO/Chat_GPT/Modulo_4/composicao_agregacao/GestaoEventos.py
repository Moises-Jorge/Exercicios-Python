class Participante:
    def __init__(self, nome: str, idade: int) -> None:
        self.nome = nome.title()
        self.idade = idade

    def __str__(self) -> str:
        return f'{self.nome} - {self.idade} anos'


class Organizador:
    def __init__(self, nome: str, cargo: str) -> None:
        self.nome = nome.title()
        self.cargo = cargo.title()

    def __str__(self) -> str:
        return f'{self.nome} - {self.cargo}'


class Evento:
    def __init__(self, nome: str, nome_organizador: str, cargo: str) -> None:
        self.nome = nome.title()
        self.organizador = Organizador(nome_organizador, cargo)  # Composição
        self.participantes = []  # Agregação

    def adicionar_participante(self, participante: Participante) -> None:
        self.participantes.append(participante)
        print(f'✅ {participante.nome} foi adicionado ao evento "{self.nome}".')

    def listar_participantes(self) -> None:
        print(f'\n🎟️ Participantes do evento "{self.nome}":')
        if not self.participantes:
            print('⚠️ Nenhum participante cadastrado.')
        else:
            for indice, participante in enumerate(self.participantes, 1):
                print(f'  {indice}. {participante}')

    def __str__(self) -> str:
        return f'\n📅 Evento: {self.nome}\n👨‍💼 Organizador: {self.organizador}\n'


# Programa Principal
evento = Evento('Conferência de Tecnologia', 'Alice', 'Gerente de Eventos')

p1 = Participante('João', 25)
p2 = Participante('Maria', 30)
p3 = Participante('Carlos', 28)

evento.adicionar_participante(p1)
evento.adicionar_participante(p2)
evento.adicionar_participante(p3)

print(evento)
evento.listar_participantes()
