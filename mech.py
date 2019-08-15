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


class camera:
	def __init__(self, width, height):
		pass