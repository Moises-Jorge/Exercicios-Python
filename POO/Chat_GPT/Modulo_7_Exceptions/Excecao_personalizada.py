# Criando a Excecao personalizada
class SaldoInsuficienteError(Exception):
    def __init__(self, mensagem: str = 'Saldo Insuficiente para a trasacao') -> None:
        super().__init__(mensagem)
        
        
class ContaBancaria:
    def __init__(self, titular: str, saldo: float) -> None:
        self.__titular = titular.title()
        self.__saldo = saldo
        
        
    @property
    def titular(self) -> str:
        return self.__titular
    
    @property
    def saldo(self) -> float:
        return self.__saldo
    @saldo.setter
    def saldo(self, novo_saldo: float) -> None:
        if isinstance(novo_saldo, (float, int)) and novo_saldo >= 0:
            self.__saldo = novo_saldo
        else:
            raise SaldoInsuficienteError('Saldo Invalido!')
    
    
    def sacar(self, valor: float) -> None:
        if valor >= self.saldo:
            raise SaldoInsuficienteError(f'Erro: Saldo insuficiente! Saldo atual: {self.saldo} Kz')
        self.saldo -= valor
        print(f'Saque de {valor} Kz realizado com sucesso! Novo saldo: {self.saldo} Kz')
        
        
# Programa Principal
try:
    conta = ContaBancaria('Carlos', 1000)
    print(conta.saldo)
    conta.sacar(500)
except SaldoInsuficienteError as e:
    print(e)