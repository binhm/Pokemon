## execute everything
import pokemon
import pygame
import pytmx


_INITIAL_BACKGROUD_WIDTH = 300
_INITIAL_BACKGROUD_HEIGHT = 300


if __name__ == '__main__':
	pygame.init()
	pygame.display.set_caption('Pokemon')
	WINDOW = pygame.display.set_mode((_INITIAL_BACKGROUD_WIDTH, _INITIAL_BACKGROUD_HEIGHT), pygame.RESIZABLE)

	## the game
	pokemon.Pokemon(WINDOW).run()
	