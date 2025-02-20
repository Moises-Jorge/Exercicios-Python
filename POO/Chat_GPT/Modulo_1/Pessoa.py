class Pessoa:
    def __init__(self, nome: str, idade: int, profissao: str) -> None:
        self.nome = nome.title()
        self.idade = idade
        self.profissao = profissao.title()
        
        
    def apresentar(self) -> None:
        print(f'Ola, meu nome eh {self.nome}, tenho {self.idade} anos e sou {self.profissao} ')
        
        
    # Metodo que facilita a visualizacao dos objectos directamente
    def __str__(self) -> str:
        return f'{self.nome}, {self.idade} anos, {self.profissao}'
        
        
# Programa principal
p1 = Pessoa('Moises', 27, 'Programador')
p2 = Pessoa('Daniel', 27, 'Arquiteto')
p1.apresentar()
p2.apresentar()

print(p1)
print(p2)