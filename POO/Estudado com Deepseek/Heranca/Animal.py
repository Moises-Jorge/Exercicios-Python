# Heranca: conceito que permite que uma classe herde atributos (variaveis) e metodos de outra classe. EX:
class Animal: # Superclasse ou Classe Pai
    def __init__(self, nome: str) -> None:
        self.nome = nome
    
    def fazer_som(self): # Metod a ser sobrescrito (implementado) nas classes filhas
        pass


class Cachorro(Animal): # Subclasse ou Classe Filha
    def fazer_som(self):
        return "Au Au!" # Sobrescrevendo o metodo fazer_som para Cachorro


class Gato(Animal): # Outra Subclasse
    def fazer_som(self):
        return "Miau!"
    

# Criando os objectos
animal1 = Animal('Dino')
print(f'O {animal1.nome} eh um animal desconhecido e faz o seguinte som: {animal1.fazer_som()}')

cao = Cachorro('Rex')
print(f'O {cao.nome} eh um cachorro e faz o seguinte som: {cao.fazer_som()}')

gato = Gato('Mixa')
print(f'O {gato.nome} eh um gato e faz o seguinte som: {gato.fazer_som()}')