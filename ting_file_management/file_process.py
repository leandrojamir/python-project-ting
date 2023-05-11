#  3 - Implemente a função process no módulo file_process. Essa função deverá
# ser capaz de transformar o conteúdo da lista gerada pela função txt_importer
# em um dicionário que será armazenado dentro da Queue.
#  A função irá receber como parâmetro um objeto instanciado da fila
# implementada no requisito 1 e o caminho para um arquivo;

#  A instância da fila recebida por parâmetro deve ser utilizada para
# registrar o processamento dos arquivos;

#  A função deve processar o arquivo passado por parâmetro (ou seja, gerar um
# dicionário com o formato e informações especificadas abaixo);

#  Deve-se ignorar arquivos que já tenham sido processados anteriormente
# (ou seja, arquivos com o mesmo nome e caminho (nome_do_arquivo)
# não devem ser readicionados a fila);

#  Após cada nova inserção válida, a função deve mostrar via "stdout" os dados
# processados, conforme estrutura no exemplo abaixo.

# Exemplo da estrutura de saída:
# {
#     "nome_do_arquivo": "arquivo_teste.txt",
#     "qtd_linhas": 3,
#     "linhas_do_arquivo": [...]
# }


def process(path_file, instance):
    """Aqui irá sua implementação"""


def remove(instance):
    """Aqui irá sua implementação"""


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
