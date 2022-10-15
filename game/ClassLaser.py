import pygame
import random
class LaserPlayer(pygame.sprite.Sprite):
	def __init__(self, x, y):
		super().__init__()
		self.image = pygame.image.load("pixel_laser_yellow.png")
		self.rect = self.image.get_rect()
		self.rect.bottom = y
		self.rect.centerx = x
		self.speed = -10

	def update(self,pressed_key):
		self.rect.y += self.speed
		if self.rect.bottom < 0:
			self.kill()

class LaserEnemy(pygame.sprite.Sprite):
	def __init__(self, x, y):
		super().__init__()
		self.sprites = []
		self.sprites.append(pygame.image.load("pixel_laser_blue.png"))
		self.sprites.append(pygame.image.load("pixel_laser_green.png"))
		self.sprites.append(pygame.image.load("pixel_laser_red.png"))
		self.image = self.sprites[random.randint(0,2)]
		self.rect = self.image.get_rect()
		self.rect.bottom = y
		self.rect.centerx = x
		self.speed = 5

	def update(self,pressed_key):
		self.rect.y += self.speed
		if self.rect.top > 800:
			self.kill()