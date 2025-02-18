class ContaBancaria:
    def __init__(self, titular: str, saldo: int = 0) -> None:
        self.titular = titular
        self.saldo = saldo
        

    def depositar(self, valor) -> None:
        self.saldo += valor
        print(f'Deposito de {valor} realizado. Novo saldo: {self.saldo}')
    
    
    def sacar(self, valor) -> None:
        if valor > self.saldo:
            print('Saldo insuficiente!')
        else:
            self.saldo -= valor
            print(f'Saque de {valor} realizado. Novo saldo: {self.saldo}')
            

# Criando um objecto da classe ContaBancaria
minha_conta = ContaBancaria('Moises', 1000)
minha_conta.depositar(500)
minha_conta.sacar(200)
minha_conta.sacar(2000)