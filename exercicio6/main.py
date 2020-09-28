# Faça um programa que leia 10 tarefas. Cada tarefa contém uma descrição
# (string) e uma prioridade (inteiro de 0 a 5. Utilizar classe ou estrutura para
# representar a tarefa). As tarefas devem ser inseridas em uma fila de prioridade.
# O programa deve imprimir as tarefas na tela de acordo com a sua prioridade.

import heapq

class FilaDePrioridade:

	def __init__(self):
		self._fila = []
		self._indice = 0

	def inserir(self, item, prioridade):
		heapq.heappush(self._fila, (-prioridade, self._indice, item))
		self._indice += 1

	def listar(self):
		for i in range(1, 10):
			print(heapq.heappop(self._fila)[-1])


class Tarefa:
	def __init__(self, nome):
		self.nome = nome

	def __repr__(self):
		return self.nome

fila = FilaDePrioridade()
fila.inserir(Tarefa(input('Escreva sua tarefa de grau de importância 3:')), 3)
fila.inserir(Tarefa(input('Escreva sua tarefa de grau de importância 5:')), 5)
fila.inserir(Tarefa(input('Escreva sua tarefa de grau de importância 1:')), 1)
fila.inserir(Tarefa(input('Escreva sua tarefa de grau de importância 4:')), 4)
fila.inserir(Tarefa(input('Escreva sua tarefa de grau de importância 3:')), 3)
fila.inserir(Tarefa(input('Escreva sua tarefa de grau de importância 2:')), 2)
fila.inserir(Tarefa(input('Escreva sua tarefa de grau de importância 1:')), 1)
fila.inserir(Tarefa(input('Escreva sua tarefa de grau de importância 5:')), 5)
fila.inserir(Tarefa(input('Escreva sua tarefa de grau de importância 2:')), 2)
fila.inserir(Tarefa(input('Escreva sua tarefa de grau de importância 5:')), 5)

fila.listar()