import pygame
"""

+================================================================+
+																 +
+	EVERYTHING INVOLVING THE PLAYER CLASS IS INCLUDED HERE.		 +
+																 +
+																 +
+================================================================+

"""
width = 1920
height = 1080
size = (width,height)
screen = pygame.display.set_mode(size)
class Hitbox(pygame.sprite.Sprite):
	def __init__(self, color, width, height):
		super().__init__()
		self.image = pygame.Surface([width, height])
		self.image.fill(color)
		self.rect = self.image.get_rect()

class Health(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.current_Health = 10
	