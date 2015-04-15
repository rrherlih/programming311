#!/usr/bin/env python3

import sys

class Graphs:

	def __init__(self, graph):
		self.graph = graph

	def open_file(self, filename):
		try:
			return(open(filename))
		except:
			print("Error opening the graph.")
			sys.exit()

	def create_adj_list(self):
		self.fd = self.open_file(self.graph)
		num = int(self.fd.readline())
		adj_list = [None]
		for i in range(1, num + 1):
			adj_list.append(Vertex())

		while True:
			line = self.fd.readline().strip()
			if not line:
				break
			else:
				edge = self.edge_to_tuple(line)
				adj_list[edge[0]].add_adj(edge[1])
		return(adj_list)

	def bfs(self, vertex, adj_list):
		q = Queue()
		q.enqueue(vertex)
		adj_list[vertex].set_color(1)

		while q.is_empty() == False:
			u = q.get_front()
			c = adj_list[u].get_color()
			for v in adj_list[u].get_adjs():
				if c == 1:
					if adj_list[v].get_color() == 1:
						print("Not two-colorable")
						sys.exit()
					else:
						adj_list[v].set_color(0)
				if c == 0:
					if adj_list[v].get_color() == 0:
						print("Not two-colorable")
						sys.exit()
					else:
						adj_list[v].set_color(1)
				q.enqueue(v)
			q.dequeue()
	
	def color_graph(self):
		a = self.create_adj_list()
		self.bfs(1, a)
		print("This graph is two-colorable")

	def edge_to_tuple(self, edge):
		l = edge.split()
		return((int(l[0]), int(l[1])))
	
class Queue:

	def __init__(self):
		self.front = None
		self.back = None

	def enqueue(self, v):
		item = [v, None]
		if self.front == None:
			self.front = item
			self.back = item
		else:
			self.back[1] = item
			self.back = item

	def dequeue(self):
		v = self.front[0]
		self.front = self.front[1]
		return(v)

	def get_front(self):
		return(self.front[0])

	def is_empty(self):
		if self.front == None:
			return True
		else:
			return False

class Vertex:

	def __init__(self):
		self.color = -1
		self.adjs = []

	def get_num(self):
		return(self.num)

	def get_color(self):
		return(self.color)

	def set_color(self, color):
		self.color = color

	def get_adjs(self):
		return(self.adjs)

	def add_adj(self, adjacency):
		self.adjs.append(adjacency)

def main():
	g = Graphs(sys.argv[1])
	g.color_graph()

if __name__ == '__main__':
	main()