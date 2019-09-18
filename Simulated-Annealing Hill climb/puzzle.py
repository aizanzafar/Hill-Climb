
from time import time
import math
import random
from node import *

f3 = 3

class Puzzle(object):

	def __init__(self, start, goal):
		self.start = start
		self.goal = goal
		self.mat = []
		for i in range(3):
			self.mat.append(final_state[i][:])


	def solvable(self,file=f3):

		print("\nStart state:", file=f3)
		print(self.start, file=f3)
		g = Puzzle(start, goal)
		g.mat=final_state
		print("\nGoal state:", file=f3)
		print(self.goal, file=f3)

	def inPut(self):
		''' Input the Start State '''
		f = open('start.txt','r')
		self.mat = [[int(num) for num in line.split(' ')] for line in f]


	def print_path(self, state,file=f3):
		''' Print the (Sub)Optimal Path'''
		path = []
		while state:
			path.append(state)
			state = state.prev
		path.reverse()
		print ("(Sub)Optimal path:", file=f3)
		print("\n-->\n".join([str(state) for state in path]), file=f3)


	def hill_climbing_h1n(self,g,file=f3):
		"""Run hill climbing search based on Displaced Tiles h1(n) heuristics"""
		stack = [self.start]
		count = 0
		t = 1000
		while stack:
			state = stack.pop()
			count += 1
			if state == self.goal:
				print ("Solved.\n", file=f3)
				self.print_path(state,file=f3)
				break

			h_val = state.displaced_tiles(g)
			print('\nParent State:', file=f3)
			print(state, file=f3)
			print('h_val: {}'.format(h_val), file=f3)
			next_state = False
			print('\nNext State(s): ', file=f3)
			for s in state.next():
				h_val_next = s.displaced_tiles(g)
				print(s, file=f3)
				print('h_val_next: {} \n'.format(h_val_next), file=f3)
				if h_val_next < h_val:
					next_state = s
					h_val = h_val_next
					stack.append(next_state)
					break

			delta_e = h_val_next - h_val

			if not next_state:
				if random.random() < 1/(1 + math.exp(-delta_e/t)):
					next_state = s
					h_val = h_val_next
					stack.append(next_state)
					break
				t = .10 * t


			if not next_state:
				print ("Solution not found.\n", file=f3)
				self.print_path(state,file=f3)

		return count


	def hill_climbing_h2n(self,g,file=f3):
		"""Run hill climbing search based on Manhattan Distance h2(n) heuristics"""
		stack = [self.start]
		count = 0
		t = 1000

		while stack:
			state = stack.pop()
			count += 1
			if state == self.goal:
				print ("Solved.\n", file=f3)
				self.print_path(state, file=f3)
				break

			h_val = state.manhattan_heuristic(g)
			print('\nParent State:', file=f3)
			print(state, file=f3)
			print('h_val: {}'.format(h_val), file=f3)
			next_state = False
			print('\nNext State(s): ', file=f3)
			for s in state.next():
				h_val_next = s.manhattan_heuristic(g)
				print(s, file=f3)
				print('h_val_next: {} \n'.format(h_val_next), file=f3)
				if h_val_next < h_val:
					next_state = s
					h_val = h_val_next
					stack.append(next_state)
					break

			delta_e = h_val_next - h_val

			if not next_state:
				if random.random() < 1/(1 + math.exp(-delta_e/t)):
					next_state = s
					h_val = h_val_next
					stack.append(next_state)
					break
				t = .10 * t


			if not next_state:
				print ("Solution not found.\n", file=f3)
				self.print_path(state,file=f3)

		return count


	def hill_climbing_h3n(self,g,file=f3):
		"""Run hill climbing search based on h3(n)=h1(n)+h2(n) heuristics"""
		stack = [self.start]
		count = 0
		t = 1000

		while stack:
			state = stack.pop()
			count += 1
			if state == self.goal:
				print ("Solved.\n", file=f3)
				self.print_path(state,file=f3)
				break

			h_val = state.manhattan_heuristic(g)+state.displaced_tiles(g)
			print('\nParent State:', file=f3)
			print(state, file=f3)
			print('h_val: {}'.format(h_val), file=f3)
			next_state = False
			print('\nNext State(s): ', file=f3)
			for s in state.next():
				h_val_next = s.manhattan_heuristic(g)+s.displaced_tiles(g)
				print(s, file=f3)
				print('h_val_next: {} \n'.format(h_val_next), file=f3)
				if h_val_next < h_val:
					next_state = s
					h_val = h_val_next
					stack.append(next_state)
					break

			delta_e = h_val_next - h_val

			if not next_state:
				if random.random() < 1/(1 + math.exp(-delta_e/t)):
					next_state = s
					h_val = h_val_next
					stack.append(next_state)
					break
				t = .10 * t


			if not next_state:
				print ("Solution not found.\n", file=f3)
				self.print_path(state,file=f3)

		return count


if __name__ == "__main__":

	f3 = open('Output.txt', 'w')

	f1 = open('start1.txt','r')
	start_state = [[int(num) for num in line.split(' ')] for line in f1]
	s1 = sum(start_state,[])
	start = Node(s1)
	print('Start State:\n', start, file=f3)

	f2 = open('goal.txt','r')
	final_state = [[int(num) for num in line.split(' ')] for line in f2]
	g1 = sum(final_state,[])
	goal = Node(g1)
	print('Goal State:\n', goal, file=f3)

	p = Puzzle(start, goal)
	p.inPut()
	p.solvable(file=f3)


	print("\nBased on Displaced tiles h1(n) Heuristic SEARCH:", file=f3)

	start_time = time()
	c = p.hill_climbing_h1n(g1,file=f3)
	end_time = time()
	elapsed = end_time - start_time
	print ("\nNumber of states in the path: %d" % c, file=f3)
	print ("Number of states explored: %d" % Node.n, file=f3)
	print ("Total time taken: %s" % elapsed, file=f3)
	print("*************************************************", file=f3)

	Node.n=0

	print("\nBased on manhattan_heuristic h2(n) Heuristic SEARCH:", file=f3)

	start_time = time()
	c = p.hill_climbing_h2n(g1,file=f3)
	end_time = time()
	elapsed = end_time - start_time
	print ("\nNumber of states in the path: %d" % c, file=f3)
	print ("Number of states explored: %d" % Node.n, file=f3)
	print ("Total time taken: %s" % elapsed, file=f3)
	print("*************************************************", file=f3)

	Node.n=0

	print("\nFor h3(n)=h1(n)+h2(n) Heuristic SEARCH:", file=f3)

	start_time = time()
	c = p.hill_climbing_h3n(g1,file=f3)
	end_time = time()
	elapsed = end_time - start_time
	print ("\nNumber of states in the path: %d" % c, file=f3)
	print ("Number of states explored: %d" % Node.n, file=f3)
	print ("Total time taken: %s" % elapsed, file=f3)
	print("*************************************************", file=f3)
