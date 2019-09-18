import heapq

class Node(object):

	n = 0

	def __init__(self, board, prev_state = None):
		assert len(board) == 9

		self.board = board[:];
		self.prev = prev_state
		self.step = 0
		Node.n += 1

		if self.prev:
			self.step = self.prev.step + 1 

	def __eq__(self, other):
		"""Check wether two states are equal."""
		return self.board == other.board

	def __str__(self):
		string_list = [str(i) for i in self.board]
		sub_list = (string_list[:3], string_list[3:6], string_list[6:])
		return "\n".join([" ".join(l) for l in sub_list])
	
	
	def manhattan_heuristic(self,goal):
		"""Return Manhattan distance of state."""
		distance = 0
		for i in range(1,9):
			xs, ys = self.inpos(self.board.index(i))
			xg, yg = self.inpos(goal.index(i))
			distance += abs(xs-xg) + abs(ys-yg)
		return distance

	
	def displaced_tiles(self,goal):
		"""Return Displaced Tiles distance of state."""
		distance = 0
		for i in range(9):
			if goal[i] != self.board[i]: distance += 1
		return distance

	
	def next(self):
		"""Return next states from this state."""    
		next_moves = []
		i = self.board.index(0)
		next_moves = (self.shup(i), self.shdown(i), self.shleft(i), self.shright(i))
		return [s for s in next_moves if s]

	def shright(self, i):
		'''move blank right if possible'''
		x, y = self.inpos(i)
		if y < 2:
			right_state = Node(self.board, self)
			right = self.posin(x, y+1)
			right_state.swap(i, right)
			return right_state

	def shleft(self, i):
		'''move blank left if possible'''
		x, y = self.inpos(i)
		if y > 0:
			left_state = Node(self.board, self)
			left = self.posin(x, y - 1)
			left_state.swap(i, left)
			return left_state

	def shup(self, i):
		'''move blank up if possible'''
		x, y = self.inpos(i)
		if x > 0:
			up_state = Node(self.board, self)
			up = self.posin(x - 1, y)
			up_state.swap(i, up)
			return up_state

	def shdown(self, i):
		'''move blank down if possible'''
		x, y = self.inpos(i)
		if x < 2:
			down_state = Node(self.board, self)
			down = self.posin(x + 1, y)
			down_state.swap(i, down)
			return down_state

	def swap(self, i, j):
		'''swap elements'''
		self.board[j], self.board[i] = self.board[i], self.board[j]

	def inpos(self, index):
		'''get position from index no'''
		return (int(index / 3), index % 3)

	def posin(self, x, y):
		'''get index no from position'''
		return x * 3 + y
	 
