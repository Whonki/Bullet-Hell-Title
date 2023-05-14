import pygame, New_Player
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


Player = New_Player.Player(WHITE,25,25)
Player.x = 500
Player.y = 1000
Player.rect.x = Player.x
Player.rect.y = Player.y
all_sprites.add(Player)

#Boss + Player Health GUI.
Health_image = pygame.image.load("HP_Icons.png").convert_alpha()
Health_image = pygame.transform.scale(Health_image,(300,54))
Boss_image = pygame.image.load("Boss-Bar.png").convert_alpha()
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
            if event.key == pygame.K_ESCAPE:
                quit()

# --- Game logic should go here
    screen.fill(BLACK)
    all_sprites.draw(screen) 
    pygame.draw.rect(screen,RED, (234,380, 255,43))
    screen.blit(Health_image,[200,375])
    pygame.draw.rect(screen,RED,(520,117,870,40))
    screen.blit(Boss_image,[500,110])
    pygame.draw.rect(screen,WHITE,(200,430, 1520,520),6)
    pygame.display.flip()
    
    clock.tick(60)