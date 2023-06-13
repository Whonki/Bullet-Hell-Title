import pygame, random, math

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
WHITE = (255, 255, 255)
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
		pygame.draw.rect(screen,RED,(570,890,self.health / self.health_ratio,30))
		pygame.draw.rect(screen,WHITE,(570,890,self.health_bar_length,30),4)
	
rain_list = []
stars_list = []
moon_list = []
class Rain(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.damage = 15
		self.velocity = 65
		self.image = pygame.Surface([10, 10])
		self.image.fill(WHITE)
		self.rect = self.image.get_rect()
		for self.i in range(125):
			self.x = random.randrange(0,width)
			self.y = 0
			rain_list.append([self.x,self.y])
	def draw(self):
		for self.i in range(len(rain_list)):
			pygame.draw.circle(screen, WHITE, rain_list[self.i], 10)
	
	

class Stars(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.damage = 35
		self.velocity = 65
		self.image = pygame.Surface([50, 50])
		self.image.fill(WHITE)
		self.rect = self.image.get_rect()
		for self.i in range(75):
			self.x = width
			self.y = random.randrange(0, height)
			rain_list.append([self.x,self.y])
	def draw(self):
		for self.i in range(len(rain_list)):
			pygame.draw.circle(screen, WHITE, rain_list[self.i], 10)

class Moon(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.damage = 150
		self.velocity = 30
		self.image = pygame.Surface([100, 100])
		self.image.fill(WHITE)
		self.rect = self.image.get_rect()
		for self.i in range(10):
			self.x = random.randrange(1000,width)
			self.y = height
			rain_list.append([self.x,self.y])
	def draw(self):
		for self.i in range(len(rain_list)):
			pygame.draw.circle(screen, WHITE, rain_list[self.i], 10)
