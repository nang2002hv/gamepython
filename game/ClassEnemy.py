import pygame
import random

class Enemy(pygame.sprite.Sprite) :
	def __init__(self,height,width) :
		super().__init__()
		self.sprites = []  #nhom phi thuyen quan 
		#self.surf.fill((0,0,0))
		self.height = height
		self.width = width
		self.sprites.append(pygame.image.load("pixel_ship_red_small.png"))
		self.sprites.append(pygame.image.load("pixel_ship_blue_small.png"))
		self.sprites.append(pygame.image.load("pixel_ship_green_small.png"))
		self.image = self.sprites[random.randint(0,2)]
		self.rect = self.image.get_rect(
			center =((random.randint(20,width-100)),(random.randint(0,10)))
		)
		self.speed = 3# tốc độ của địch đi ra
	def update(self,pressed_key) :
		self.rect.move_ip(0,self.speed)
		if self.rect.bottom > self.height :
			self.kill()
			self.rect = self.image.get_rect(
				center =((random.randint(20,self.width-100)),(random.randint(0,10)))
			)
	def show(self):
		return (self.rect.centerx, self.rect.bottom)
