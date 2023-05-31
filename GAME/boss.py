import pygame

"""

+================================================================+
+																 +
+	EVERYTHING INVOLVING THE BOSS CLASS IS INCLUDED HERE.		 +
+																 +
+																 +
+================================================================+

"""
width = 1920
height = 1080
RED = (255, 0, 0)
size = (width,height)
screen = pygame.display.set_mode(size)

class Hitbox(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()

class HealthBar(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.image = pygame.Surface((40,40))
		self.rect = self.image.get_rect()
		self.health = 10000 # Can Change
		self.max_health = 10000 #Can Change
		self.health_bar_length = 690
		self.health_ratio = self.max_health / self.health_bar_length
		self.health_change_speed = 5

	def damage(self,amount):
		if self.health > 0:
			self.health -= amount
		if self.health < 0:
			self.health = 0

	def update(self):
		self.basic_health()
		
	def basic_health(self):
		pygame.draw.rect(screen,RED,(219,220,85,self.health / self.health_ratio))
