import pygame
from colors import Color

pygame.init()
pygame.font.init()

colors = Color()

#BUTTON PARAMETERS
BUTTON_COLOR = colors.light_purple
BUTTON_PRESSED_COLOR = colors.red
BUTTON_WIDTH = 40
BUTTON_HEIGHT = 40
BUTTON_FONT = pygame.font.Font("font1.ttf", 15)
BUTTON_START_GAP = 80
BUTTON_GAP = 50
BUTTON_SECOND_GAP = 50

#MENU PARAMETERS
MENU_WIDTH = 800
MENU_COLOR = colors.light_green

#LABEL PARAMETERS
LABEL_FONT = pygame.font.Font("font1.ttf", 25)
LABEL_COLOR = colors.red



class Label:
	def __init__(self, screen, name, pos_x, pos_y, font=LABEL_FONT, color=LABEL_COLOR):
		self.screen = screen
		self.name = name
		self.font = font
		self.color = color
		self.x = pos_x
		self.y = pos_y

	def draw(self):
		text = self.font.render(self.name, True, self.color)
		self.screen.blit(text, (self.x, self.y))

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
		if not self.pressed and self.x <= pos_x <= self.x + self.width and self.y <= pos_y <= self.y + self.height:
			if not self.pressed:
				self.pressed = True
				self.color = BUTTON_PRESSED_COLOR
				return True
		else:
			self.pressed = False
			self.color = BUTTON_COLOR
			return False


	def draw(self):
		pygame.draw.rect(self.screen, self.color, [self.x, self.y, self.width, self.height])
		text = self.font.render(self.name, True, self.color)
		self.screen.blit(text, (self.x + self.width + 5, self.y + (self.height//4)))


class Menu:
	def __init__(self, graph, screen, screen_width, screen_height):
		self.graph = graph
		self.screen = screen
		self.screen_width = screen_width
		self.screen_height = screen_height
		self.color = MENU_COLOR
		self.title = Label(self.screen, "GraphVisualizator", MENU_WIDTH + BUTTON_SECOND_GAP - 5, 5)
		self.add_top = Button(self.screen, "Add Top", MENU_WIDTH + BUTTON_SECOND_GAP, BUTTON_START_GAP)
		self.add_edge = Button(self.screen, "Add Edge", MENU_WIDTH + BUTTON_SECOND_GAP, BUTTON_START_GAP + BUTTON_GAP)
		self.delete_top = Button(self.screen, "Delete Top", MENU_WIDTH + BUTTON_SECOND_GAP, BUTTON_START_GAP + 2*BUTTON_GAP)
		self.delete_edge = Button(self.screen, "Delete Edge", MENU_WIDTH + BUTTON_SECOND_GAP, BUTTON_START_GAP + 3*BUTTON_GAP)
		self.clear_tops = Button(self.screen, "Clear Tops", MENU_WIDTH + BUTTON_SECOND_GAP, BUTTON_START_GAP + 4*BUTTON_GAP)
		self.clear_edges = Button(self.screen, "Clear Edges", MENU_WIDTH + BUTTON_SECOND_GAP, BUTTON_START_GAP + 5*BUTTON_GAP)
		self.random_edges = Button(self.screen, "Random Edges", MENU_WIDTH + BUTTON_SECOND_GAP, BUTTON_START_GAP + 6*BUTTON_GAP)
		self.full_edges = Button(self.screen, "Full Edges", MENU_WIDTH + BUTTON_SECOND_GAP, BUTTON_START_GAP + 7*BUTTON_GAP)
		self.dfs = Button(self.screen, "DFS", MENU_WIDTH + BUTTON_SECOND_GAP, BUTTON_START_GAP + 8*BUTTON_GAP)
		self.bfs = Button(self.screen, "BFS", MENU_WIDTH + BUTTON_SECOND_GAP, BUTTON_START_GAP + 9*BUTTON_GAP)

		self.labels = [self.title]
		self.buttons = [self.add_top, self.add_edge, self.delete_top, self.delete_edge, 
						self.clear_tops, self.clear_edges, self.dfs, self.bfs, self.full_edges, self.random_edges]
		


	def is_focused_on_menu(self, pos_x, pos_y):
		if MENU_WIDTH < pos_x:
			return True
		return False

	def update_max_tops_pressed(self):
		if self.add_edge.pressed or self.delete_edge.pressed:
			self.graph.limit_pressed = 2
		else:
			self.graph.limit_pressed = 1

	def any_button_active(self):
		for button in self.buttons:
			if button.pressed:
				return True
		return False

	def click(self, pos_x, pos_y):
		if len(self.graph.tops) > 0:
			if self.graph.tops[0].visited:
				self.graph.reset_visited()
				
		if self.is_focused_on_menu(pos_x, pos_y):
			for button in self.buttons:
				button.is_pressed(pos_x, pos_y)

			if self.clear_tops.pressed:
				self.graph.clear_tops()
				self.clear_tops.pressed = False
				
			elif self.clear_edges.pressed:
				self.graph.clear_edges()
				self.clear_edges.pressed = False

			elif self.random_edges.pressed:
				self.graph.random_edges()

			elif self.full_edges.pressed:
				self.graph.full_edges()

			elif self.dfs.pressed:
				self.graph.DFS()

			elif self.bfs.pressed:
				self.graph.BFS()
			
		else:
			self.update_max_tops_pressed()
			self.graph.update_pressed(pos_x, pos_y)

			if self.add_top.pressed:
				self.graph.add_top(pos_x, pos_y)
				
			elif self.add_edge.pressed:
				self.graph.add_edge()
				
			elif self.delete_top.pressed:
				self.graph.delete_top(pos_x, pos_y)
				
			elif self.delete_edge.pressed:
				self.graph.delete_edge()

				


	def draw_background(self):
		pygame.draw.rect(self.screen, self.color, [MENU_WIDTH, 0, self.screen_width-MENU_WIDTH, self.screen_height])

	def draw(self):
		self.draw_background()
		for label in self.labels:
			label.draw()
		for button in self.buttons:
			button.draw()


