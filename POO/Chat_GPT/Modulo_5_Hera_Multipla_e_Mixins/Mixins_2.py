class VoadorMixin:
    def voar(self) -> None:
        print(f'{self.__class__.__name__} esta voando!')
        
        
class NadadorMixin:
    def nadar(self) -> None:
        print(f'{self.__class__.__name__} esta nadando!')
        
        
class Pato(VoadorMixin, NadadorMixin):
    def __init__(self, nome: str) -> None:
        self.nome = nome.title()
        
        
class Peixe(NadadorMixin):
    def __init__(self, nome: str) -> None:
        self.nome = nome.title()
        
        
# Programa Principal:
pato = Pato('Marcos')
peixe = Peixe('Nana')
pato.voar()
pato.nadar()
peixe.nadar()