class Pessoa:  
    def __init__(self, nome: str, idade: int) -> None:
        self.nome = nome
        self.idade = idade
        
       
    def apresentar(self) -> None:
        print(f'Ola, meu nome eh {self.nome} e tenho {self.idade} anos.')
        
    
# Criando um objecto da calsse Pessoa
pessoa1 = Pessoa('Moises', 27)
pessoa1.apresentar()
