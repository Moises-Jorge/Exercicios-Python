""" Metodos da classe servem para aceder/alterar os valores dos atributos da classe (valores que nao dependem das instancias). Usam o decorador "@classmethod" para os identificar e "cls" como primeiro argumento para referenciar a classe."""
class Produto:
    desconto = 0.10 # Atributo da classe (10% de desconto). Soh pode ser alterado ou acessado por um metodo da classe
    
    def __init__(self, nome: str, preco: float) -> None:
        self.nome = nome
        self.preco = preco
        
        
    # Metodo Normal, que opera sobre os atributos das instancias da classe (por isso usamos o self)
    def calcular_preco_com_desoconto(self) -> float:
        preco_com_desconto = self.preco * (1 - Produto.desconto)
        return preco_com_desconto
    
    
    @classmethod # Metodo da classe, atua sobre os atributos da classe. Pode acessa-los ou modifica-los
    def mudar_desconto(cls, novo_desconto: float) -> None:
        cls.desconto = novo_desconto
        
        
# Programa Principal
p1 = Produto('Celular', 5000)
print(p1.calcular_preco_com_desoconto())

p1.mudar_desconto(0.20)
print(p1.calcular_preco_com_desoconto())