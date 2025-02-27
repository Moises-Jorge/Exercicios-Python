class Professor:
    def __init__(self, nome_professor: str) -> None:
        self.nome_professor = nome_professor
        
        
    def ensinar(self) -> None:
        print(f'O professor {self.nome_professor} esta ensinando.')
        
        
class Escola:
    def __init__(self, nome_escola: str) -> None:
        self.nome_escola = nome_escola
        self.professores = [] # Lista de Professores
        
        
    def adicionar_professor(self, professor: Professor) -> None:
        self.professores.append(professor)
        print(f'O professor {professor.nome_professor} foi adicionado com sucesso!')
    
    
    def listar_professores(self) -> None:
        print(f'Os Professores da escola {self.nome_escola} sao:')
        for indice, prof in enumerate(self.professores):
            print(f'{indice+1} - {prof.nome_professor}')
            
            
# Programa Principal
prof1 = Professor('Pembele')
prof2 = Professor('Catarina')
escola = Escola('Cmdt Loy')
escola.adicionar_professor(prof1)
escola.adicionar_professor(prof2)
escola.listar_professores()
prof1.ensinar()
