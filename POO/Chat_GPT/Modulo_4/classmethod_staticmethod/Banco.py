class Banco:
    taxa_juros = 0.05 # Taxa de 5%
    
    @classmethod
    def modificar_taxa_juros(cls, nova_taxa: float) -> None:
        cls.taxa_juros = nova_taxa
    
    
    @staticmethod
    def calcular_juros(valor: float) -> float:
        valor_com_juros = valor * Banco.taxa_juros
        return valor_com_juros
    
    
# Programa Principal
print(Banco.taxa_juros)
print(Banco.calcular_juros(100))
Banco.modificar_taxa_juros(0.10)
print(Banco.calcular_juros(100))
