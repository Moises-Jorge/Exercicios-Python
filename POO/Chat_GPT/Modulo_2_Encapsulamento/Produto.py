class Produto:
    def __init__(self, nome: str, preco: float, estoque: int) -> None:
        self.__nome = nome.title()
        self.__preco = preco
        self.__estoque = estoque
        
        
    @property
    def nome(self) -> str:
        return self.__nome
    
    @nome.setter
    def nome(self, novo_nome: str) -> None:
        if isinstance(novo_nome, str) and len(novo_nome) > 2:
            self.__nome = novo_nome.title()
        else:
            print('Nome invalido!')
            
            
    @property
    def preco(self) -> float:
        return self.__preco
    
    @preco.setter
    def preco(self, novo_preco: float) -> None:
        if isinstance(novo_preco, (int, float)) and novo_preco > 0:
            self.__preco = novo_preco
        else:
            print('Preço ivalido!')
            
            
    @property
    def estoque(self) -> int:
        return self.__estoque
    
    @estoque.setter
    def estoque(self, novo_estoque: int) -> None:
        if isinstance(novo_estoque, int) and novo_estoque >= 0:
            self.__estoque = novo_estoque
        else:
            print('Valor invalido!')
            
            
# Programa Principal
p1 = Produto('iPhone', 1000, 10)
print(f'Produto: {p1.nome}\nPreco: {p1.preco} KZ\nEstoque: {p1.estoque}\n')
p1.nome = 'Samsung'
p1.preco = 750.0
p1.estoque = 15
print(f'Produto: {p1.nome}\nPreco: {p1.preco} KZ\nEstoque: {p1.estoque}\n')