import pygame


class Pokemon:
	def __init__(self):
		self._running = False

	def run(self):
		self._running = True
		pygame.init()
		self._window = pygame.display.set_mode((600, 600))

		# Game loop we can make this better I think
		while self._running:
			# Just checks to see if user clicked the "X" on the top
			# right of the window
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					self._running = False
		pygame.quit()

if __name__ == '__main__':
	Pokemon().run()
	print("in main")
    
