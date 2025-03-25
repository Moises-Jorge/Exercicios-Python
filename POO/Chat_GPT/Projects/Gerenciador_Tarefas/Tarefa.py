class Tarefa:
    def __init__(self, titulo: str, descricao: str = '', status: bool = False) -> None:
        self.__titulo = titulo.title()
        self.__descricao = descricao
        self.__concluida = status
        
        
    @property
    def titulo(self) -> str:
        return self.__titulo
    @property
    def descricao(self) -> str:
        return self.__descricao
    @property
    def concluida(self) -> bool:
        return self.__concluida
    
    
    def marcar_como_concluida(self) -> None:
        self.__concluida = True
        
        
    def __str__(self) -> str:
        estado = 'Concluída' if self.concluida else 'Pendente'
        return f'Tarefa: {self.titulo}\nDescrição: {self.descricao}\nEstado: {estado}'
        
 
if __name__ == '__main__':       
    # Teste
    t1 = Tarefa('Estudar', 'Ler e resolver as tarefas')
    print(t1)
    t1.marcar_como_concluida()
    print(f'\nApos conclusao:\n{t1}')
        