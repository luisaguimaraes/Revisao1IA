# Faça um programa que leia 10 tarefas. Cada tarefa contém uma descrição
# (string) e uma prioridade (inteiro de 0 a 5. Utilizar classe ou estrutura para
# representar a tarefa). As tarefas devem ser inseridas em uma fila de prioridade.
# O programa deve imprimir as tarefas na tela de acordo com a sua prioridade.

import heapq

class Filadeprioridade;

    def __init__ (self):
        self._fila =[]
        self._indice=0

    def inserir (self,, item, prioridade):
        heapq.heappush(self._fila, (-prioridade, self._indice, item))
        self._indice +=1

    def remover (self):
        return heapq.heappop(self._fila)[-1]

class Pessoa:
    def __init__ (self, nome):
        self.nome=nome

    def __repr__(self):
        return self.nome

fila = Filadeprioridade
fila.inserir(Pessoa('Maria'),20)
fila.inserir(Pessoa('Pedro'),16)
fila.inserir(Pessoa('Felipe'),25)
fila.inserir(Pessoa('Carol'),23)

print(fila.remover())