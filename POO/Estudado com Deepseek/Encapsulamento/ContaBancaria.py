# Encapsulamento: conceito de esconder os detalhes internos de uma classe (por meio de atributos e metods privados). Usamos o underscore (_) para indicar que um atributo ou metodo eh privado. Aqui entra o uso dos "getters e setters" para visualizar e alterar os dados da classe. EX:
class ContaBancaria:
    _titular = str()
    _saldo = int()
    
    def __init__(self, titular: str, saldo: float = 0) -> None:
        self._titular = titular
        self._saldo = saldo
        
    def get_titular(self) -> str:
        return self._titular
    def set_titular(self, titular: str) -> None:
        self._titular = titular
        
        
    def get_saldo(self) -> float:
        return self._saldo
    def set_saldo(self, valor: float) -> None:
        if valor > 0:
            self._saldo = valor
        else:
            print('Saldo nao pode ser negativo')


# Criando um objecto da classe ContaBancaria
conta = ContaBancaria('Carlos', 1000)
print(conta.get_saldo())
conta.set_saldo(1500)
print(conta.get_saldo())