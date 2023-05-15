import pygame, sys
#Using to understand and use
class Player(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.image = pygame.Surface((40,40))
		self.image.fill((200,30,30))
		self.rect = self.image.get_rect(center = (400,400))
		self.current_health = 200
		self.target_health = 500
		self.max_health = 1000
		self.health_bar_length = 400
		self.health_ratio = self.max_health / self.health_bar_length

	def get_damage(self,amount):
		if self.target_health > 0:
			self.target_health -= amount
		if self.target_health < 0:
			self.target_health = 0

	def get_health(self,amount):
		if self.target_health < self.max_health:
			self.target_health += amount
		if self.target_health > self.max_health:
			self.target_health = self.max_health

	def update(self):
		self.basic_health()
		
	def basic_health(self):
		pygame.draw.rect(screen,(255,0,0),(10,10,self.target_health / self.health_ratio,25))
		pygame.draw.rect(screen,(255,255,255),(10,10,self.health_bar_length,25),4)

pygame.init()
screen = pygame.display.set_mode((800,800))
clock = pygame.time.Clock()
player = pygame.sprite.GroupSingle(Player())

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
			pygame.quit()
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_UP:
				player.sprite.get_health(20)
			if event.key == pygame.K_DOWN:
				player.sprite.get_damage(20)

	screen.fill((30,30,30))
	player.draw(screen)
	player.update()
	pygame.display.update()
	clock.tick(60)