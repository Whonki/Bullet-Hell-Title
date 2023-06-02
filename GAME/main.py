import pygame, player, boss, bullet

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
x_speed = 0
y_speed = 0
x = 0
y = 0
Boss_Hits = 0
pygame.init()
width = 1920
height = 1080
size = (width,height)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("My Game")

#Text 
pygame.font.init()
font = pygame.font.SysFont('PublicPixel-z84yD.ttf', 35, True, False)
Boss_text = font.render("THE WITHERHORDE, THE INTERGALACTIC CLOWN", True, WHITE )
Player_text = font.render("PLAYER: THE UNHONKED", True,WHITE)

# Loops
pause = False
done = False

clock = pygame.time.Clock()
all_sprites = pygame.sprite.Group()
bullets = pygame.sprite.Group()
arms_sprites = pygame.sprite.Group()
Boss_Health = pygame.sprite.GroupSingle(boss.HealthBar())
Player_Health = pygame.sprite.GroupSingle(player.HealthBar())

Background = pygame.mixer.Sound("Music-Tsuki no Waltz.ogg")
Background.play(-1)
injured = pygame.mixer.Sound("injured sound effect.ogg")
injured.set_volume(0.5)
death = pygame.mixer.Sound("death.ogg")
death.set_volume(0.5)

#Image rendering
Boss_image = pygame.image.load("BOSS HP.png").convert_alpha()
Boss_image = pygame.transform.scale(Boss_image,(90,90))

Player_image = pygame.image.load("PLAYER HP.png").convert_alpha()
Player_image = pygame.transform.scale(Player_image, (60,60))

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
all_sprites.add(Witherhorde)

Witherhorde_Boss = pygame.sprite.GroupSingle(Witherhorde)
#Top Arms

Arms_horizontal1 = boss.Hitbox(GREEN, 100,150)
Arms_horizontal1.rect.x = 500
Arms_horizontal1.rect.y = 400
all_sprites.add(Arms_horizontal1)
arms_sprites.add(Arms_horizontal1)

Arms_horizontal2 = boss.Hitbox(BLUE, 100,150)
Arms_horizontal2.rect.x = 1200
Arms_horizontal2.rect.y = 400
all_sprites.add(Arms_horizontal2)
arms_sprites.add(Arms_horizontal2)

#Bottom Arms

Arms_vertical1 = boss.Hitbox(BLUE, 150,100)
Arms_vertical1.rect.x = 400
Arms_vertical1.rect.y = 750
all_sprites.add(Arms_vertical1)
arms_sprites.add(Arms_vertical1)

Arms_vertical2 = boss.Hitbox(GREEN, 150,100)
Arms_vertical2.rect.x = 1370
Arms_vertical2.rect.y = 750
all_sprites.add(Arms_vertical2)
arms_sprites.add(Arms_vertical2)

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
			Bullet = bullet.Bullets(player.rect.x, player.rect.y, mouse_x, mouse_y)
			all_sprites.add(Bullet)
			bullets.add(Bullet)
			print("fire")

	if player.rect.y <= 435:
		player.rect.y = 435
	if player.rect.y >= 830:
		player.rect.y = 830
	if player.rect.x <= 420:
		player.rect.x = 420
	if player.rect.x >= 1480:
		player.rect.x = 1480

	all_sprites.update()

	for Bullet in bullets:
 
        # See if it hit a block
		block_hit_list = pygame.sprite.spritecollide(Bullet, arms_sprites, False)
		Witherhorde_Collide = pygame.sprite.spritecollide(Bullet,Witherhorde_Boss, False)
 
        # For each block hit, remove the Bullet and add to the Boss_Hits
		for block in block_hit_list:
			block_hit_list = pygame.sprite.spritecollide(Bullet, arms_sprites, False)
			bullets.remove(Bullet)
			all_sprites.remove(Bullet)
			Boss_Hits += 1
			print(Boss_Hits)
			Boss_Health.sprite.damage(30)
			injured.play()
			if Boss_Hits == 10:
				block_hit_list = pygame.sprite.spritecollide(Bullet, arms_sprites, True)
				death.play()
				Boss_Hits = 0
				Boss_Health.sprite.damage(1000)
	
		for Witherhorde in Witherhorde_Collide:
			bullets.remove(Bullet)
			all_sprites.remove(Bullet)
			Boss_Health.sprite.damage(45)

			# Remove the Bullet if it flies up off the screen
			if Bullet.rect.y < -10 or Bullet.rect.x < -10 or Bullet.rect.x > 1920 or Bullet.rect.y > 1080:
				bullets.remove(Bullet)
				all_sprites.remove(Bullet)
	
	
# --- Game logic should go her
	screen.fill(BLACK)
	pygame.draw.rect(screen,BLACK,(410,430, 1100,430))
	#Boss Health GUI.

	Boss_Health.draw(screen), Player_Health.draw(screen)
	Boss_Health.update(), Player_Health.update()
	screen.blit(Boss_image,[510,870]),screen.blit(Player_image, [200,140])
	screen.blit(Boss_text, [610,920]),screen.blit(Player_text, [250,175])

	#GUI
	pygame.draw.rect(screen,WHITE,(410,430, 1100,430),6)
	all_sprites.draw(screen) 
	pygame.display.flip()
	clock.tick(60)  