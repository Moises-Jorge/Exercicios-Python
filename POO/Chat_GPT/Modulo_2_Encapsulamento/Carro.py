class Carro:
    def __init__(self, marca: str, modelo: str, velocidade_max: int) -> None:
        self.__marca = marca.title()
        self.__modelo = modelo.title()
        self.__velocidade_max = velocidade_max
    
    
    def get_velocidade_max(self) -> int:
        return self.__velocidade_max
    def set_velocidade_max(self, velocidade: int) -> None:
        if velocidade > 0:
            self.__velocidade_max = velocidade
        else:
            print('ERRO! A velocidade nao pode ser inferior ou igual 0')
    
    
    
    def __str__(self) -> str:
        return f'Carro: {self.__marca} {self.__modelo} com velocidade maxima de {self.__velocidade_max} Km/h'
    
    
# Programa Principal
meu_carro = Carro('Toyota', 'Corolla', 180)
print(meu_carro.get_velocidade_max())
meu_carro.set_velocidade_max(-100)

print(meu_carro)