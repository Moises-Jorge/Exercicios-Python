class ContaBancaria:
    def __init__(self, titular: str, saldo: float = 0) -> None:
        self.__titular = titular.title()
        self.__saldo = saldo
        
        
    def get_titular(self) -> str:
        return self.__titular
    def set_titular(self, novo_titular: str) -> None:
        self.__titular = novo_titular
        
        
    def get_saldo(self) -> float:
        return self.__saldo
    def set_saldo(self, valor: float) -> None:
        if valor >= 0:
            self.__saldo = valor
        else:
            print('ERRO! Saldo invalido.')
            
            
    def depositar(self, valor: float) -> None:
        if valor >= 0:
            self.__saldo += valor
            print(f'Deposito de {valor} Kz efetuado com sucesso na conta de {self.__titular}!')
        else:
            print('Saldo invalido')
            
            
    def sacar(self, valor: float) -> None:
        if 0 < valor <= self.__saldo:
            self.__saldo -= valor
            print(f'Saque de {valor} Kz efetuado com sucesso na conta de {self.__titular}!')
        else:
            print('Saque nao permitido. Saldo insuficiente ou valor invalido!')
    
    
    def transferir(self, destino: "ContaBancaria", valor: float) -> None:
        if 0 < valor <= self.__saldo:
            self.sacar(valor)        
            destino.depositar(valor)
            print(f'Transferencia de {valor} Kz para {destino.get_titular()} efetuado com sucesso!')
        else:
            print('Transferencia nao permitida. Saldo insuficiente ou valor invalido!')
            
    def __str__(self) -> str:
        return f'O titular dessa conta é {self.__titular} e tem {self.__saldo} Kz.'
            
            
# Programa Principal
conta1 = ContaBancaria('Mauro', 1500)
conta2 = ContaBancaria('Miguel', 500)
conta1.transferir(conta2, 2000)

print(conta1)
print(conta2)