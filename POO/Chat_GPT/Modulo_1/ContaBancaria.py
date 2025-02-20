class ContaBancaria:
    def __init__(self, titular: str, saldo: float = 0) -> None:
        self.titular = titular.title()
        self.saldo = saldo
        
        
    def depositar(self, valor: float) -> None:
        self.saldo += valor
        print(f'Depósito de {valor}Kz realizado na conta de {self.titular}.')
        
        
    def sacar(self, valor: float) -> None:
        if self.saldo >= valor:
            self.saldo -= valor
            print(f'Saque de {valor}Kz realizado na conta de {self.titular}.')
        else:
            print(f'Saque de {valor}Kz não permitido! Saldo insuficiente.')
            
            
    def mostrar_saldo(self) -> None:
        print(f'Saldo actual de {self.titular}: {self.saldo:.2f}Kz')
        
        
    def __str__(self) -> str:
        return f'{self.titular}, {self.saldo}'
    
    
# Programa Principal
conta1 = ContaBancaria('Marcos')
conta2 = ContaBancaria('Anselmo')

conta1.depositar(1000)
conta1.sacar(500)
conta1.mostrar_saldo()
print()
conta2.depositar(2000)
conta2.sacar(2500)
conta2.mostrar_saldo()