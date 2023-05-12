from ting_file_management.file_management import txt_importer
import sys


#  3 - Implemente a função process no módulo file_process. Essa função deverá
# ser capaz de transformar o conteúdo da lista gerada pela função txt_importer
# em um dicionário que será armazenado dentro da Queue.
def process(path_file, instance):
    #  Deve-se ignorar arquivos que já tenham sido processados anteriormente
    # (ou seja, arquivos com o mesmo nome e caminho (nome_do_arquivo)
    # não devem ser readicionados a fila);
    if path_file in instance.list:
        return None
    else:
        #  A função irá receber como parâmetro um objeto instanciado da fila
        # implementada no requisito 1 e o caminho para um arquivo;
        #  A instância da fila recebida por parâmetro deve ser utilizada para
        # registrar o processamento dos arquivos;
        instance.enqueue(path_file)
        line_list = txt_importer(path_file)
        #  A função deve processar o arquivo passado por parâmetro, ou seja,
        # gerar um dicionário com o formato e informações especificadas abaixo
        # Exemplo da estrutura de saída:
        # {
        #     "nome_do_arquivo": "arquivo_teste.txt", # Caminho do arquivo
        #     "qtd_linhas": 3,                        # Quantidade de linhas
        #     "linhas_do_arquivo": [...]              # linhas retornadas req2
        # }
        dict_list = {
            "nome_do_arquivo": path_file,
            "qtd_linhas": len(line_list),
            "linhas_do_arquivo": line_list,
        }
        #  Após cada nova inserção válida, a função deve mostrar via "stdout"
        # os dados processados, conforme estrutura no exemplo.
        # https://acervolima.com/como-imprimir-em-stderr-e-stdout-em-python/
        # print(*a, file = sys.stdout)
        # unexpected spaces around keyword / parameter equalsFlake8(E251)
        print(dict_list, file=sys.stdout)


def remove(instance):
    """Aqui irá sua implementação"""


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
