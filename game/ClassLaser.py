import pygame
import time
import random
class LaserPlayer(pygame.sprite.Sprite):
	def __init__(self, x, y):
		super().__init__()
		self.image = pygame.image.load("no1/pixel_laser_yellow.png")
		self.rect = self.image.get_rect(center =(x,y))
		self.speed = -10

	def update(self,pressed_key):
		self.rect.y += self.speed
		if self.rect.bottom <= 0:
			self.kill()

class LaserEnemy(pygame.sprite.Sprite):
	def __init__(self, x, y,height):
		super().__init__()
		self.sprites = []
		self.height = height
		self.sprites.append(pygame.image.load("no1/pixel_laser_blue.png"))
		self.sprites.append(pygame.image.load("no1/pixel_laser_green.png"))
		self.sprites.append(pygame.image.load("no1/pixel_laser_red.png"))
		# self.sprites.append(pygame.image.load("nang.png"))
		self.image = self.sprites[0]
		self.image = self.sprites[random.randint(0,2)]
		self.rect = self.image.get_rect(center = (x,y))
		self.speed = 4

	def update(self,pressed_key):
		self.rect.y += self.speed
		if self.rect.top > self.height:
			self.kill()

class Explosions(pygame.sprite.Sprite):
	def __init__(self, center) :
		super().__init__()
		self.sprites = []
		self.sprites.append(pygame.image.load("no/regularExplosion00.png"))
		self.sprites.append(pygame.image.load("no/regularExplosion01.png"))
		self.sprites.append(pygame.image.load("no/regularExplosion02.png"))
		self.sprites.append(pygame.image.load("no/regularExplosion03.png"))
		self.sprites.append(pygame.image.load("no/regularExplosion04.png"))
		self.sprites.append(pygame.image.load("no/regularExplosion05.png"))
		self.sprites.append(pygame.image.load("no/regularExplosion06.png"))
		self.sprites.append(pygame.image.load("no/regularExplosion07.png"))
		self.sprites.append(pygame.image.load("no/regularExplosion08.png"))
		for i in range(9) :
			self.sprites[i] = pygame.transform.scale(self.sprites[i],(75,75))
		self.count_image = 0
		self.image = self.sprites[self.count_image]
		self.rect = self.image.get_rect(center = center)
		self.time_1 = pygame.time.get_ticks()

	def update(self,pressed_key) :
		self.time_2 = pygame.time.get_ticks()
		if self.time_2 - self.time_1 > 30:
			self.time_1 = self.time_2
			self.count_image += 1
		if self.count_image > 9 :
			self.count_image = 0
			self.kill()

