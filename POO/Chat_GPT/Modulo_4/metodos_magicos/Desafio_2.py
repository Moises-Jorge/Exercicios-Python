class Produto:
    def __init__(self, nome: str, preco: float) -> None:
        self.__nome = nome.title()
        self.__preco = preco
        
        
    @property
    def nome(self) -> str:
        return self.__nome
    
    @property
    def preco(self) -> float:
        return self.__preco
    
    
    def __str__(self) -> str:
        return f'{self.nome} custa: {self.preco:.2f} Kz.'
    
    
class Pedido:
    def __init__(self, cliente: str) -> None:
        self.__cliente = cliente.title()
        self.__itens = list()
        
        
    @property
    def cliente(self) -> str:
        return self.__cliente
    
    @property
    def itens(self) -> list[Produto]:
        return self.__itens
    
    
    def __str__(self) -> str:
        itens_str = "\n".join(str(item) for item in self.itens) # Usando compreecao de lista.
        return f'Pedido de {self.cliente}:\n{itens_str}'
    
    
    def adicionar_item(self, produto: Produto) -> None:
        self.itens.append(produto)
    
    
    def remover_item(self, produto: Produto) -> None:
        if produto in self.itens:
            self.itens.remove(produto)

        
    def __len__(self) -> int:
        return len(self.itens)
    
    
    def __getitem__(self, index: int) -> Produto:
        return self.itens[index]
    
    
# Teste:
prod1 = Produto('Pizza', 2000)
prod2 = Produto('Suco', 500)

pedido = Pedido('Carlos')
pedido.adicionar_item(prod1)
pedido.adicionar_item(prod2)

print(pedido)
print(f'Itens no pedido: {len(pedido)}')
print(f'Primeiro item: {pedido[0]}')