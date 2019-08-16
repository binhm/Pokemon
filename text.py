import pygame

class Text:
    def __init__(self, font, font_size, text, text_color, surface, x_pos, y_pos):
        self.font = font
        self.size = font_size
        self.text = text
        self.text_color = text_color
        self.surface = surface
        self.x_pos = x_pos
        self.y_pos = y_pos
    
    def create(self):
        t = pygame.font.SysFont(self.font, self.size, bold=True)
        text_surface = t.render(self.text, True, self.text_color)
        text_rect = text_surface.get_rect(center = (self.x_pos, self.y_pos))
        self.surface.blit(text_surface, text_rect)
        