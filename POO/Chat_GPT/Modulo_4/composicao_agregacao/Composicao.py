class Motor:
    def __init__(self, potencia: int) -> None:
        self.potencia = potencia
        
        
    def ligar(self) -> None:
        print('Motor Ligado!')
        
        
    def desligar(self) -> None:
        print('Motor desligado!')
        
        
class Carro:
    def __init__(self, marca: str, modelo: str, potencia_motor) -> None:
        self.marca = marca
        self.modelo = modelo
        self.motor = Motor(potencia_motor) # Composicao
        
        
    def exibir_info(self) -> None:
        print(f'Carro: {self.marca} {self.modelo}\nMotor: {self.motor.potencia} CV')
        
        
# Programa Principal
meu_carro = Carro('Toyota', 'Corolla', 100)
meu_carro.exibir_info() # Apresenta as informacoes do carro (vindo da classe Carro)
meu_carro.motor.ligar() # Apresenta informacao sobre o estado do motor (vindo da classe Motor)
                        # Se a instancia de carro for apagada, a instancia de motor tbm serah!
