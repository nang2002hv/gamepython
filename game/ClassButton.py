import pygame
pygame.init()
font_main = pygame.font.SysFont('cambria', 50)

class button :
	def __init__(self, img, pos_x, pos_y, text_input,scanner,height,width):
		self.img = img
		self.pos_x = pos_x
		self.scanner = scanner #display
		self.height = height
		self.width = width
		self.pos_y = pos_y
		self.text_input = text_input
		self.rect_img = self.img.get_rect(center = (self.pos_x,self.pos_y)) #lưa lại vị trí của ảnh
		self.text = font_main.render(self.text_input, True, 'white')
		self.rect_text = self.text.get_rect(center = (self.pos_x,self.pos_y)) #lưu lại vị  trí của text

	def update(self):
		scanner.blit(self.img, self.rect_img)
		scanner.blit(self.text_input, self.rect_text)

	def checkForInput(self, position):
		if position[0] in range(self.rect_img.left, self.rect_img.right) and position[1] in range(self.rect_img.top, self.rect_img.bottom):
			run = game.pygame1()
			return run
	def changeColor(self,position):
		if position[0] in range(self.rect_img.left, self.rect_img.right) and position[1] in range(self.rect_img.top, self.rect_img.bottom):
			self.text_input = font_main.render(self.text_input, True, "green")
		else :self.text = font_main.render(self.text_input, True, "white")