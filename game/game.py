import random
import time
from turtle import speed
import pygame
from pygame.locals import (
	K_UP, K_DOWN, K_LEFT,K_RIGHT, K_ESCAPE,QUIT,KEYDOWN
)
clock = pygame.time.Clock() # cài đặt khung hình trên giây
pygame.init()
width = 1200
height = 800
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("bat may bay")
#tao lop nhan vat nguoi chơi
#pygame.mixer.music.load("C:\\Users\\ASUS\\OneDrive\\NangPTIT\\test\\game\\nhac1.mp3")
#pygame.mixer.music.play(loops=-1)
#music_kill = pygame.mixer.Sound("amthanhmaybayno.ogg")

class Player(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.surf = pygame.image.load("pixel_ship_yellow.png")
		#xoa phon
		self.surf.set_colorkey((0,0,0),pygame.RLEACCEL) #xoa phong mau tranng
		self.rect = self.surf.get_rect(
			center = (400,400)
		) #gọi nó ra ở góc trái trên cùng màn hình
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
		if self.rect.bottom > height:
			self.rect.bottom = height	
		if self.rect.left < 0:
			self.rect.left = 0	
		if self.rect.right > width:
			self.rect.right = width	

class Enemy(pygame.sprite.Sprite) :
	def __init__(self) :
		super(Enemy,self).__init__()
		self.surf = pygame.image.load("pixel_ship_blue_small.png")
		#self.surf.fill((0,0,0))
		self.surf.set_colorkey((0,0,0),pygame.RLEACCEL)
		self.rect = self.surf.get_rect(
			center =((random.randint(20,1000)),(random.randint(0,10)))
		)
		self.speed = 3# tốc độ của địch đi ra
	def update(self) :
		self.rect.move_ip(0,self.speed)
		if self.rect.bottom > height :
			self.kill()
			self.rect = self.surf.get_rect(
				center =((random.randint(20,700)),(random.randint(0,10)))
			)						

AddEnemy = pygame.USEREVENT + 1
pygame.time.set_timer(AddEnemy,1000)

enemies = pygame.sprite.Group()
player = Player()
all_sprites = pygame.sprite.Group() #gom nhung thang giong nhau lai
all_sprites.add(player)
running = True
while running:
	clock.tick(120)
	for event in pygame.event.get():
		if event.type == KEYDOWN :
			if event.type == K_ESCAPE :
				running == False
		elif event.type == QUIT:
			running = False
		elif event.type == AddEnemy :
			#tao them mot quan dich moi 
			new_enemy = Enemy()
			enemies.add(new_enemy)
			all_sprites.add(new_enemy)
	pressed_key = pygame.key.get_pressed()
	player.update(pressed_key)
	enemies.update()
	screen.fill((255,255,255)) #màu xanh da
	for entity in all_sprites :
		screen.blit(entity.surf,entity.rect) #đổi bề mặt này sang bề mặt khác
	# cài đặt va chạm với nhiều vật thể 
	if pygame.sprite.spritecollideany(player,enemies) :
		player.kill()
		#music_kill.play()
		time.sleep(1)
		running = False

	pygame.display.flip() # cập nhật màu liên tục
pygame.mixer.music.stop()
pygame.quit()
