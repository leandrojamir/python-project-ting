import pytest
from ting_file_management.priority_queue import PriorityQueue


#  6 - Implemente os testes para a classe PriorityQueue capaz de armazenar
# arquivos pequenos de forma prioritária
# Implemente em: tests/priority_queue/test_priority_queue.py
# Entenda a lógica da fila de prioridades:
#  Quando um arquivo prioritário (com menos de 5 linhas) é adicionado à fila
# de prioridades, este arquivo ficará "após" todos os arquivos prioritários
# já inseridos, mas ficará "antes" de todos os arquivos não-prioritários
# já inseridos.
#  Quando um arquivo não-prioritário (com 5 linhas ou mais) é adicionado
# à fila de prioridades, este arquivo ficará "após" todos os arquivos
# já inseridos.
# Exemplo:
# # Tamanhos dos arquivos, em ordem de inserção na fila:
# [9, 4, 2, 5, 7, 11, 3]
# # Tamanhos dos arquivos, em ordem de remoção da fila:
# [4, 2, 3, 9, 5, 7, 11]
def test_basic_priority_queueing():
    #  A classe PriorityQueue utiliza a implementação da classe Queue do
    # requisito 1 para armazenar arquivos pequenos com prioridade. Utilizando a
    # classe PriorityQueue, arquivos com menos de 5 linhas são armazenados de
    # forma prioritária na fila, o que impacta no resultado dos métodos
    # dequeue e search.
    #  Você deve implementar testes para a classe PriorityQueue, garantindo
    # que a lógica de prioridades é respeitada pelos métodos enqueue, dequeue
    # e search.
    Queue = PriorityQueue()
    Queue.enqueue(
        {
            "nome_do_arquivo": "4linhas",
            "qtd_linhas": 4,
            "linhas_do_arquivo": ["primeiro", "a", "ser", "removido"],
        }
    )
    assert len(Queue.high_priority) == 1
    assert len(Queue.regular_priority) == 0

    Queue.enqueue(
        {
            "nome_do_arquivo": "9ultimo",
            "qtd_linhas": 9,
            "linhas_do_arquivo": [
                "este",
                "deve",
                "ser",
                "ultimo",
                "estando",
                "depois",
                "do",
                "arquivo",
                "2linhas",
            ],
        }
    )
    assert len(Queue.high_priority) == 1
    assert len(Queue.regular_priority) == 1

    dequeue = Queue.dequeue()
    # TypeError: 'NoneType' object is not subscriptable
    assert dequeue is not None
    assert dequeue["linhas_do_arquivo"] == [
        "primeiro",
        "a",
        "ser",
        "removido",
    ]

    Queue.enqueue(
        {
            "nome_do_arquivo": "2linhas",
            "qtd_linhas": 2,
            "linhas_do_arquivo": ["duas", "linhas"],
        }
    )
    assert Queue.search(0)["linhas_do_arquivo"] == ["duas", "linhas"]
    assert Queue.search(1)["nome_do_arquivo"] == "9ultimo"

    # if index >= len(self.list):
    #     raise IndexError('Índice Inválido ou Inexistente')
    with pytest.raises(
        IndexError,
        match="Índice Inválido ou Inexistente",
    ):
        Queue.search(len(Queue) + 1)
