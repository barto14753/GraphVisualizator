import pygame
import random
import math
from colors import Color

pygame.init()
pygame.font.init()

colors = Color()

# GRAPH PARAMETERS
TOP_COLOR = colors.green
TOP_PRESSED_COLOR = colors.red
TOP_RADIUS = 15

#EDGE PARAMETERS
EDGE_COLOR = colors.blue
EDGE_WIDTH = 2
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


	def update_color(self):
		if self.pressed:
			self.color = TOP_COLOR
		else:
			self.color = TOP_PRESSED_COLOR

	def draw(self):
		self.update_color()
		pygame.draw.circle(self.screen, self.color, (self.x-self.radius, self.y-self.radius), self.radius)

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
		pygame.draw.line(self.screen, self.color, (self.start_x,self.start_y),
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
			new_edge = Edge(screen=self.screen, start_top=self.pressed[0], end_top=end_top[0])
			self.edges.append(new_edge)
			self.reset_pressed()


	def delete_top(self, pos_x, pos_y):
		for i in range(len(self.tops)):
			if self.tops[i].is_on_coursor(pos_x, pos_y):
				self.tops.pop(i)
				self.reset_pressed()
				return True
		return False

	def delete_edge(self):
		for i in range(len(self.edges)):
			if self.edges[i].is_focused(self.pressed[0], self.pressed[1]) or self.edges[i].is_focused(self.pressed[1], self.pressed[0]):
				self.edges.pop(i)
				self.reset_pressed()
				return True
		return False

	def draw(self):
		for edge in self.edges:
			edge.draw()
		for top in self.tops:
			top.draw()












