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
    
    
class GerenciadorTarefas:
    def __init__(self) -> None:
        self.__tarefas = list()
        
        
    @property
    def tarefas(self) -> list:
        return self.__tarefas
    
    
    def adicionar_tarefa(self, tarefa: Tarefa) -> None:
        self.__tarefas.append(tarefa)
        print('Tarefa adicionada com sucesso')
            
            
    def remover_tarefa(self, titulo: str) -> bool:
        for tarefa in self.__tarefas:
            if tarefa.titulo.lower() == titulo.lower():
                self.__tarefas.remove(tarefa)
                print('Tarefa removida com sucesso')
                return True
        print('Tarefa nao encotrada')
        return False
        
        
    def listar_tarefas(self) -> None:
        if not self.__tarefas:
            print('Nenhuma tarefa registrada')
        else:
            print('\nTODAS AS TAREFAS:')
            for ind, tarefa in enumerate(self.__tarefas, 1):
                print(f'{ind} - {tarefa.titulo} - {"Concluída" if tarefa.concluida else "Pendente"}')
        
 
if __name__ == '__main__':       
    # Teste
    t1 = Tarefa('Estudar', 'Ler e resolver as tarefas')
    t2 = Tarefa('Arrumar o Quarto', 'Varrer, limpar e organizar tudo')
    print(t1)
    t1.marcar_como_concluida()
    print(f'\nApos conclusao:\n{t1}\n')
    
    g1 = GerenciadorTarefas()
    g1.adicionar_tarefa(t1)
    g1.adicionar_tarefa(t2)
    g1.listar_tarefas()
    g1.remover_tarefa(t1.titulo)
    g1.listar_tarefas()
        