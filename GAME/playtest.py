import pygame

class Health(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.image = pygame.Surface((40,40))
		self.image.fill((200,30,30))
		self.rect = self.image.get_rect()
		self.health = 10000 # Can Change
		self.max_health = 10000 #Can Change
		self.health_bar_length = 690
		self.health_ratio = self.max_health / self.health_bar_length
		self.health_change_speed = 5

	def get_damage(self,amount):
		if self.health > 0:
			self.health -= amount
		if self.health < 0:
			self.health = 0
	def get_health(self,amount):
		if self.health < self.max_health:
			self.health += amount
		if self.health > self.max_health:
			self.health = self.max_health

	def update(self):
		self.basic_health()
		
	def basic_health(self):
		pygame.draw.rect(screen,(120,0,0),(219,220,85,self.health / self.health_ratio))




pygame.init()
screen = pygame.display.set_mode((1920,1080))
clock = pygame.time.Clock()
Health = pygame.sprite.GroupSingle(Health())
Boss_image = pygame.image.load("BOSS HP.png").convert_alpha()
Boss_image = pygame.transform.scale(Boss_image,(120,720))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                Health.sprite.get_health(200)
            if event.key == pygame.K_DOWN:
                Health.sprite.get_damage(200)
            if event.key == pygame.K_ESCAPE:
                quit()
    screen.fill((30,30,30))
    Health.draw(screen)
    Health.update()
    screen.blit(Boss_image,[200,200])
    pygame.display.update()
    clock.tick(60)