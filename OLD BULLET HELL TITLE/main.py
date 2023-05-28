import pygame, player, boss, bullet
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
Arms = 4
pygame.init()
width = 1920
height = 1080
size = (width,height)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("My Game")
# Loops
pause = False
done = False

clock = pygame.time.Clock()
all_sprites = pygame.sprite.Group()
bullets = pygame.sprite.Group()
arms_sprites = pygame.sprite.Group()

Background = pygame.mixer.Sound("Music-Tsuki no Waltz.ogg")
Background.play(-1)

#Bosses
Witherhorde = boss.Hitbox(GREEN, 300, 240)
Witherhorde.x = 790
Witherhorde.y = 190
Witherhorde.rect.x = Witherhorde.x
Witherhorde.rect.y = Witherhorde.y
Witherhorde.image = pygame.image.load("kitty cat.png")
Witherhorde.image = pygame.transform.scale(Witherhorde.image,(300,305))
all_sprites.add(Witherhorde)

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

Arms_vertical1 = boss.Hitbox(BLUE, 150,100)
Arms_vertical1.rect.x = 400
Arms_vertical1.rect.y = 800
all_sprites.add(Arms_vertical1)
arms_sprites.add(Arms_vertical1)

Arms_vertical2 = boss.Hitbox(GREEN, 150,100)
Arms_vertical2.rect.x = 1500
Arms_vertical2.rect.y = 800
all_sprites.add(Arms_vertical2)
arms_sprites.add(Arms_vertical2)

player = player.Hitbox(WHITE,25,25)
player.x = 900
player.y = 700
player.rect.x = player.x 
player.rect.y = player.y
all_sprites.add(player)

# -------- Main Program Loop -----------
while not done:

# --- Main event loop
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True 
			pygame.quit()
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_w:
				y_speed = -4
			if event.key == pygame.K_s:
				y_speed = 4
			if event.key == pygame.K_a:
				x_speed = -4
			if event.key == pygame.K_d:
				x_speed = 4
			#Shooting
			if event.key == pygame.K_ESCAPE:
				quit()
			if event.key == pygame.K_UP:
				Health.sprite.get_health()
				Boss_Health.sprite.get_health(200)
			if event.key == pygame.K_DOWN:
				Health.sprite.get_damage()
				Boss_Health.sprite.get_damage(200)
		if event.type == pygame.MOUSEBUTTONDOWN:
			pos = pygame.mouse.get_pos() 
			mouse_x = pos[0]
			mouse_y = pos[1]
			Bullet = bullet.Bullets(player.rect.x, player.rect.y, mouse_x, mouse_y)
			all_sprites.add(Bullet)
			bullets.add(Bullet)
			print("fire")
		if event.type == pygame.KEYUP:
			if event.key == pygame.K_w or event.key == pygame.K_s:
				y_speed = 0
			if event.key == pygame.K_a or event.key == pygame.K_d:
				x_speed = 0
			
		player.rect.x += x_speed
		player.rect.y += y_speed

		if player.rect.y <= 435:
			player.rect.y = 435
		if player.rect.y >= 923:
			player.rect.y = 923
		if player.rect.x <= 410:
			player.rect.x = 410
		if player.rect.x >= 1600:
			player.rect.x = 1600

	all_sprites.update()

	for Bullet in bullets:
 
        # See if it hit a block
		block_hit_list = pygame.sprite.spritecollide(Bullet, arms_sprites, False)
 
        # For each block hit, remove the Bullet and add to the Boss_Hits
		for block in block_hit_list:
			block_hit_list = pygame.sprite.spritecollide(Bullet, arms_sprites, False)
			bullets.remove(Bullet)
			all_sprites.remove(Bullet)
			Boss_Hits += 1
			print(Boss_Hits)
			if Boss_Hits == 20:
				block_hit_list = pygame.sprite.spritecollide(Bullet, arms_sprites, True)
				Boss_Hits = 0
 
        # Remove the Bullet if it flies up off the screen
			if Bullet.rect.y < -10 or Bullet.rect.x < -10 or Bullet.rect.x > 1920 or Bullet.rect.y > 1080:
				bullets.remove(Bullet)
				all_sprites.remove(Bullet)

# --- Game logic should go her
	screen.fill(BLACK)
	#Boss + Player Health GUI.
	#Actual Health
	pygame.draw.rect(screen,WHITE,(410,430, 1220,520),6)
	all_sprites.draw(screen) 
	pygame.display.flip()
	clock.tick(60)  