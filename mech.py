'''
Handles the mechanics of the game
Handles how the avatar interacts with
the World
'''

import pytmx
#pixel
TILE_HEIGHT = 16
TILE_WIDTH = 16

testing_background = [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
					  [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,'w','w','w','w','w','w','w','w','w','w']]

background = 'backgrounds/practice.tmx'

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
		# second argument of load_pygame
		self.tmxdata = pytmx.load_pygame(filename)

		#tm.width is num of tiles across
		self.width = tm.width * tm.tilewidth #the width of the image
		self.height = tm.height * tm.tileheight
	def draw(self, surface ):
		tile_image = self.tmxdata.get_tile_image_by_gid
		for layer in self.tmxdata.visible_layers:
			## if the layer is a tiled layer
			## get the x,y, grid in the layer
			if isinstance(layer, pytmx.TiledTileLayer):
				for x,y, gid, in layer:
					tile = tile_image(gid)
					if tile:
						pass
class camera:
	def __init__(self, width, height):
		pass