def arquivo_existe(nome_arquivo) -> bool:
    """-> Funcao que recebe um arquivo e verifica se ele existe. A funcao tenta abrir e fechar logo de seguida; se conseguir realizar essa operacao, entao ela devolve "True" para indicar que o arquivo existe. Se nao conseguir, devolve "False" para indicar que o arquivo nao existe/nao foi encotrado

    Args:
        nome_arquivo (.txt): Nome do arquivo que se quer verificar

    Returns:
        bool: "True" -> Se o arquivo for encotrado. "False" -> Se o arquivo nao for encotrado
    """
    try:
        arquivo = open(nome_arquivo, 'rt') # rt -> "read text": abrir o arquivo em modo de leitura
        arquivo.close()
    except FileNotFoundError:
        return False
    else:
        return True
    

def criar_arquivo(nome_arquivo) -> None:
    """-> Funcao que cria um arquivo caso nao exista.

    Args:
        nome_arquivo (.txt): O nome do arquivo que serah criado
    """
    try:
        arquivo = open(nome_arquivo, 'wt+') # wt+ -> "write text": abrir o arquivo em modo de escrita. "+": cria o arquivo caso nao exista.
        arquivo.close()
    except:
        print('Houve um ERRO na criacao do arquivo')
    else:
        print(f'Arquivo {nome_arquivo} criado com sucesso!')
        
        
def ler_arquivo(nome_arquivo) -> None:
    """-> Funcao que mostra o conteudo do arquivo que eh passado como parametro

    Args:
        nome_arquivo (.txt): Arquivo cujo conteudo sera lido
    """
    from lib.interface import cabecalho
    try:
        arquivo = open(nome_arquivo, 'rt')
    except:
        print('Erro ao ler o arquivo!')
    else:
        cabecalho('PESSOAS CADASTRADAS')
        print(arquivo.read())