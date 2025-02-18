class Carro:
    def __init__(self, marca: str, modelo: str) -> None:
        self.marca = marca
        self.modelo = modelo
    
    
    def exibir_info(self) -> None:
        print(f'Carro: {self.marca} {self.modelo}')
        

# Criando um objecto da classe Carro
meu_carro = Carro('Hyundai', 'Accent')
meu_carro.exibir_info()