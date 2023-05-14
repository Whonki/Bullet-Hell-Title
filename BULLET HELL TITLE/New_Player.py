import pygame
class Player(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super().__init__()
        self.image = pygame.Surface([width, height]) #HITBOX
        self.image.fill(color) #HITBOX
        self.rect = self.image.get_rect #HITBOX
        self.health = 100
    def attack(self):
        self.damage = 75 #Attack DMG
        self.cooldown = 3 #seconds
        



