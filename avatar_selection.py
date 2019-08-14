import pygame

class AvatarSelection:
	def __init__(self, image, rows, columns, row_d, col_d, x_pos, y_pos, window):
		self.image_path = image
		self.rows = rows
		self.cols = columns
		self.row_d = row_d
		self.col_d = col_d
		self.x_pos = x_pos
		self.y_pos = y_pos
		self.window = window

	def create_avatar_selection(self):
		avatar = pygame.image.load(self.image_path).convert_alpha()
		img_width, img_height = avatar.get_width() / self.cols, avatar.get_height() / self.rows
		self.window.blit(avatar, (self.x_pos, self.y_pos),
			(self.col_d * img_width, self.row_d * img_height, img_width, img_height))


