import sys
import os


# 2 - Implemente uma função txt_importer dentro do módulo file_management
# capaz de importar notícias a partir de um arquivo TXT, utilizando "\n"
# como separador.
def txt_importer(path_file):
    #  Caso o arquivo TXT não exista, deve ser exibida a mensagem
    # "Arquivo {path_file} não encontrado" na stderr, em que {path_file} é o
    # caminho do arquivo;
    if not os.path.isfile(path_file):
        return sys.stderr.write(f'Arquivo {path_file} não encontrado\n')
    #  Caso a extensão do arquivo seja diferente de .txt, deve ser exibida a
    # mensagem "Formato inválido" na stderr;
    elif not path_file.endswith('.txt'):
        return sys.stderr.write('Formato inválido\n')
    else:
        with open(path_file, mode='r') as file:
            # A função deve retornar uma lista contendo as linhas do arquivo
            # utilizando "\n" como separador.
            line_list = file.read().split('\n')
            print(f'\nvvv\nlista contendo linhas: {line_list}')
            return line_list
