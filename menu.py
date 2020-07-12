import pygame
from colors import Color

pygame.init()
pygame.font.init()

colors = Color()

#BUTTON PARAMETERS
BUTTON_COLOR = colors.light_purple
BUTTON_PRESSED_COLOR = colors.light_green
BUTTON_WIDTH = 50
BUTTON_HEIGHT = 50
BUTTON_FONT = pygame.font.Font("font1.ttf", 20)
BUTTON_START_GAP = 100
BUTTON_GAP = 100
BUTTON_SECOND_GAP = 50

#MENU PARAMETERS
MENU_WIDTH = 800
MENU_COLOR = colors.white



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
		if not self.pressed and abs(pos_x - self.x) <= self.width and abs(pos_y - self.y) <= self.height:
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
	def __init__(self, screen, screen_width, screen_height):
		self.screen = screen
		self.screen_width = screen_width
		self.screen_height = screen_height
		self.color = MENU_COLOR
		self.add_top = Button(self.screen, "Add Top", MENU_WIDTH + BUTTON_SECOND_GAP, BUTTON_START_GAP)
		self.add_edge = Button(self.screen, "Add Edge", MENU_WIDTH + BUTTON_SECOND_GAP, BUTTON_START_GAP + BUTTON_GAP)
		self.delete_top = Button(self.screen, "Delete Top", MENU_WIDTH + BUTTON_SECOND_GAP, BUTTON_START_GAP + 2*BUTTON_GAP)
		self.delete_edge = Button(self.screen, "Delete Edge", MENU_WIDTH + BUTTON_SECOND_GAP, BUTTON_START_GAP + 3*BUTTON_GAP)

		self.buttons = [self.add_top, self.add_edge, self.delete_top, self.delete_edge]

	def click(self, pos_x, pos_y):
		for button in self.buttons:
			button.is_pressed(pos_x, pos_y)

	def draw_background(self):
		pygame.draw.rect(self.screen, self.color, [MENU_WIDTH, 0, self.screen_width-MENU_WIDTH, self.screen_height])

	def draw(self):
		self.draw_background()
		for button in self.buttons:
			button.draw()

