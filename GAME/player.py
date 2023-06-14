import pygame
"""

+================================================================+
+																 +
+	EVERYTHING INVOLVING THE PLAYER CLASS IS INCLUDED HERE.		 +
+																 +
+																 +
+================================================================+

"""
width = 1920
height = 1080
RED = (255, 0, 0)
WHITE = (255, 255, 255)
PURPLE = (82,28,129)
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
		self.health = 1000 # Can Change
		self.max_health = 1000 #Can Change
		self.health_bar_length = 690
		self.health_ratio = self.max_health / self.health_bar_length
		self.health_change_speed = 5

	def damage(self,amount):
		if self.health > 0:
			self.health -= amount
		if self.health < 0:
			self.health = 0

	def healing(self,amount):
		if self.health > 0 and self.health < self.max_health:
			self.health += amount
			if self.health >= self.max_health:
				self.health = self.max_health
		if self.health < 0:
			self.health = 0

	def update(self):
		self.basic_health()
		
	def basic_health(self):
		pygame.draw.rect(screen,PURPLE,(250,150,self.health / self.health_ratio,25))
		pygame.draw.rect(screen,WHITE,(250,150,self.health_bar_length,25),4)

class Movement(pygame.sprite.Sprite):
	""" The class is the player-controlled sprite. """

	# -- Methods
	def __init__(self, x, y):
		"""Constructor function"""
		# Call the parent's constructor
		super().__init__()

		# Set height, width
		self.image = pygame.Surface([25, 25])
		self.image.fill(WHITE)

		# Make our top-left corner the passed-in location.
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y

		# -- Attributes
		# Set speed vector
		self.change_x = 0
		self.change_y = 0

	def changespeed(self, x, y):
		""" Change the speed of the player"""
		self.change_x += x
		self.change_y += y

	def update(self):
		""" Find a new position for the player"""
		self.rect.x += self.change_x
		self.rect.y += self.change_y