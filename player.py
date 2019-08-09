

class Player:
	def __init__(self, x_pos, y_pos):
		self.x = x_pos
		self.y = y_pos
		self.width = 40
		self.height = 50
		self.velocity = 10
		self._avatarcell = 0
		self._current_row = 0
		self._current_col = 0
		self.path = ''
		self._spriter = 0
		self._spritec = 0
		self._area = 0
		# self._track_row = 1
		self._avatar = 0
	def avatar(self, num: int)-> 'path':
		'''player needs to choose avatar, 
			numbered from 1 and return a string path'''
		self._avatar = num
		self.spritesheet()
		return self.path

	def current_row(self) -> int:
		'''
		returns the current row of the cell to be drawn. 
		Starts from 0
		'''
		return self._current_row
	def current_col(self)->int:
		'''
		returns the current col of the cell to be drawn. 
		Starts from 0
		'''
		return self._current_col

	def sprite_row(self):
		'''
		returns total row of the spritesheet, starting from 1
		'''
		return self._spriter
	def sprite_col(self):
		''' returns total col of the spritesheet, starting from 1'''
		return self._spritec
	def sprite_total_cell(self):
		''' total number of cells in the sprite sheet '''
		return self._spriter * self._spritec
	def sprite_area(self, width: int, height: int):
		'''returns the sprite cell area given a width and height'''
		pass
	def spritesheet(self):
		'''
		returns a list of avatar movements
		'''
		if self._avatar <= 2:
			# avatar with different row and col
			
			self._spriter = 1
			self._spritec = 4
			self.path = 'backgrounds/character1/bd.png' if self._avatar == 1 else 'backgrounds/character1/gd.png' 
			
		else:
			# other avatars

			self._spriter = 4
			self._spritec = 3
			self.path = 'backgrounds/avatars/' + str(self._avatar) + '.png'



	'''
	The movement of avatar, which might be needed if the player
	enters a home of some sort. For now it is not needed
	if the avatar is outside, because the background will be the one
	moving not the avatar itself.
	'''
	def movedown(self):
		
		# self._track_row = 1
		# if self.avatarcell > 2:
		# 	'''if not avatar 1, 2 then move down starts at row 1'''
		# 	# self.avatarcell = 0
		# 	self._track_row = 1
		self._current_row = 0
		self.path = 'backgrounds/character1/bd.png' if self._avatar == 1 else 'backgrounds/character1/gd.png' 
		self._current_col += 1 if self._current_col < self.sprite_col()-1 else -self.sprite_col()+1
		self.y += self.velocity
	def moveleft(self):
		
		# if self._avatar > 2:
		# 	'''if not avatar 1, 2 then move down starts at row 2'''
		# 	self._track_row = 2
		self._current_row = 0 if self._avatar <= 2 else 1
		self.path = 'backgrounds/character1/bl.png' if self._avatar == 1 else 'backgrounds/character1/gl.png' 
		self._current_col += 1 if self._current_col < self.sprite_col()-1 else -self.sprite_col()+1
		self.x -= self.velocity
	def moveright(self):
		
		# if self._avatar > 2:
		# 	'''if not avatar 1, 2 then move down starts at row 1'''
		# 	self._track_row = 3
		self._current_row = 0 if self._avatar <= 2 else 2
		self.path = 'backgrounds/character1/br.png' if self._avatar == 1 else 'backgrounds/character1/gr.png' 
		self._current_col += 1 if self._current_col < self.sprite_col()-1 else -self.sprite_col() + 1
		self.x += self.velocity
	def moveup(self):
		# self.y -= self.velocity
		self._current_row = 0 if self._avatar <= 2 else 3
		self.path = 'backgrounds/character1/bu.png' if self._avatar == 1 else 'backgrounds/character1/gu.png' 

		self._current_col += 1 if self._current_col < self.sprite_col() -1  else -self.sprite_col() +1
		self.y -= self.velocity