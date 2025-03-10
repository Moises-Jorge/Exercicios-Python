class ContaBancaria:
    def __init__(self, titular: str, senha: str, saldo: float = 0) -> None:
        self.titular = titular.title()
        self._saldo = saldo
        self.__senha = senha
        
        
    def depositar(self, valor: float) -> None:
        if valor > 0:
            self._saldo += valor
            print('Deposito efetuado com sucesso!')
        else:
            print('ERRO: valor invalido!')
            
            
    def sacar(self, senha: str, valor: float) -> None:
        if self.__senha == senha and 0 < valor <= self._saldo:
            self._saldo -= valor
            print('Saque realizado com sucesso!')
        else:
            print('ERRO: Senha ou valor invalido!')
            
            
    def exibir_saldo(self) -> None:
        print(f'Saldo atual: {self._saldo} Kz')
        
        
# Programa Principal:
conta = ContaBancaria('Marcelo', '1234', 1000)
conta.exibir_saldo()
print()
conta.depositar(500)
conta.exibir_saldo()
print()
conta.sacar('1234', -1000)
conta.exibir_saldo()