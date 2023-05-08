import pygame, sys, random
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
PINK = (221, 0, 255)
x_speed = 0
y_speed = 0
x = 0
y = 0
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
class Player(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect
    
#Cas
Cas = Entity(GREEN, 300,305)
Cas.x = 790
Cas.y = 190
Cas.rect.x = Cas.x
Cas.rect.y = Cas.y
Cas.image = pygame.image.load("kitty cat.png")
Cas.image = pygame.transform.scale(Cas.image,(300,305))
all_sprites.add(Cas)
All_NPC.add(Cas)
#Player
player = Player(WHITE,25,25)
player.x = 500
player.y = 500
player.rect.x = player.x
player.rect.y = player.y
all_sprites.add(player)

#Boss + Player Health GUI.
Health_image = pygame.image.load("HP_Icons.png").convert()
Health_image = pygame.transform.scale(Health_image,(300,54))
Boss_image = pygame.image.load("Boss-Bar.png").convert()
Boss_image = pygame.transform.scale(Boss_image,(900,54))
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

# --- Game logic should go here
    screen.fill(BLACK)
    screen.blit(Health_image,[200,375])
    screen.blit(Boss_image,[500,110])
    pygame.draw.rect(screen,WHITE,(200,430, 1520,520),6)
    collision = pygame.sprite.spritecollide(player, All_NPC, True)
    for cas in collision: 
        print("ouch")
    
    all_sprites.draw(screen) 
    pygame.display.flip()
    clock.tick(60)