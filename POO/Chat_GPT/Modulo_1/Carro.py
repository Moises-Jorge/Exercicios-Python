class Carro:
    def __init__(self, marca: str, modelo: str, ano: int) -> None:
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
    
    
    def mostrar_dados(self) -> None:
        print(f'Carro: {self.marca} {self.modelo}, Ano: {self.ano}')
        

# Programa Principal
meu_carro = Carro('Toyota', 'Corolla', 2020)
meu_carro.mostrar_dados()