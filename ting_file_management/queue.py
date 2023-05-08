from ting_file_management.abstract_queue import AbstractQueue


# Pacote ting_file_management
# 1 - Implemente uma fila para armazenar os arquivos que serão lidos.
#  Preencha a classe Queue, presente no arquivo queue.py utilizando as
# estruturas vistas no módulo.
class Queue(AbstractQueue):
    #  A fila (Queue) deve ser uma estrutura FIFO, ou seja, o primeiro item a
    # entrar, deve ser o primeiro a sair. Utilize seus conhecimentos de
    # estruturas de dados para otimizar as operações implementadas.
    def __init__(self):
        self.list = list()

    #  O tamanho da fila deverá ser exposto utilizando o método __len__ que
    # permitirá, após implementado, o uso do comando len(instancia_da_fila)
    # para se obter o tamanho da fila.
    def __len__(self):
        return len(self.list)

    #  A fila deve implementar os métodos de inserção (enqueue)
    def enqueue(self, value):
        return self.list.append(value)

    #  A fila deve implementar os métodos de remoção (dequeue)
    def dequeue(self):
        return self.list.pop(0)

    #  A fila deve implementar os métodos de busca (search)
    def search(self, index: int):
        #  Na busca uma exceção do tipo IndexError com a seguinte mensagem:
        # "Índice Inválido ou Inexistente" deve ser lançada caso um índice
        # inválido seja passado. Para uma fila com N elementos, índices
        # válidos são inteiros entre 0 e N-1.
        if index >= len(self.list):
            raise IndexError('Índice Inválido ou Inexistente')
        elif index < 0:
            raise IndexError('Índice Inválido ou Inexistente')
        else:
            return self.list[index]
