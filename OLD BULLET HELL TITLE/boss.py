import pygame
width = 1920
height = 1080
size = (width,height)
screen = pygame.display.set_mode(size)

class Hitbox(pygame.sprite.Sprite):
	def __init__(self, color, width, height):
		super().__init__()
		self.image = pygame.Surface([width, height])
		self.image.fill(color)
		self.rect = self.image.get_rect()

class Health(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.health = 1000
    def get_damage(self,amount):
        if self.target_health > 0:
            self.target_health -= amount
        if self.target_health < 0:
            self.target_health = 0