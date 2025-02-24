# Classe base (superclasse)
class Veiculo:
    def __init__(self, marca: str, modelo: str) -> None:
        self.marca = marca
        self.modelo = modelo
        
    
    def exibir_info(self) -> None:
        print(f'Veiculo: {self.marca} {self.modelo} ')
        

# Classe derivada (subclasse)
class Carro(Veiculo):
    def __init__(self, marca: str, modelo: str, portas: int) -> None:
        super().__init__(marca, modelo) # Chama o construtor da superclasse e passa os parametros da subclasse pra la
        self.portas = portas
        
    
    # Sobrescrevendo o metodo que esta implementado na superclasse
    def exibir_info(self) -> None:
        super().exibir_info() # Reaproveita o metodo da superclasse e acrescenta partes que nao existe nela
        print(f'Portas: {self.portas}')
        
        
# Outra classe derivada 
class Moto(Veiculo):
    def __init__(self, marca: str, modelo: str, cilindradas: int) -> None:
        super().__init__(marca, modelo)
        self.cilindradas = cilindradas
        
        
    def exibir_info(self) -> None:
        super().exibir_info()
        print(f'Cilindradas: {self.cilindradas}')
        
        
# Criando um objecto da classe Carro
meu_carro = Carro('Toyota', 'Corolla', 4)
meu_carro.exibir_info()
minha_moto = Moto('Honda', 'ADV', 125)
minha_moto.exibir_info()