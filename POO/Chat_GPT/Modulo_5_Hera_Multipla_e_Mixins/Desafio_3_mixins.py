class LutadorMixin:
    def lutar(self) -> None:
        print(f'{self.__class__.__name__} esta lutando!')


class MagoMixin:
    def lancar_magia(self) -> None:
        print(f'{self.__class__.__name__} lancou magia!')
        
        
class Guerreiro(LutadorMixin):
    def __init__(self, nome: str) -> None:
        self.nome = nome.title()
        
        
class Feiticeiro(MagoMixin):
    def __init__(self, nome: str) -> None:
        self.nome = nome.title()
        
        
class Paladino(LutadorMixin, MagoMixin):
    def __init__(self, nome: str) -> None:
        self.nome = nome.title()
        
        
# Programa Principal
guerreiro = Guerreiro('Cratos')
feiticeiro = Feiticeiro('Rudeus')
paladino = Paladino('Poulos')

guerreiro.lutar()
feiticeiro.lancar_magia()
paladino.lutar()
paladino.lancar_magia()