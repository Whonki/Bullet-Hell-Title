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
        self.no_health = 0
        self.current_Health = 1000
        self.max_health = 1000
