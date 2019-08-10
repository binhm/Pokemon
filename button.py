import pygame

class Button:
	def __init__(self, surface, button_info, button_color, text, text_size, font, text_color):
		self.surface = surface
		self.button_info = button_info
		self.x_pos = button_info[0]
		self.y_pos = button_info[1]
		self.w = button_info[2]
		self.h = button_info[3]
		self.button_color = button_color
		self.text = text
		self.text_size = int(text_size)
		self.font = font
		self.color = text_color
		self.text_color = text_color

	def create(self):
		button = pygame.draw.rect(self.surface, self.button_color, self.button_info)
		button_text = pygame.font.SysFont(self.font, self.text_size, bold=True)
		bt_surface = button_text.render(self.text, True, self.text_color)
		bt_rect = bt_surface.get_rect(center = (self.x_pos + self.w / 2, self.y_pos + self.h / 2))
		self.surface.blit(bt_surface, bt_rect)
