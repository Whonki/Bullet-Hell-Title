import pygame
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
# Loops
pause = False
done = False


clock = pygame.time.Clock()
All_NPC = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
bullets = pygame.sprite.Group()

class Entity(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
#Witherhorde
Witherhorde = Entity(GREEN, 300, 240)
Witherhorde.x = 790
Witherhorde.y = 190
Witherhorde.rect.x = Witherhorde.x
Witherhorde.rect.y = Witherhorde.y
"""Witherhorde.image = pygame.image.load("kitty cat.png")
Witherhorde.image = pygame.transform.scale(Witherhorde.image,(300,305))"""
all_sprites.add(Witherhorde)
All_NPC.add(Witherhorde)
class Player(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
#Player
player = Player(WHITE,25,25)
player.x = 500
player.y = 500
player.rect.x = player.x
player.rect.y = player.y
all_sprites.add(player)
class bullet(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
 
        self.image = pygame.Surface([4, 10])
        self.image.fill(WHITE)
 
        self.rect = self.image.get_rect()
    def update(self):
        self.rect.y -= 5

# -------- Main Program Loop -----------
while not done:

# --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True 
            pause = False
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                y_speed -= 4
            if event.key == pygame.K_s:
                y_speed += 4
            if event.key == pygame.K_a:
                x_speed -= 4
            if event.key == pygame.K_d:
                x_speed += 4
            if event.key == pygame.K_ESCAPE:
                quit()
            elif event.type == pygame.K_SPACE:
            # Fire a bullet if the user clicks the mouse button
                bullet = bullet()
                # Set the bullet so it is where the player is
                bullet.rect.x = player.rect.x
                bullet.rect.y = player.rect.y
                # Add the bullet to the lists
                all_sprites.add(bullet)
                bullets.add(bullet)
                print("pew")

                
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
        if player.rect.x <= 200:
            player.rect.x = 200
        if player.rect.x >= 1695:
            player.rect.x = 1695

# --- Game logic should go her
    #Boss + Player Health GUI.
    Health_image = pygame.image.load("HP_Icons.png").convert_alpha()
    Health_image = pygame.transform.scale(Health_image,(300,54))
    Boss_image = pygame.image.load("BOSS HP.png").convert_alpha()
    Boss_image = pygame.transform.scale(Boss_image,(100,840))
    Boss_image.set_colorkey(PINK)
    screen.fill(BLACK)
    pygame.draw.rect(screen,RED, (234,380, 255,43))
    screen.blit(Health_image,[200,375])
    pygame.draw.rect(screen,RED,(1640,140,70,810))
    screen.blit(Boss_image,[1630,125])
    pygame.draw.rect(screen,WHITE,(210,430, 1420,520),6)
    for Bullet in bullets:
 
        # See if it hit a block
        enemy_collision = pygame.sprite.spritecollide(bullets, Witherhorde, True)
 
        # For each block hit, remove the bullet and add to the score
        for witherhorde in enemy_collision:
            Bullet.remove(bullet)
            all_sprites.remove(bullet)
            print("hit")
 
        # Remove the bullet if it flies up off the screen
        if bullet.rect.y > -1000:
            bullet.remove(bullet)
            all_sprites.remove(bullet)
    
    all_sprites.draw(screen) 
    pygame.display.flip()
    clock.tick(60)