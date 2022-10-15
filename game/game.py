import random
import time
from turtle import speed
import pygame
from ClassPlayer import Player1,Player2
from pygame.locals import *
from ClassLaser import LaserEnemy,LaserPlayer
from ClassEnemy import Enemy
clock = pygame.time.Clock() # cài đặt khung hình trên giây
pygame.init()
width = 800
height = 800
scanner = pygame.display.set_mode((width,height))
pygame.display.set_caption("bat may bay")
pygame.mixer.music.load("nhac1.mp3")
music_kill = pygame.mixer.Sound("amthanhmaybayno.ogg")					
font = pygame.font.SysFont('04B_19__.TTF', 50)
img = pygame.image.load("background-black.png")
img = pygame.transform.scale(img,(width,height))

def pygame1(people):
	score = 0
	AddEnemy = pygame.USEREVENT + 1
	pygame.time.set_timer(AddEnemy,500)

	enemies = pygame.sprite.Group()
	
	player = pygame.sprite.Group()
	
	laserplayer = pygame.sprite.Group()
	
	laserenemy = pygame.sprite.Group()

	all_sprites = pygame.sprite.Group()
	player1 = Player1(height,width)	
	all_sprites.add(player1)
	player.add(player1)
	if people :
		player2 = Player2(height,width)
		all_sprites.add(player2)
		player.add(player2)
	pygame.mixer.music.play(loops=-1)
	check1 = check2 = 1
	dem = 0
	while True:
		clock.tick(60)
		for event in pygame.event.get():
			if event.type == AddEnemy :
				new_enemy = Enemy(height,width)
				enemies.add(new_enemy)
				all_sprites.add(new_enemy)
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_SPACE and check1 == 1:
					laserplayer1 = LaserPlayer(player1.show()[0], player1.show()[1])
					all_sprites.add(laserplayer1)
					laserplayer.add(laserplayer1)
				if people and event.key == pygame.K_c and check2 == 1:
					laserplayer2 = LaserPlayer(player2.show()[0], player2.show()[1])
					all_sprites.add(laserplayer2)
					laserplayer.add(laserplayer2)
		text = font.render(f"score : {score}", True,"white")

		pressed_key = pygame.key.get_pressed()
		gets_hit = pygame.sprite.groupcollide(enemies, laserplayer, True,True)
		if gets_hit:
			music_kill.play()
			score += 1
		all_sprites.update(pressed_key)
		scanner.fill((255,255,255)) #màu xanh da
		gets_player = pygame.sprite.groupcollide(enemies, player, True,True)
		if gets_player:
			music_kill.play()
		if len(player) == 0:
			scanner.blit(pygame.transform.scale(pygame.image.load("gameover.jpg"),(height,width)),(0,0))
			pygame.display.flip()
			pygame.mixer.music.stop()
			time.sleep(1)
			return
		scanner.blit(img,(0,0))
		all_sprites.draw(scanner)
		scanner.blit(text,(width-200, 10))
		pygame.display.flip() # cập nhật màu liên tục
	