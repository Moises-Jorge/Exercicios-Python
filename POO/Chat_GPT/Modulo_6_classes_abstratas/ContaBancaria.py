from abc import ABC, abstractclassmethod

class ContaBancaria(ABC):
    def __init__(self, titular: str, saldo: float) -> None:
        self.__titular = titular.title()
        self.__saldo = saldo
        
        
    @property
    def titular(self) -> str:
        return self.__titular
    @property
    def saldo(self) -> float:
        return self.__saldo
        
        
    @abstractclassmethod
    def calcular_juros(self) -> float:
        pass
    
    
class ContaPoupanca(ContaBancaria):      
    def calcular_juros(self) -> float:
        return self.saldo * 0.05 # Juros de 5%
    
    
class ContaCorrente(ContaBancaria):
    def calcular_juros(self) -> float:
        return self.saldo * 0.02 # Juros de 2%
    
    
# Testando
poupanca = ContaPoupanca('Marcelo', 1000)
corrente = ContaCorrente('Maria', 1000)

print(f'Juros da Poupanca: {poupanca.calcular_juros()} Kz')
print(f'Juros da Corrente: {corrente.calcular_juros()}')