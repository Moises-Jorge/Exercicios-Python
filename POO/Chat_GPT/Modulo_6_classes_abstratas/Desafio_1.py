from abc import ABC, abstractmethod

class Veiculo(ABC):
    def __init__(self, marca: str, modelo:str, ano: int) -> None:
        self.__marca = marca.title()
        self.__modelo = modelo.title()
        self.__ano = ano
        
        
    @property
    def marca(self) -> str:
        return self.__marca
    @property
    def modelo(self) -> str:
        return self.__modelo
    @property
    def ano(self) -> int:
        return self.__ano
    
    
    @abstractmethod
    def tipo_combustivel(self) -> str:
        pass
    
    
class Carro(Veiculo):
    def tipo_combustivel(self) -> str:
        return 'Gasolina/Diesel'
    
    
class Moto(Veiculo):
    def tipo_combustivel(self) -> str:
        return 'Gasolina'
    
    
class Barco(Veiculo):
    def tipo_combustivel(self) -> str:
        return 'Diesel'
    
    
# Testando:
carro = Carro('Toyota', 'Corolla', 2024)
moto = Moto('Honda', 'Jorge', 2025)
barco = Barco('Chata', 'Mary', 2025)
print(f'Carro: {carro.marca} {carro.modelo}, Combustivel: {carro.tipo_combustivel()}')
print(f'Moto: {moto.marca} {moto.modelo}, Combustivel: {moto.tipo_combustivel()}')
print(f'Barco: {barco.marca} {barco.modelo}, Combustivel: {barco.tipo_combustivel()}')