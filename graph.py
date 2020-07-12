import pygame
import random
from colors import Color

colors = Color()

# GRAPH PARAMETERS
TOP_COLOR = colors.green
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


	def draw(self):
		pygame.draw.circle(self.screen, self.color, (self.x-self.radius, self.y-self.radius), self.radius)



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


	def 





