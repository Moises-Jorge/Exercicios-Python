class Funcionario:
    def __init__(self, nome: str, salario: float) -> None:
        self.nome = nome
        self.salario = salario
        
        
    def exibir_dados(self) -> None:
        print(f'Funcionario: {self.nome}')
        print(f'Salario: {self.salario:.2f} Kz')
        
        
class Gerente(Funcionario):
    def __init__(self, nome: str, salario: float, bonus: float) -> None:
        super().__init__(nome, salario)
        self.bonus = bonus
        
        
    def exibir_dados(self) -> None:
        super().exibir_dados()
        print(f'Bonus: {self.bonus:.2f} Kz')
        
        
class Estagiario(Funcionario):
    def __init__(self, nome: str, salario: float, horas_trabalhadas: int) -> None:
        super().__init__(nome, salario)
        self.horas_trabalhadas = horas_trabalhadas
        
        
    def exibir_dados(self) -> None:
        super().exibir_dados()
        print(f'Horas Trabalhadas: {self.horas_trabalhadas}')
        
        
# Programa Principal
funcionario1 = Funcionario('Esmael', 15000)
funcionario1.exibir_dados()
print()
gerente1 = Gerente('Pedro', 25000, 5000)
gerente1.exibir_dados()
print()
estagiario1 = Estagiario('Marcelo', 8000, 10)
estagiario1.exibir_dados()