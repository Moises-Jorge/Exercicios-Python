""" Um Mixin é uma classe que fornece funcionalidades extras sem ser uma entidade completa por si só (eh uma classe auxiliar).
Os Mixins são úteis quando queremos adicionar funcionalidades específicas a várias classes diferentes. Sao importantes porque tambem ajudam na reutilizacao de codigo.
"""
class RegistravelMixin:
    def registrar(self) -> None:
        print(f'{self.__class__.__name__} registrado com sucesso!')
        
        
class Usuario(RegistravelMixin):
    def __init__(self, nome: str) -> None:
        self.nome = nome.title()
        
        
class Produto(RegistravelMixin):
    def __init__(self, nome: str, preco: float) -> None:
        self.nome = nome.title()
        self.preco = preco
        
        
# Programa Principal
usuario = Usuario('Antonio')
usuario.registrar() # Usando o metodo do mixin

produto = Produto('Notebook', 3500)
produto.registrar()# Usando tambem o metodo do mixin