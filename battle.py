## all the game battles state 

import pygame



## information we need to know for the battle
	## the pygame window (will attempt resizing for this, so be mindful that the width and height of the window will not be hardcoded)
	
	## Battle with random pokemon? 
		## Once we kill the pokemon, we are done

	## battle with pokemon trainers?
		## 1) trainers have multiple pokemons. 

	## before the battle begins, we need information:
		## opponent (pokemon)'s name, HP, levels, types, algorithmns of attacks
		## same info of our pokemon, except we need to know the names of the attacks and the abilities to select it using mouse and or keys
	## some animation during the battle to consider:
		## entry, entering the battle
		## HP damages
		## if it's trainer, we need to know how many pokemon they carries
		## MORE TO BE ADDED

	## at the end, we need to have HP gains, level gains



########### THIS FILE RIGHT HERE HANDLES THE RUNNING PART
########### BUT CONSIDER MAKING OTHER FILES, SUCH AS ALGORITHMN FOR ATTACKS
########### ALSO MAKE ANOTHER CLASS FOR POKEMON OPPONENT, WHERE WE CAN EASILY GET INFO
########### ABOUT THE LEVEL, HP, etc...

class battle:
	def __init__(self, window):
		pass

	def run(self):
		pass




if __name__ == '__main__':
	print("=============================debugging purposes=================================================")
	_INITIAL_BACKGROUD_WIDTH = 300
	_INITIAL_BACKGROUD_HEIGHT = 300

	pygame.init()
	pygame.display.set_caption('Pokemon')
	WINDOW = pygame.display.set_mode((_INITIAL_BACKGROUD_WIDTH, _INITIAL_BACKGROUD_HEIGHT), pygame.RESIZABLE)
	battle(WINDOW).run()

	print("=============================debugging purposes=================================================")
