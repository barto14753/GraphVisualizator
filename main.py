import pygame
import random
import time
from colors import Color
from menu import Menu
from graph import Graph

colors = Color()

WIDTH = 1100
HEIGHT = 600

BACKGROUND_COLOR = colors.white

def main():
	pygame.init()
	pygame.font.init()



	screen = pygame.display.set_mode((WIDTH, HEIGHT))
	G = Graph(screen)
	menu = Menu(G, screen, WIDTH, HEIGHT)


	running = True

	while running:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False
				pygame.quit()
				return 0
			elif event.type == pygame.MOUSEBUTTONDOWN:
				pos_x, pos_y = pygame.mouse.get_pos()
				menu.click(pos_x, pos_y)

		screen.fill(BACKGROUND_COLOR)
		G.draw()
		menu.draw()
		pygame.display.flip()



main()



