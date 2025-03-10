class Pessoa:
    def __init__(self, nome: str, idade: int) -> None:
        self.__nome = nome.title()
        self.__idade = idade
        
        
    @property # == @nome.getter
    def nome(self) -> str:
        return self.__nome
    
    @nome.setter
    def nome(self, novo_nome: str) -> None:
        if isinstance(novo_nome, str) and len(novo_nome) > 2:
            self.__nome = novo_nome
        else:
            print('O nome deve ser uma string com mais de dois caracteres!')
            
            
    @property
    def idade(self) -> int:
        return self.__idade
    
    @idade.setter
    def idade(self, nova_idade: int) -> None:
        if isinstance(nova_idade, int) and nova_idade > 0:
            self.__idade = nova_idade
        else:
            print('Idade Ivanlida!')
        
        
# Programa Principal:
p = Pessoa('Marcos', 27)
print(f'Nome: {p.nome}\nIdade: {p.idade}')
print()
p.nome = "Marta"
p.idade = 18
print(f'Nome: {p.nome}\nIdade: {p.idade}')
