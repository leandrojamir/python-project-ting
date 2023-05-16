# Pacote ting_word_searches
#  7 - Implemente uma função exists_word, dentro do módulo word_search, que
# verifique a existência de uma palavra em todos os arquivos processados.


#  A função irá receber como parâmetros a palavra a ser buscada e a fila
# implementada no requisito 1;
# 'exists_word' is too complex (6)Flake8(C901)
def exists_word(word, instance):
    path_file = instance.list[0]

    with open(path_file, mode="r") as file:
        # Preciso retornar lista contendo as linhas do arquivo utilizando
        # um "\n" como separador igual foi no requisito 2 com split
        line_list = file.read().split("\n")

        #  A fila não deve ser modificada durante a busca. Ela deve permanecer
        # com os mesmos arquivos processados antes e depois da busca.
        # Ideia usar um loop e iterar sobre cada linha e nela verifica-se se
        # a "word" informada está presente, se tiver dou um append
        occurrences = []
        for index, line in enumerate(line_list):
            # A busca deve ser case insensitive
            # (não diferenciar maiúsculas e minúsculas);
            if word.lower() in line.lower():
                #  A função deve retornar uma lista com as informações de cada
                # arquivo e suas linhas em que a palavra foi encontrada
                # colocar +1 pois comecei do zero...
                occurrences.append({"linha": index + 1})

        #  Caso a palavra não seja encontrada em nenhum arquivo, deve-se
        # retornar uma lista vazia;
        if not occurrences:
            return []

        # Exemplo da estrutura de retorno:
        # [{
        #   "palavra": "de",
        #   "arquivo": "arquivo_teste.txt",
        #   "ocorrencias": [
        #     {
        #       "linha": 2
        #     },
        #     {
        #       "linha": 7
        #     }
        #   ]
        # }]
        result = {
            "palavra": word,
            "arquivo": path_file,
            "ocorrencias": occurrences,
        }

        return [result]


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
