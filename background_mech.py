'''
Code for 
'''

import pytmx
#pixel
import pygame
import player
TILE_HEIGHT = 16
TILE_WIDTH = 16

testing_background = [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
					  [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,'w','w','w','w','w','w','w','w','w','w']]

background = 'practice.tmx'

## CAN'T GO THROUGH
## - bush
## - trees
## - houses
## - walls

## JUMPS DOWN
## - cliff?

## SWIM
## BODY OF WATER

class Map:
	def __init__(self):
		self.background = testing_background

	def data(self):
		return self.background

class Tiledmap:
	def __init__(self, filename: str):
		# to get the transparency, set pixelalpha to true in the 
		# second argument of load_pygame, not needed in this case since there's no 
		# transparency in our case
		self.tmxdata = pytmx.load_pygame(filename)

		# find the entire map's dimension by titlewidth * num of tiles across and below
		self.width = self.tmxdata.width * self.tmxdata.tilewidth #the width of the image
		self.height = self.tmxdata.height * self.tmxdata.tileheight
	
	def draw_map(self, surface: pygame.Surface):
		'''Iterate the .xml file and blit all the tiles on screen '''

		ti = self.tmxdata.get_tile_image_by_gid
		for layer in self.tmxdata.visible_layers:
			if isinstance(layer, pytmx.TiledTileLayer):
				for x,y,gid, in layer:
					tile = ti(gid)
					# print(gid)
					if tile:

						# print("x = {}, y={}".format(x,y))
						surface.blit(tile,( x * self.tmxdata.tilewidth, y * self.tmxdata.tilewidth))
			elif isinstance(layer, pytmx.TiledObjectGroup):
				# print(" OBJECT GROUP IS NOT HANDLED")
				pass

	def make_map(self)-> pygame.Surface:
		'''make a temporary surface with the .tmx 
		map drawn and return that surface. This is so we can 
		blit portion of the .tmx map for moving background'''
		temp_surface = pygame.Surface((self.width, self.height))
		self.draw_map(temp_surface)
		return temp_surface

	# def camera(self, player: player.Player, surface: pygame.Surface):
	
class camera:
	def __init__(self, width, height, surface:pygame.Surface):
		self.camera = pygame.Rect (0,0, surface.get_width(), surface.get_height())
		self.width = width
		self.height = height
		self.surface = surface
		## self.height & self.width is the surface size of the tilemap
		## we want to find the right pixels to blit
	# def apply(self, entity):
		
	# 	return entity.rect.move(self.camera.topleft)

	def apply_rect(self, rect)->pygame.Rect:
		return rect.move(self.camera.topleft)


	def update(self, target:player.Player):
		'''changes the coordinate of screen itself 
		so that it create moving background.  '''

		### so many problems with this one.....
		### target pixel goes off screen
		
		WIDTH, HEIGHT = self.surface.get_size()
		x = -target.x  + WIDTH/2
		y = -target.y  + HEIGHT/2
		# limit scrolling to map size
		# print("mech.py: avatar coord x = {}, y = {}".format(-target.x, -target.y))
		
		x = min(0, x)  # left
		y = min(0, y)  # top
		# print("mech.py: avatar coord after min x = {}, y = {}".format(x, y))
		x = max(-(self.width - WIDTH), x)  # right
		y = max(-(self.height - HEIGHT), y)  # bottom

		# print("mech.py: map offset x = {}, y = {}".format(x,y))
		self.camera = pygame.Rect(x, y, self.width, self.height)