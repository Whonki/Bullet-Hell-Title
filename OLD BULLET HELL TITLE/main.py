import pygame,random,Health
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
PINK = (255, 0, 255)
x_speed = 0
y_speed = 0
x = 0
y = 0
score = 0
pygame.init()
width = 1920
height = 1080
size = (width,height)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("My Game")
pygame.font.init
# Loops
pause = False
done = False

clock = pygame.time.Clock()
All_NPC = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
bullets = pygame.sprite.Group()

Background = pygame.mixer.Sound("Music-Euthanasia.ogg")
Background.play(-1)

class Boss_hitbox(pygame.sprite.Sprite):
	def __init__(self, color, width, height):
		super().__init__()
		self.image = pygame.Surface([width, height])
		self.image.fill(color)
		self.rect = self.image.get_rect()
class Boss():
	def __init__(self):
		super().__init__()
		self.Max_health = 1000 #Max Health, Track
		self.Current_Health = 1000 #Current Health, Track	
#Witherhorde
Witherhorde = Boss_hitbox(GREEN, 300, 240)
Witherhorde.x = 790
Witherhorde.y = 190
Witherhorde.rect.x = Witherhorde.x
Witherhorde.rect.y = Witherhorde.y
Witherhorde.image = pygame.image.load("kitty cat.png")
Witherhorde.image = pygame.transform.scale(Witherhorde.image,(300,305))
all_sprites.add(Witherhorde)
All_NPC.add(Witherhorde)
class Player_hitbox(pygame.sprite.Sprite):
	def __init__(self, color, width, height):
		super().__init__()
		self.image = pygame.Surface([width, height])
		self.image.fill(color)
		self.rect = self.image.get_rect()
class Player():
	def __init__(self):
		super().__init__()
		self.Max_health = 1000 #Max Health, Track
		self.Current_Health = 1000 #Current Health, Track
#Player
player = Player_hitbox(WHITE,25,25)
player.x = 900
player.y = 700
player.rect.x = player.x
player.rect.y = player.y
all_sprites.add(player)

Boss_Health = pygame.sprite.GroupSingle(Boss())
Player_Health = pygame.sprite.GroupSingle(Player())
# -------- Main Program Loop -----------
while not done:

# --- Main event loop
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True 
			pygame.quit()
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_w:
				y_speed = -8
			if event.key == pygame.K_s:
				y_speed = 8
			if event.key == pygame.K_a:
				x_speed = -8
			if event.key == pygame.K_d:
				x_speed = 8
			if event.key == pygame.K_ESCAPE:
				quit()
			if event.key == pygame.K_w:
				Boss_Health.sprite.get_health(100)
				Player_Health.sprite.get_health(100)
			if event.key == pygame.K_s:
				Boss_Health.sprite.get_damage(100)
				Player_Health.sprite.get_damage(100)

		elif event.type == pygame.KEYUP:
			if event.key == pygame.K_w or event.key == pygame.K_s:
				y_speed = 0
			if event.key == pygame.K_a or event.key == pygame.K_d:
				x_speed = 0
			
		player.rect.x += x_speed
		player.rect.y += y_speed

		if player.rect.y <= 435:
			player.rect.y = 435
		if player.rect.y >= 925:
			player.rect.y = 925
		if player.rect.x <= 210:
			player.rect.x = 210
		if player.rect.x >= 1600:
			player.rect.x = 1600

# --- Game logic should go her
	#Boss + Player Health GUI.
	Health_image = pygame.image.load("HP_Icons.png").convert_alpha()
	Health_image = pygame.transform.scale(Health_image,(300,54))
	Boss_image = pygame.image.load("BOSS HP.png").convert_alpha()
	Boss_image = pygame.transform.scale(Boss_image,(100,840))
	Boss_image.set_colorkey(PINK)
	#Not Health
	screen.fill(BLACK)
	#Actual Health
	screen.blit(Health_image,[200,375])
	screen.blit(Boss_image,[1630,125])
	pygame.draw.rect(screen,WHITE,(210,430, 1420,520),6)
	all_sprites.draw(screen) 
	pygame.display.flip()
	clock.tick(60)