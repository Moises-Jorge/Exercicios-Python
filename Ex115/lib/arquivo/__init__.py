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
        arquivo = open(nome_arquivo, 'rt') # Abrindo o arquivo
    except:
        print('Erro ao ler o arquivo!')
    else:
        cabecalho('PESSOAS CADASTRADAS')
        for linha in arquivo: # Mostrando o conteudo do arquivo
            dado = linha.split(';') # Transformando cada linha em uma lista (eliminando o ;)
            dado[1] = dado[1].replace('\n', '') # Eliminando a quebra de linha
            print(f'{dado[0]:<30}{dado[1]:>3} anos')
    finally:
        arquivo.close() # Fechando o arquivo no final de tudo
        

def cadastrar_pessoa(nome_arquivo, nome: str = 'desconhecido', idade: int = 0) -> None:
    """-> Funcao que cadastra uma nova pessoa no arquivo

    Args:
        nome_arquivo (.txt): Arquivo onde sera armazenado os dados
        nome (str, optional): Nome da pessoa que vai ser cadastrada. Defaults to 'desconhecido'.
        idade (int, optional): Idade da pessoa que vai ser cadastrada. Defaults to 0.
    """
    try:
        arquivo = open(nome_arquivo, 'at') # at -> "append text": adicionar dados no arquivo
    except:
        print('Houve um ERRO na abertura do arquivo!')
    else:
        try:
            arquivo.write(f'{nome};{idade}\n')
        except:
            print('Houve um ERRO na hora de escrever os dados')
        else:
            print(f'Novo registro de {nome} adicionado!')
    finally:
        arquivo.close()