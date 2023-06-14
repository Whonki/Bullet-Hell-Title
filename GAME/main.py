import pygame, player, boss, bullet, random

"""

+================================================================+
+																 +
+			THIS IS THE MAIN PROGRAM FOR THE GAME.               +
+						PRESS RUN HERE.		                     +
+																 +
+																 +
+================================================================+

"""
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
PINK = (255, 0, 255)
PURPLE = (82,28,129)
x_speed = 0
y_speed = 0
x = 0
y = 0
pygame.init()
width = 1920
height = 1080
Boss_Hits = 0
size = (width,height)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("My Game")

#Text 
pygame.font.init()
font = pygame.font.SysFont('PublicPixel-z84yD.ttf', 35, False, True)
game_over_Screen = pygame.font.SysFont('PublicPixel-z84yD.ttf', 100, False, True)

Boss_text = font.render("THE TUMORS OF THE ABYSS", False, WHITE )
Player_text = font.render("THE PLAYER", False, WHITE)
game_over = game_over_Screen.render("HA YOU DIED! :o)", False, RED)
win = game_over_Screen.render("YOU WON. ...I GUESS. >:o(", False, GREEN)
poison = font.render("POISONED!", False, PURPLE)

# Loops
pause = False
done = False

clock = pygame.time.Clock()
all_sprites = pygame.sprite.Group()
arms_sprites = pygame.sprite.Group()
Boss_Health = pygame.sprite.GroupSingle(boss.HealthBar())
Player_Health = pygame.sprite.GroupSingle(player.HealthBar())

rain_list = []
stars_list = []
moon_list = []

# Projectiles
player_attacks = pygame.sprite.Group() #Player
boss_attacks = pygame.sprite.Group() #Boss


Background = pygame.mixer.Sound("sounds/Music-Tsuki no Waltz.ogg")
Background.play(-1)
injured = pygame.mixer.Sound("sounds/injured sound effect.ogg")
injured.set_volume(0.5)
death = pygame.mixer.Sound("sounds/death.ogg")
death.set_volume(0.5)

#Image rendering
	# Health
Boss_image = pygame.image.load("imgs/BOSS HP.png").convert_alpha()
Boss_image = pygame.transform.scale(Boss_image,(90,90))

Player_image = pygame.image.load("imgs/PLAYER HP.png").convert_alpha()
Player_image = pygame.transform.scale(Player_image, (60,60))

# Player

player = player.Movement(50, 50)
player.x = 900
player.y = 700
player.rect.x = player.x 
player.rect.y = player.y
all_sprites.add(player)

player_collision = pygame.sprite.GroupSingle(player)

#Bosses
Witherhorde = boss.Hitbox(GREEN, 300, 240)
Witherhorde.x = 790
Witherhorde.y = 190
Witherhorde.rect.x = Witherhorde.x
Witherhorde.rect.y = Witherhorde.y
Witherhorde.image = pygame.image.load("imgs/Main tumor.png").convert_alpha()
Witherhorde.image = pygame.transform.scale(Witherhorde.image, (300,240))
all_sprites.add(Witherhorde)


Witherhorde_Boss = pygame.sprite.GroupSingle(Witherhorde)


Tumor_1 = boss.Hitbox(GREEN, 210,140)
Tumor_1.rect.x = 500
Tumor_1.rect.y = 315
Tumor_1.image = pygame.image.load("imgs/Tumor 3.png").convert_alpha()
Tumor_1.image = pygame.transform.scale(Tumor_1.image, (210,140))
all_sprites.add(Tumor_1)
arms_sprites.add(Tumor_1)

Tumor_2 = boss.Hitbox(BLUE, 300,200)
Tumor_2.rect.x = 1200
Tumor_2.rect.y = 260
Tumor_2.image = pygame.image.load("imgs/side tumor.png").convert_alpha()
Tumor_2.image = pygame.transform.scale(Tumor_2.image, (300,200))
all_sprites.add(Tumor_2)
arms_sprites.add(Tumor_2)

Tumor_3 = boss.Hitbox(BLUE, 200,300)
Tumor_3.rect.x = 230
Tumor_3.rect.y = 700
Tumor_3.image = pygame.image.load("imgs/left_Tumor.png").convert_alpha()
Tumor_3.image = pygame.transform.scale(Tumor_3.image, (200,300))
all_sprites.add(Tumor_3)
arms_sprites.add(Tumor_3)

Tumor_4 = boss.Hitbox(GREEN, 200,300)
Tumor_4.rect.x = 1480
Tumor_4.rect.y = 700
Tumor_4.image = pygame.image.load("imgs/right_Tumor.png").convert_alpha()
Tumor_4.image = pygame.transform.scale(Tumor_4.image, (200,300))
all_sprites.add(Tumor_4)
arms_sprites.add(Tumor_4)

# -------- Main Program Loop -----------
while not done:
# --- Main event loop
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True 
			pygame.quit()
			
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_a:
				player.changespeed(-3, 0)
			elif event.key == pygame.K_d:
				player.changespeed(3, 0)
			elif event.key == pygame.K_w:
				player.changespeed(0, -3)
			elif event.key == pygame.K_s:
				player.changespeed(0, 3)
			if event.key == pygame.K_ESCAPE:
				quit()
 
        # Reset speed when key goes up
		if event.type == pygame.KEYUP:
			if event.key == pygame.K_a:
				player.changespeed(3, 0)
			elif event.key == pygame.K_d:
				player.changespeed(-3, 0)
			elif event.key == pygame.K_w:
				player.changespeed(0, 3)
			elif event.key == pygame.K_s:
				player.changespeed(0, -3)
		#Shooting
		if event.type == pygame.MOUSEBUTTONDOWN:
			pos = pygame.mouse.get_pos() 
			mouse_x = pos[0]
			mouse_y = pos[1]
			Bullet = bullet.Fire(player.rect.x, player.rect.y, mouse_x, mouse_y)
			Bullet.image = pygame.image.load("imgs/Bullet.png").convert_alpha()
			Bullet.image = pygame.transform.scale(Bullet.image, (30,30))
			all_sprites.add(Bullet)
			player_attacks.add(Bullet)


	if player.rect.y < 435:
		player.rect.y = 434
	if player.rect.y > 830:
		player.rect.y = 831
	if player.rect.x < 420:
		player.rect.x = 419
	if player.rect.x > 1480:
		player.rect.x = 1481
#Rain's cooldown
	boss_cooldowns = random.randrange(0, 600)
	print(boss_cooldowns)

	#Rain
	if boss_cooldowns <= 0 and boss_cooldowns >= 150:
		velocity = 5
		for i in range(15):
			x = random.randrange(0, 1900)
			y = random.randrange(0,10)
			rain_list.append[x,y]
	for i in range(len(stars_list)):
		image = pygame.draw.circle(screen, WHITE, rain_list[i], 15)
		rain_list[i][1] += 1*velocity

#Boss Attack Collisions
	for Rain in boss_attacks:
		Player_Collide = pygame.sprite.spritecollide(rain_list,player,False)
		Player_Health.sprite.damage(75)

#Player Attack Collisions
	
	for Bullet in player_attacks:
 
		Tumor_Collision = pygame.sprite.spritecollide(Bullet, arms_sprites, False)
		Witherhorde_Collide = pygame.sprite.spritecollide(Bullet,Witherhorde_Boss, False)

		for arm_sprites in Tumor_Collision:
			player_attacks.remove(Bullet)
			all_sprites.remove(Bullet)
			Boss_Hits += 1
			print(Boss_Hits)
			injured.play()
			if Boss_Hits == 15:
				Tumor_Collision = pygame.sprite.spritecollide(Bullet, arms_sprites, True)
				death.play()
				Boss_Hits = 0
				Boss_Health.sprite.damage(1000)
				Player_Health.sprite.healing(170)
	
		for Witherhorde in Witherhorde_Collide:
			player_attacks.remove(Bullet)
			all_sprites.remove(Bullet)
			Boss_Health.sprite.damage(150)
			injured.play()

		# Remove the Bullet if it flies up off the screen
		if Bullet.rect.x < 10 or Bullet.rect.x > width-10 or Bullet.rect.y < 10 or Bullet.rect.y > height-10:
			Boss_Health.sprite.healing(125)
			Bullet.kill()
			print(len(player_attacks))
	if player.x  > 410 or player.y > 430 or player.x < 1100 or player.y < 430:
		Player_Health.sprite.damage(0.6)
			
# --- Game logic should go here
	#Boss Health GUI.
	screen.fill(BLACK)
	pygame.draw.rect(screen,BLACK,(410,430, 1100,430))
	Boss_Health.draw(screen), Player_Health.draw(screen)
	Boss_Health.update(), Player_Health.update()
	screen.blit(Boss_image,[510,870]),screen.blit(Player_image, [200,140])
	screen.blit(Boss_text, [610,920]),screen.blit(Player_text, [250,175])
	screen.blit(poison,[450,175])
	#GUI
	pygame.draw.rect(screen,WHITE,(410,430, 1100,430),6)
	all_sprites.draw(screen) 
	all_sprites.update()

	if Boss_Health.sprite.health <= 0:
		Witherhorde_Collide = pygame.sprite.spritecollide(Bullet,Witherhorde_Boss, True)
		screen.fill(BLACK)
		Background.set_volume(0)
		screen.blit(win, [610,540])
		arms_sprites.remove(Tumor_1,Tumor_2,Tumor_3,Tumor_4)
		all_sprites.remove(Tumor_1,Tumor_2,Tumor_3,Tumor_4)

	if Player_Health.sprite.health <= 0:
		screen.fill(BLACK)
		screen.blit(game_over, [610,540])
		Background.set_volume(0)
		all_sprites.remove(player)

	pygame.display.flip()
	clock.tick(60)