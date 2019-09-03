## in charge of the new game
## select saved data, or start new game
## select characters
## select background
import pygame
import button 
from avatar_selection import AvatarSelection
from text import Text
_INITIAL_BACKGROUD_WIDTH = 300
_INITIAL_BACKGROUD_HEIGHT = 300

class intro:
	def __init__(self, window):
		self._window = window

	def run(self):
		self.start_menu()

	def start_menu(self):

		start = True
		w, h = self._window.get_size()
		
		start_logo = Text('Comic Sans MS', 50, 'Pokemon', (0, 0, 0), self._window, w / 2, h - (h - 50))
		sample_text = Text('Comic Sans MS', 20, 'Test', (0, 0, 0), self._window, 25, 20)
		new_game = button.Button(self._window, (25, 150, 100, 50),(0, 0, 0), 'New Game', 15, 'Comic Sans MS',
						 (255, 255, 255))
		load_game = button.Button(self._window, (150, 150, 100, 50), (0, 0, 0), 'Load Game', 15, 'Comic Sans MS',
						 (255, 255, 255))
		##================set the background of the game intro=====================================
		self._window.fill((255, 255, 255))		
		start_logo.create()
		##================set the background of the game intro=====================================

		# While user is in the start menu	
		while start == True:
			
			new_game.create()
			load_game.create()	

			if new_game.clicked():
				start = False
			if load_game.clicked():
				pass

			new_game.hover()
			load_game.hover()

			pygame.display.update()

			for event in pygame.event.get():
				mouse_pos = pygame.mouse.get_pos()

				if event.type == pygame.QUIT:
					start = False
					pygame.quit()
				if event.type == pygame.KEYDOWN:

					if event.key == pygame.K_RIGHT:
						pass
					elif event.key == pygame.K_RIGHT:
						pass

if __name__ == '__main__':

	pygame.init()
	pygame.display.set_caption('Pokemon')
	WINDOW = pygame.display.set_mode((_INITIAL_BACKGROUD_WIDTH, _INITIAL_BACKGROUD_HEIGHT), pygame.RESIZABLE)
	intro(WINDOW).run()
	pass