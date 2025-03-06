class Animal:
    def __init__(self, nome: str) -> None:
        self.nome = nome
        
        
    def mover(self) -> None:
        print(f'{self.nome} esta se movendo!')


class Aquatico:
    def __init__(self) -> None:
        self.vive_na_agua = True
        
        
    def nadar(self) -> None:
        print('Esse animal pode nadar!')
        
        
class Sapo(Animal, Aquatico): # Herdando dados e comportamento de duas classes (isso eh Heranca Multipla)
    def __init__(self, nome: str) -> None:
        Animal.__init__(self, nome) # Construtor da superclasse Animal
        Aquatico.__init__(self) # Construtor da superclasse Aquatico
        
        
    def coaxar(self) -> None:
        print(f'{self.nome} esta coaxando!')
        
""" Outra Proposta alternativa a Heranca Multipla (Mas isso nao eh Heranca Multipla). Nos permite ter acesso aos metodos e atributo das duas classes
class Aquatico(Animal):
    def __init__(self, nome: str) -> None:
        super().__init__(nome)
        
        
    def nadar(self) -> None:
        print(f'{self.nome} pode nadar!')
        
        
class Sapo(Aquatico):
    def __init__(self, nome: str) -> None:
        super().__init__(nome)
        
        
    def coaxar(self) -> None:
        print(f'{self.nome} esta coaxando!') """
        
        
# Programa Principal
sapo = Sapo('Kermit')
sapo.mover() # Metodo da classe Animal
sapo.nadar() # Metodo da classe Aquatico
sapo.coaxar()# Metodo da classe Sapo
