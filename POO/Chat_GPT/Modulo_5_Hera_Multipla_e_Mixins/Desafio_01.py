class Funcionario:
    def __init__(self, nome_func: str, salario: float) -> None:
        self.nome = nome_func.title()
        self.salario = salario

    def exibir_dados(self) -> None:
        print(f'{self.__class__.__name__}: {self.nome} - Salário: {self.salario} Kz')

    def __str__(self) -> str:
        return f'{self.__class__.__name__}: {self.nome} - Salário: {self.salario} Kz'


class Programador(Funcionario):
    def __init__(self, nome_prog: str, salario: float, linguagem: str) -> None:
        super().__init__(nome_prog, salario)
        self.linguagem = linguagem

    def exibir_dados(self) -> None:
        super().exibir_dados()
        print(f'Linguagem: {self.linguagem}')


class Gerente(Funcionario):
    def __init__(self, nome_gerente: str, salario: float, equipe: list) -> None:
        super().__init__(nome_gerente, salario)
        self.equipe = equipe  # Lista de Funcionarios sob a gerência do Gerente

    def exibir_dados(self) -> None:
        super().exibir_dados()
        print(f'Equipe do gerente {self.nome}:')
        for indice, funcionario in enumerate(self.equipe, 1):
            print(f' {indice}. {funcionario.nome}')


class LiderTecnico(Programador, Gerente):
    def __init__(self, nome_func: str, salario: float, linguagem: str, equipe: list) -> None:
        super().__init__(nome_func, salario, linguagem)  # Chama a MRO correta
        self.equipe = equipe  # Define a equipe diretamente

    def exibir_dados(self) -> None:
        super().exibir_dados()
        print('Equipe do líder técnico:')
        for i, membro in enumerate(self.equipe, 1):
            print(f' {i}. {membro.nome}')


# Teste no Programa Principal
funcionario1 = Funcionario('Carlos', 5000)
programador1 = Programador('Ana', 7000, 'Python')
gerente1 = Gerente('Roberto', 12000, [funcionario1, programador1])
#lider1 = LiderTecnico('Marcos', 15000, 'JavaScript', [funcionario1, programador1])

print()
funcionario1.exibir_dados()
print()
programador1.exibir_dados()
print()
gerente1.exibir_dados()
print()
#lider1.exibir_dados()
