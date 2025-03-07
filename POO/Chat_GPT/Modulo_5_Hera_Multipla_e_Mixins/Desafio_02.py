class Animal:
    def __init__(self, nome: str, idade: int) -> None:
        self.nome = nome.title()
        self.idade = idade
        
        
    def fazer_som(self) -> None:
        print(f'O {self.__class__.__name__.lower()} faz um som.')
        
        
    def __str__(self) -> str:
        return f'{self.__class__.__name__} chama-se: {self.nome}'
        
        
class Mamifero(Animal):
    def __init__(self, nome: str, idade: int, tem_pelos: bool = True) -> None:
        super().__init__(nome, idade)
        self.tem_pelos = tem_pelos
        
        
    def amamentar(self) -> None:
        print(f'\nO mamífero está amamentando.')
        
        
class Ave(Animal):
    def __init__(self, nome: str, idade: int, consegue_voar: bool = True) -> None:
        super().__init__(nome, idade)
        self.consegue_voar = consegue_voar
        
        
    def voar(self) -> None:
        if self.consegue_voar:
            print('\nA ave está voando.')
        else:
            print('\nEsta ave não pode voar.')
            
            
class Morcego(Mamifero, Ave):
    def __init__(self, nome: str, idade: int, tem_pelos: bool = True) -> None:
        Mamifero.__init__(self, nome, idade, tem_pelos) # Inicializando os atributos da primeira classe Mae.
        Ave.__init__(self, nome, idade, True)  # Morcegos sempre voam. Inicializando os atributos da segunda classe Mae.
        
        
    def fazer_som(self) -> None:
        print('\nO morcego emite ultrassons.')
            
            
# Programa Principal:
animal = Animal('Weezy', 4)
animal.fazer_som()
print(animal)

mamifero = Mamifero('Cao', 5)
mamifero.amamentar()
mamifero.fazer_som()
print(mamifero)

ave = Ave('Pato', 2)
ave.voar()
ave.fazer_som()

morcego = Morcego('Nela', 8)
morcego.fazer_som()
morcego.voar()
print(morcego)
