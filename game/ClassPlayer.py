import pygame
from pygame.locals import *


class Player1(pygame.sprite.Sprite):
	def __init__(self,width,height):
		super().__init__() 
		self.width = width
		self.height = height
		self.image = pygame.image.load("pixel_ship_yellow.png")
		self.image = pygame.transform.scale(self.image,(80,80))
		self.rect = self.image.get_rect(center = (400, 400))
	def update(self,pressed_key): # cài dặt các phím 
		if pressed_key[K_UP]:
			self.rect.move_ip(0,-5)
		if pressed_key[K_DOWN]:
			self.rect.move_ip( 0,5)
		if pressed_key[K_LEFT]:
			self.rect.move_ip(-5,0)
		if pressed_key[K_RIGHT]:
			self.rect.move_ip(5,0)
	#cai dat người chơi chỉ ở trong khung hinh
		if self.rect.top <  0:
			self.rect.top = 0	
		if self.rect.bottom > self.height:
			self.rect.bottom = self.height	
		if self.rect.left < 0:
			self.rect.left = 0	
		if self.rect.right > self.width:
			self.rect.right = self.width	

	def show(self) :
		return (self.rect.centerx, self.rect.top)



class Player2(pygame.sprite.Sprite):
	def __init__(self,height,width):
		super().__init__()
		self.height = height
		self.width = width		
		self.image = pygame.image.load("pixel_ship_yellow.png")
		self.image = pygame.transform.scale(self.image,(80,80))
		self.rect = self.image.get_rect(
			center = (400,400)
		) #gọi nó ra ở góc trái trên cùng màn hình
	def update(self,pressed_key): # cài dặt các phím 
		if pressed_key[K_w]:
			self.rect.move_ip(0,-5)
		if pressed_key[K_s]:
			self.rect.move_ip( 0,5)
		if pressed_key[K_a]:
			self.rect.move_ip(-5,0)
		if pressed_key[K_d]:
			self.rect.move_ip(5,0)
	#cai dat người chơi chỉ ở trong khung hinh
		if self.rect.top <  0:
			self.rect.top = 0	
		if self.rect.bottom > self.height:
			self.rect.bottom = self.height	
		if self.rect.left < 0:
			self.rect.left = 0	
		if self.rect.right > self.width:
			self.rect.right = self.width
	def show(self) :
		return (self.rect.centerx, self.rect.top)	