import pygame
import random


class Enemy(pygame.sprite.Sprite):
    def __init__(self, height, width):
        super().__init__()
        self.sprites = []  # nhom phi thuyen quan
        # self.surf.fill((0,0,0))
        self.height = height
        self.width = width
        self.sprites.append(pygame.image.load("no1/pixel_ship_red_small.png"))
        self.sprites.append(pygame.image.load("no1/pixel_ship_blue_small.png"))
        self.sprites.append(pygame.image.load(
            "no1/pixel_ship_green_small.png"))
        self.image = self.sprites[random.randint(0, 2)]
        self.rect = self.image.get_rect(
            center=((random.randint(20, width-100), random.randint(-200, -150)))
        )
        self.speed = 2  # tốc độ của địch đi ra
        self.laser = 0

    def update(self, pressed_keys):
        self.rect.move_ip(0, self.speed)
        self.laser += 1
        if self.rect.top > self.height:
            self.kill()
