""" 1 - Exemplo com Atributos Publicos:
class Pessoa:
    def __init__(self, nome: str, idade: int) -> None:
        # Os dois sao atributos publicos, podem ser acessados e modidificados de qualquer lugar
        self.nome = nome
        self.idade = idade
        
        
# Programa Principal
p = Pessoa('Lucas', 30)
print(p.nome) # Acessando directamente a nome
print(p.idade) # Acessando directamente a idade
print()
p.nome = 'Mateus' # Modificando o nome a partir do programa principal
p.idade = 25 # Modificando tembem a idade
print(p.nome) # Acessando directamente a nome
print(p.idade) # Acessando directamente a idade """

""" 2 - Exemplo com Atributos Protegidos:
class Pessoa:
    def __init__(self, nome: str, idade: int) -> None:
        # Os dois atributos sao protegidos, significa que soh podem ser alterados pela superclasse e suas filhas
        self._nome = nome
        self._idade = idade
        
        
# Programa Principal
p = Pessoa('Lucas', 30)
print(p._nome)
print(p._idade)
print()
p._nome = 'Mateus'
p._idade = 25
print(p._nome)
print(p._idade)
# Os dados ainda soa acessiveis, mas nao recomendados. O Python nao bloqueia o acesso, mas indica que os atributos nao devem ser alterados directamente. """

""" 3 = Exemplo com Atributos Privados:
class ContaBancaria:
    def __init__(self, titular: str, saldo: float = 0) -> None:
        # Os dois atributos aqui sao PRIVADOS, nao podem ser acessados fora da classe (nem mesmo nas subclasses)
        self.__titular = titular
        self.__saldo = saldo
    
    
# Programa Principal
conta = ContaBancaria('Carlos', 1000)
print(conta.__titular) # Vai dar ERRO, pois esses atributos sao privados e nao podem ser acessados fora da classe
print(conta.__saldo) # Agora ninguem pode modificar os dados directamente, garantindo maior seguranca. A unica forma de acessar os atributos privados eh usando os metodos "getter e setter". """

# 4 - Acessando atributos privados (unica forma):
class ContaBancaria:
    def __init__(self, titular: str, saldo: float = 0) -> None:
        self.__titular = titular
        self.__saldo = saldo
        
    
    # Metodo Getter para acessar o titular  
    def get_titular(self) -> str:
        return self.__titular
    # Metodo Setter para modificar o titular
    def set_titular(self, novo_titular: str) -> None:
        self.__titular = novo_titular
    
    
    # Metodo Getter para acessar o saldo
    def get_saldo(self) -> float:
        return self.__saldo
    # Metodo Setter para modificar o saldo (com controle)
    def set_saldo(self, novo_saldo: float) -> None:
        if novo_saldo >= 0:
            self.__saldo = novo_saldo
        else:
            print('Saldo invalido!')
            
            
# Programa principal
conta = ContaBancaria('Carlos', 1000)
print(conta.get_saldo()) # Acessando o saldo pelo metodo getter (unica forma)
conta.set_saldo(500) # Modificando o saldo pelo metodo setter
print(conta.get_saldo())
conta.set_saldo(-500)
# A vantagem de se usar atributos privados eh que podemos controlar como os atributos sao acessados e modificados