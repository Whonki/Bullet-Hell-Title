import pygame
class Enemy(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super().__init__()
        #Start of Hitbox
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect
        #End of Hitbox
        self.health = "" #HP (Min. 1000, max 3000.)
        self.damage = "" #Damage
        self.rest = "" #Resting period

    #def attack(self,amount):
