class ContadorRegressivo:
    def __init__(self, n: int) -> None:
        self.n = n
        
        
        
    def __iter__(self):
        return self
    
    
    def __next__(self):
        if self.n <= 0:
            raise StopIteration
        self.n -= 1
        return self.n + 1
        
        
# Teste
contador = ContadorRegressivo(5)
for numero in contador:
    print(numero, end=' ')
    