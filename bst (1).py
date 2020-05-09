class Node:

	def __init__(self, label):
		self.label = label
		self.left = None
		self.right = None

	def getLabel(self):
		return self.label

	def setLabel(self, label):
		self.label = label

	def getLeft(self):
		return self.left

	def setLeft(self, left):
		self.left = left

	def getRight(self):
		return self.right

	def setRight(self, right):
		self.right = right

class BinarySearchTree:

	def __init__(self):
		self.root = None

	def insert(self, label):

		# cria um novo nó
		node = Node(label)

		# verifica se a árvore está vazia
		if self.empty():
			self.root = node
		else:

			# árvore não vazia, insere recursivamente

			dad_node = None
			curr_node = self.root

			while True:

				if curr_node != None:

					dad_node = curr_node

					# verifica se vai para esquerda ou direita
					if node.getLabel() < curr_node.getLabel():
						# vai para esquerda
						curr_node = curr_node.getLeft()
					else:
						# vai para direita
						curr_node = curr_node.getRight()
				else:

					# se curr_node é None, então encontrou onde inserir

					if node.getLabel() < dad_node.getLabel():
						dad_node.setLeft(node)
					else:
						dad_node.setRight(node)

					break # sai do loop

	def empty(self):
		if self.root == None:
			return True
		return False

	# mostra em pré-ordem (raiz-esq-dir)
	def show(self, curr_node):

		if curr_node != None:
			print('%d' % curr_node.getLabel(), end=' ')
			self.show(curr_node.getLeft())
			self.show(curr_node.getRight())

	def getRoot(self):
		return self.root

	def remove(self, label):
		'''
			3 casos

			Caso 1
			o nó a ser removido não tem filhos
			esse caso é simples, basta setar a ligação
			do pai para None

			Caso 2
			o nó a ser removido tem somente 1 filho
			basta colocar o seu filho no lugar dele

			Caso 3
			o nó a ser removido possui dois filhos
			basta pegar o menor elemento da subárvore à direita
		'''

		dad_node = None # parent
		curr_node = self.root

		while curr_node != None:

			# verifica se encontrou o nó a ser removido
			if label == curr_node.getLabel():

				# caso 1: o nó a ser removido não possui filhos (nó folha)
				if curr_node.getLeft() == None and curr_node.getRight() == None:

					# verifica se é a raiz
					if dad_node == None:
						self.root = None
					else:
						# verifica se é filho à esquerda ou à direita
						if dad_node.getLeft() == curr_node:
							dad_node.setLeft(None)
						elif dad_node.getRight() == curr_node:
							dad_node.setRight(None)

				# caso 2: o nó a ser removido possui somente um filho
				elif (curr_node.getLeft() == None and curr_node.getRight() != None) or \
					(curr_node.getLeft() != None and curr_node.getRight() == None):

					# verifica se o nó a ser removido é a raiz
					if dad_node == None:
						# verifica se o filho de curr_node é filho à esquerda
						if curr_node.getLeft() != None:
							self.root = curr_node.getLeft()
						else: # senão o filho de curr_node é filho à direita
							self.root = curr_node.getRight()
					else:
						# se não for a raiz...
						pass


t = BinarySearchTree()
t.insert(8)
t.insert(3)
t.insert(1)
t.insert(6)
t.insert(4)
t.insert(7)
t.insert(10)
t.insert(14)
t.insert(13)

t.show(t.getRoot())