import pygame
import random
from colors import Color
import menu
import graph

colors = Color()

WIDTH = 1100
HEIGHT = 600

BACKGROUND_COLOR = colors.white

def main():
	pygame.init()
	pygame.font.init()

	screen = pygame.display.set_mode((WIDTH, HEIGHT))
	graph = graph.Graph(screen)
	menu = menu.Menu(screen, WIDTH, HEIGHT)


	running = True

	while running:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False
				pygame.quit()
		screen.blit(colors.black)
		menu.draw()
		pygame.display.flip()



main()



