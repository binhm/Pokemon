import pygame


class Pokemon:
	def __init__(self):
		self._running = False
		self.keys = None
		self.player = Player()

	def run(self):
		self._running = True
		pygame.init()
		self._window = pygame.display.set_mode((600, 600))

		# Game loop we can make this better I think
		while self._running:
			pygame.time.delay(100)
			# Just checks to see if user clicked the "X" on the top
			# right of the window
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					self._running = False

			self.handle_events()

			self._window.fill((0, 0, 0))
			pygame.draw.rect(self._window, (255, 0, 0), (self.player.x, self.player.y, 
				self.player.width, self.player.height))
			pygame.display.update()

		pygame.quit()

	# function to handle movements	
	def handle_events(self):
		keys = pygame.key.get_pressed()

		if keys[pygame.K_UP]:
			self.player.y -= self.player.velocity
		if keys[pygame.K_DOWN]:
			self.player.y += self.player.velocity
		if keys[pygame.K_RIGHT]:
			self.player.x += self.player.velocity
		if keys[pygame.K_LEFT]:
			self.player.x -= self.player.velocity


class Player:
	def __init__(self):
		self.x = 300
		self.y = 300
		self.width = 40
		self.height = 50
		self.velocity = 10

if __name__ == '__main__':
	Pokemon().run()
	print("in main")
    
