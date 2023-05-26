import pygame
class Hitbox(pygame.sprite.Sprite):
	def __init__(self, color, width, height):
		super().__init__()
		self.image = pygame.Surface([width, height])
		self.image.fill(color)
		self.rect = self.image.get_rect()

class Health(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
    def Health(self):
        self.Health = 10000

