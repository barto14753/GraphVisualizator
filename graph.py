import pygame
import random
import math
import time
from colors import Color
from queue import Queue

pygame.init()
pygame.font.init()

colors = Color()

# GRAPH PARAMETERS
TOP_COLOR = colors.green
TOP_VISITED_COLOR = colors.black
TOP_PRESSED_COLOR = colors.red
TOP_RADIUS = 15

#EDGE PARAMETERS
EDGE_COLOR = colors.blue
EDGE_VISITED_COLOR = colors.black
EDGE_WIDTH = 10
EDGE_BASE_FLOW = 10


class Top:
	def __init__(self, screen, index, value, pos_x, pos_y, radius=TOP_RADIUS, color=TOP_COLOR):
		self.screen = screen
		self.id = index
		self.value = value
		self.x = pos_x
		self.y = pos_y
		self.radius = radius
		self.color = color
		self.pressed = False
		self.visited = False

	def update_color(self):
		if self.pressed:
			self.color = TOP_COLOR
		else:
			self.color = TOP_PRESSED_COLOR

	def draw(self):
		self.update_color()
		pygame.draw.circle(self.screen, self.color, (self.x, self.y), self.radius)

	def raw_draw(self):
		pygame.draw.circle(self.screen, self.color, (self.x, self.y), self.radius)


	def is_on_coursor(self, pos_x, pos_y):
		if abs(self.x - pos_x) <= self.radius and abs(self.y - pos_y) <= self.radius:
			return True
		return False

	def is_focused(self, pos_x, pos_y):
		# it focus on top even if you dont click on it(small difference)
		if abs(self.x - pos_x) <= self.radius and abs(self.y - pos_y) <= self.radius:
			if self.pressed:
				self.pressed = False
			else:
				self.pressed = True
			return True
		return False


class Edge:
	def __init__(self, screen, start_top, end_top, color=EDGE_COLOR, width=EDGE_WIDTH, flow=EDGE_BASE_FLOW):
		self.screen = screen
		self.start_top = start_top
		self.end_top = end_top
		self.color = color
		self.width = width
		self.flow = flow
		self.start_x = self.start_top.x
		self.start_y = self.start_top.y
		self.end_x = self.end_top.x
		self.end_y = self.end_top.y

	def is_focused(self, start, end):
		if start is self.start_top and end is self.end_top:
			return True
		return False

	def draw(self):
		pygame.draw.aaline(self.screen, self.color, (self.start_x,self.start_y),
			(self.end_x,self.end_y), self.width)



class Graph:
	def __init__(self, screen):
		self.screen = screen
		self.tops = []
		self.edges = []
		self.ids = 0
		self.pressed = []
		self.limit_pressed = 1

	def update_pressed(self, pos_x, pos_y):
		for top in self.tops:
			if top.is_focused(pos_x, pos_y):
				top.pressed = True
				if top.pressed:
					if len(self.pressed) >= self.limit_pressed:
						self.pressed[0].pressed = False
						self.pressed.pop(0)
					self.pressed.append(top)
				else:
					for i in range(len(self.pressed)):
						if self.pressed[i] is top:
							self.pressed[i].pressed = False
							self.pressed.pop(i)

	def delete_edges_associated_with_delted_top(self, top):
		to_delete = []
		for i in range(len(self.edges)):
			if self.edges[i].start_top is top or self.edges[i].end_top is top:
				to_delete.append(i)
		for i in range(len(to_delete)-1, -1, -1):
			self.edges.pop(to_delete[i])

	def is_edge_already_exist(self):
		start = self.pressed[0]
		end = self.pressed[1]
		for edge in self.edges:
			if edge.start_top is start and edge.end_top is end or edge.start_top is end and edge.end_top is start:
				self.reset_pressed()
				return True

		return False

	def reset_pressed(self):
		for i in range(len(self.pressed)):
			self.pressed[0].pressed = False
			self.pressed.pop(0)

	def add_top(self, pos_x, pos_y, value=0):
		self.reset_pressed()
		new_top = Top(screen=self.screen, index=self.ids, value=value, pos_x=pos_x, pos_y=pos_y)
		self.tops.append(new_top)

	def add_edge(self):
		if len(self.pressed) < 2:
			return False
		else:
			if not self.is_edge_already_exist():
				new_edge = Edge(screen=self.screen, start_top=self.pressed[0], end_top=self.pressed[1])
				self.edges.append(new_edge)
				self.reset_pressed()

	def delete_top(self, pos_x, pos_y):
		for i in range(len(self.tops)):
			if self.tops[i].is_on_coursor(pos_x, pos_y):
				self.delete_edges_associated_with_delted_top(self.tops[i])
				self.tops.pop(i)
				self.reset_pressed()
				return True
		return False

	def delete_edge(self):
		if len(self.pressed) < 2:
			return False
		else:
			for i in range(len(self.edges)):
				if self.edges[i].is_focused(self.pressed[0], self.pressed[1]) or self.edges[i].is_focused(self.pressed[1], self.pressed[0]):
					self.edges.pop(i)
					self.reset_pressed()
					return True
			return False

	def clear_tops(self):
		for i in range(len(self.tops)):
			self.tops.pop()
		for i in range(len(self.edges)):
			self.edges.pop()

	def clear_edges(self):
		for i in range(len(self.edges)):
			self.edges.pop()

	def draw(self):
		for edge in self.edges:
			edge.draw()
		for top in self.tops:
			top.draw()

	def raw_draw(self):
		for edge in self.edges:
			edge.draw()
		for top in self.tops:
			top.raw_draw()


	def reset_visited(self):
		for top in self.tops:
			top.visited = False
			top.color = TOP_COLOR
		for edge in self.edges:
			edge.color = EDGE_COLOR

	def DFS(self):

		def dfs(self, top):
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					print("quit")
			top.visited = True
			top.color = TOP_VISITED_COLOR

			self.raw_draw()
			pygame.display.flip()
			time.sleep(0.5)

			for edge in self.edges:
				if edge.start_top is top:
					if not edge.end_top.visited:
						edge.color = EDGE_VISITED_COLOR
						dfs(self, edge.end_top)
				elif edge.end_top is top:
					if not edge.start_top.visited:
						edge.color = EDGE_VISITED_COLOR
						dfs(self, edge.start_top)
		if len(self.pressed) != 1:
			return False
		else:
			dfs(self, self.pressed[0])
			

	def BFS(self):
		if len(self.pressed) != 1:
			return False
		else:
			q = Queue()
			q.put(self.pressed[0])

			while not q.empty():
				self.raw_draw()
				pygame.display.flip()
				time.sleep(0.5)

				for event in pygame.event.get():
					if event.type == pygame.QUIT:
						return

				top = q.get()
				if not top.visited:
					top.visited = True
					top.color = TOP_VISITED_COLOR
					for edge in self.edges:
						if edge.start_top is top:
							q.put(edge.end_top)
							edge.color = EDGE_VISITED_COLOR
						elif edge.end_top is top:
							q.put(edge.start_top)
							edge.color = EDGE_VISITED_COLOR


















