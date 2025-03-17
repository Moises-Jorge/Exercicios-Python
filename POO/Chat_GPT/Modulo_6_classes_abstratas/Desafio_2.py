from abc import ABC, abstractmethod

# Simulando uma Interface
class MetodoPagamento(ABC):
    @abstractmethod
    def pagar(self, valor: float) -> None:
        pass
    
    
class CartaoCredito(MetodoPagamento):
    def pagar(self, valor: float) -> None:
        print(f'Pagamento de {valor} Kz realizado via Cartão de Crédito.')
        
        
class PayPal(MetodoPagamento):
    def pagar(self, valor: float) -> None:
        print(f'Pagamento de {valor} Kz realizado via PayPal.')
        
        
# Programa Principal
metodos_pagamento = [CartaoCredito(), PayPal()]
valores = [100, 200]

for metodo, valor in zip(metodos_pagamento, valores):
    metodo.pagar(valor)