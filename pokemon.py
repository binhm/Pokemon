import pygame
import player

class Pokemon:
	def __init__(self):
		self._running = True
		self._pause = False
		self.keys = None
		self.player = player.Player()
		self._mousex, self._mousey = (0,0)

	def play(self):
		'''if the game is in the playing state'''

		while self._running:
			# print("Game is running")
			pygame.time.delay(100)
			# Just checks to see if user clicked the "X" on the top
			# right of the window
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					self.quit()
				elif event.type == pygame.MOUSEBUTTONDOWN:
					print("Mouse detected in play state")
					# if the user pressed the mouse
					### Not sure if we need this during the play state
					### Maybe if we click on something, we can get it's information??
					### Not sure, but doesn't need this
					self.handle_mouse()
			self.handle_play_events()

			### make a draw class
			# self._window.fill((66, 245, 72)) #color of grass, don't turn it on, might hurt ur eyes
			self._window.fill((0, 0, 0)) 
			pygame.draw.rect(self._window, (255, 0, 0), (self.player.x, self.player.y, 
				self.player.width, self.player.height))
			pygame.display.update()
	# def handle_pause_key_events():

	def pause(self):
		''' the pause state brings up the settings.
			So far, the setting includes exit, save, Pokedex(?), 
			Pokemon, Personal info (badges,etc), bags (items)'''

		### PROBLEM SO FAR IS THAT WHEN WE EXIT PLAY STATE WITH X
		### PAUSE FUNCTION IS CALLED BEFORE IT EXIT. 
		### NOT A MAJOR PROBLEM BUT PAUSE SHOULDN'T BE CALLED AT ALL
		### PUT IF ELSE STATEMENTS
		print("self.pause: pause state")

		setting = pygame.image.load('backgrounds/settings.png')
		self._window.blit(setting, (50,100))
		while self._pause == True:

			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					self.quit()
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_ESCAPE:
						'''
						if user pressed esc again, then exit
						pause state and resume the play state. The time wait prevent
						the game from registering the key too fast  
						'''
						self._pause = False
						self._running = True
						pygame.time.wait(250)
					elif event.key == pygame.K_DOWN:
						pass
					elif event.key == pygame.K_UP:
						pass
				if event.type == pygame.MOUSEBUTTONDOWN:
					### If we use mouse instead of keyboard
					### Checks to see the mouse click is within range of the option
					### make sure to draw the options
					self.handle_mouse()
					# pass 
			# self.handle_setting()
			pygame.display.update()
	def run(self):

		pygame.init()
		self._window = pygame.display.set_mode((600, 600))
		pygame.display.set_caption('Pokemon') # Sets the window name 

		
		while not (self._running == False and self._pause == False):
			
			self.play()
			self.pause()


		pygame.quit()

	def quit(self):
		'''kills the game'''
		self._running = False
		self._pause = False

	def handle_mouse (self):
		self._mousex, self._mousey = pygame.mouse.get_pos()
		print("mouse coordinate: x = ", self._mousex, " y = ", self._mousey)
		# print(self._mousex, self._mousey)



	def handle_play_events(self):
		# function to handle movements
		keys = pygame.key.get_pressed()
		character = None
		'''
		player movements
		'''
		d = ['d1']
		if keys[pygame.K_UP]:
			self.player.y -= self.player.velocity
			
			# self._window.blit(setting, (100,100))
		if keys[pygame.K_DOWN]:
			self.player.y += self.player.velocity
			character = pygame.image.load('backgrounds/character1/' + d[0] + '.png')
		if keys[pygame.K_RIGHT]:
			self.player.x += self.player.velocity
		if keys[pygame.K_LEFT]:
			self.player.x -= self.player.velocity

		if character != None:
			self._window.blit(character, (self.player.x,self.player.y))

		'''settings. Problem: holding any key shouldn't do anything'''
		
		if keys[pygame.K_LCTRL] and keys[pygame.K_s]:
			print("Save option")
			f = open("SAVED_GAME.txt", "w+")
			### created a txt file for saved game, what what should be saved??

		if keys[pygame.K_ESCAPE]:
			# If user press esc, then bring up the setting option
			self._pause = True
			self._running = False
	

		

if __name__ == '__main__':
	Pokemon().run()
	print("in main")
    
