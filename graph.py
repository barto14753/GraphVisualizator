import pygame
import random
import math
from colors import Color

pygame.init()
pygame.font.init()

colors = Color()

# GRAPH PARAMETERS
TOP_COLOR = colors.green
TOP_RADIUS = 15

#EDGE PARAMETERS
EDGE_COLOR = colors.blue
EDGE_WIDTH = 2
EDGE_BASE_FLOW = 10

#BUTTON PARAMETERS
BUTTON_COLOR = colors.orange
BUTTON_PRESSED_COLOR = colors.light_green
BUTTON_WIDTH = 50
BUTTON_HEIGHT
BUTTON_FONT = pygame.font.Font("font1.ttf", 32)


#MENU PARAMETERS
MENU_WIDTH = 800



class Button:
	def __init__(self, screen, name, pos_x, pos_y, width=BUTTON_WIDTH, height=BUTTON_HEIGHT, color=BUTTON_COLOR, font=BUTTON_FONT):
		self.screen = screen
		self.name = name
		self.font = font
		self.x = pos_x
		self.y = pos_y
		self.width = width
		self.height = height
		self.color = color
		self.pressed = False

	def is_pressed(self, pos_x, pos_y):
		if pos_x - self.x <= self.width and pos_y - self.y <= self.height:
			self.pressed = True
			return True
		else:
			self.pressed = False
			return False

	def draw(self):
		pygame.draw.rect(self.surface, self.color, [self.x, self.y, self.width, self.height])
		text = self.font.render(self.name, Truen, self.color)
		self.screen.blit(text, (self.x + self.width, self.y))




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


	def draw(self):
		pygame.draw.line(self.screen, self.color, (self.start_x,self.start_y),
			(self.end_x,self.end_y), self.width)



class Graph:
	def __init__(self, screen):
		self.screen = screen
		self.tops = []
		self.edges = []


class Menu:
	def __init__(self, screen):
		self.screen = screen
		self.add_top = Button(self.screen, )






