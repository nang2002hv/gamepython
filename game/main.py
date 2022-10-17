import pygame
import sys
from pygame.locals import *
import game
import time
pygame.init()
height = 800
width = 800
scanner = pygame.display.set_mode((width, height))
pygame.display.set_caption("Game xxx")
button_surface = pygame.image.load("button.png")

button_surface = pygame.transform.scale(button_surface, (400, 150))
font_main = pygame.font.SysFont('cambria', 50)


class button:
    def __init__(self, img, pos_x, pos_y, text_input):
        self.img = img
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.text_input = text_input
        self.rect_img = self.img.get_rect(
            center=(self.pos_x, self.pos_y))  # lưa lại vị trí của ảnh
        self.text = font_main.render(self.text_input, True, 'white')
        self.rect_text = self.text.get_rect(
            center=(self.pos_x, self.pos_y))  # lưu lại vị  trí của text

    def update(self):
        scanner.blit(self.img, self.rect_img)
        scanner.blit(self.text, self.rect_text)

    def checkForInput(self, position):
        if position[0] in range(self.rect_img.left, self.rect_img.right) and position[1] in range(self.rect_img.top, self.rect_img.bottom):
            return True

    def changeColor(self, position):
        if position[0] in range(self.rect_img.left, self.rect_img.right) and position[1] in range(self.rect_img.top, self.rect_img.bottom):
            self.text = font_main.render(self.text_input, True, "green")
        else:
            self.text = font_main.render(self.text_input, True, "white")


button1 = button(button_surface, 400, 100, "Play 1 people")
button2 = button(button_surface, 400, 300, "Play 2 people")
button3 = button(button_surface, 400, 500, "Rank")
button4 = button(button_surface, 400, 700, "QUIT")
while True:
    scanner.fill('black')
    pos = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            run1 = run2 = run3 = run4 = False
            run1 = button1.checkForInput(pos)
            run2 = button2.checkForInput(pos)
            run3 = button3.checkForInput(pos)
            run4 = button4.checkForInput(pos)
            if run1:
                game.pygame1(False)
            if run2:
                game.pygame1(True)
            if run3:
                scanner.fill("white")
                scanner.blit(pygame.transform.scale(pygame.image.load(
                    "pixel_ship_yellow.png"), (height, width)), (0, 0))
                time.sleep(0.5)
            if run4:
                pygame.quit()
                sys.exit()

    button1.update()
    button1.changeColor(pos)
    button2.update()
    button2.changeColor(pos)
    button3.update()
    button3.changeColor(pos)
    button4.update()
    button4.changeColor(pos)
    pygame.display.flip()
