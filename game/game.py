import random
import time
import pygame
from ClassPlayer import Player1, Player2
from pygame.locals import *
from ClassLaser import LaserEnemy, LaserPlayer, Explosions
from ClassEnemy import Enemy
clock = pygame.time.Clock()  # cài đặt khung hình trên giây
pygame.init()
width = 800
height = 800
scanner = pygame.display.set_mode((width, height))
pygame.display.set_caption("bat may bay")
# ____music,img,text____
pygame.mixer.music.load("nhac1.mp3")
music_kill = pygame.mixer.Sound("amthanhmaybayno.ogg")
font = pygame.font.SysFont('04B_19__.TTF', 50)
img = pygame.image.load("background-black.png")
img = pygame.transform.scale(img, (width, height))


def pygame1(people):
    score = 0
    AddEnemy = pygame.USEREVENT + 1
    pygame.time.set_timer(AddEnemy, 1000)
    # ___Group____
    enemies = pygame.sprite.Group()
    player = pygame.sprite.Group()
    laser_player = pygame.sprite.Group()
    laser_enemy = pygame.sprite.Group()
    all_sprites = pygame.sprite.Group()
    # ___Player___
    player1 = Player1(height, width)
    all_sprites.add(player1)
    player.add(player1)
    if people:
        player2 = Player2(height, width)
        all_sprites.add(player2)
        player.add(player2)
    pygame.mixer.music.play(loops=-1)
    check1 = check2 = 1
    previous_time = pygame.time.get_ticks()
    # ___PLay___
    while True:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == AddEnemy:
                new_enemy = Enemy(height, width)
                enemies.add(new_enemy)
                all_sprites.add(new_enemy)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and check1 == 1:
                    laserplayer1 = LaserPlayer(
                        player1.rect.centerx, player1.rect.centery)
                    all_sprites.add(laserplayer1)
                    laser_player.add(laserplayer1)
                if people and event.key == pygame.K_c and check2 == 1:
                    laserplayer2 = LaserPlayer(
                        player2.rect.centerx, player2.rect.centery)
                    all_sprites.add(laserplayer2)
                    laser_player.add(laserplayer2)
        pressed_key = pygame.key.get_pressed()
        all_sprites.update(pressed_key)
        text = font.render(f"score : {score}", True, "white")
        gets_hits = pygame.sprite.groupcollide(
            enemies, laser_player, True, True)
        for explosion in gets_hits:
            explosion = Explosions(explosion.rect.center)
            all_sprites.add(explosion)
        if gets_hits:
            score += 1
            music_kill.play()
        gets_player = pygame.sprite.groupcollide(enemies, player, True, True)
        if gets_player:
            music_kill.play()
        scanner.blit(img, (0, 0))
        # toc do ra dan
        for enemy in enemies:
            if enemy.laser >= 180:
                new_laser = LaserEnemy(
                    enemy.rect.centerx, enemy.rect.centery, height)
                laser_enemy.add(new_laser)
                all_sprites.add(new_laser)
                enemy.laser = 0
        gets_enemy = pygame.sprite.groupcollide(
            laser_enemy, player, True, True)
        if gets_enemy:
            music_kill.play()
        all_sprites.draw(scanner)
        scanner.blit(text, (width-200, 10))
        if len(player) == 0:
            scanner.blit(pygame.transform.scale(
                pygame.image.load("gameover.jpg"), (height, width)), (0, 0))
            pygame.display.flip()
            pygame.mixer.music.stop()
            time.sleep(1)
            return
        pygame.display.flip()  # cập nhật màu liên tục
