import pygame,random
pygame.init()
screen = pygame.display.set_mode((1920, 1080))
WHITE = 0,0,0
clock = pygame.time.Clock()
moon_list = []
class Moon(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.damage = 150
		self.velocity = 30
		self.image = pygame.Surface([100, 100])
		self.image.fill(WHITE)
		self.rect = self.image.get_rect()
		for self.i in range(10):
			self.x = random.randrange(1000,1920)
			self.y = 1080
			moon_list.append([self.x,self.y])
	def draw(self):
		for self.i in range(len(moon_list)):
			pygame.draw.circle(screen, WHITE, moon_list[self.i], 10)
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True 
            pygame.quit()

   
    pygame.display.flip()
    clock.tick(60)