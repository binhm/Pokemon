

class Player:
	def __init__(self, x_pos, y_pos):
		self.x = x_pos
		self.y = y_pos
		self.width = 40
		self.height = 50
		self.velocity = 10
		self._avatarcell = 0
		self._cell = 3 ## hard coded to 3 right now
	def avatarcell(self):
		'''
		Returns the cell of avatar movement and which one should be 
		drawn on screen.
		'''
		### Not accounting for pictures with multilples rows.
		return self._avatarcell





	'''
	The movement of avatar, which might be needed if the player
	enters a home of some sort. For now it is not needed
	if the avatar is outside, because the background will be the one
	moving not the avatar itself.
	'''
	def moveup(self):
		self.y -= self.velocity
		self._avatarcell += 1 if self._avatarcell < self._cell else -self._cell
	def movedown(self):
		self.y += self.velocity
		self._avatarcell += 1 if self._avatarcell < self._cell else -self._cell
	def moveright(self):
		self.x += self.velocity
		self._avatarcell += 1 if self._avatarcell < self._cell else -self._cell
	def moveleft(self):
		self.x -= self.velocity
		self._avatarcell += 1 if self._avatarcell < self._cell else -self._cell