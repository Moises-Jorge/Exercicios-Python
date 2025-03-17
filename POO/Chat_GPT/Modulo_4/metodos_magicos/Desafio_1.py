class Filme:
    def __init__(self, titulo: str, diretor: str, duracao: int) -> None:
        self.__titulo = titulo.title()
        self.__diretor = diretor.title()
        self.__duracao = duracao
        
        
    @property
    def titulo(self) -> str:
        return self.__titulo
    @titulo.setter
    def titulo(self, novo_titulo: str) -> None:
        if isinstance(novo_titulo, str):
            self.__titulo = novo_titulo
        else:
            print('Titulo invalido')

    @property
    def diretor(self) -> str:
        return self.__diretor
    @property
    def duracao(self) -> int:
        return self.__duracao
        
        
    def __str__(self) -> str:
        return f'Filme: {self.titulo} de {self.diretor}.'
    
    def __len__(self) -> int:
        return self.duracao
    
    
# Teste:
film = Filme('A aranha', 'MJ', 1)
print(film)
print(f'Duracao: {len(film)}h')
