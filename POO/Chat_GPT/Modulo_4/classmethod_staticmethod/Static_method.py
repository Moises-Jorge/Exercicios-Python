""" Metodos Estaticos sao metodos que nao modificam nada (nem classe e nem nas instancias) por isso nao recebem os parametros 'self e cls'. Eles servem apenas como funcoes auxiliares dentro das classes."""
class Calculadora:
    @staticmethod
    def somar(a: int = 0, b: int = 0) -> int:
        return a + b
    
    
    @staticmethod
    def subtrair(a: int = 0, b: int = 0) -> int:
        return a - b
    
    
# Programa Principal
print(Calculadora.somar(2, 5))
print(Calculadora.subtrair(5, 2))