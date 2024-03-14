# Глобальные библиотеки
import pygame
import sys
import random
# Локальные библиотеки
import colors


screenWidth = 1366
screenHeight = 768
FPS = 60

class Player(pygame.sprite.Sprite):
   def __init__(self):
      pygame.sprite.Sprite.__init__(self)
      self.image = pygame.Surface((50, 50))
      self.image.fill(colors.BLACK)
      self.rect = self.image.get_rect()
      self.rect.center = (screenWidth / 2, screenHeight / 2)

   def update(self):
      self.rect.top += 7
      if self.rect.bottom > screenHeight:
         self.rect.top = 0

# Создание окна и задача основных параметров
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption("Текстовая игра")
clock = pygame.time.Clock()
allSprites = pygame.sprite.Group()
player = Player()
allSprites.add(player)

# Цикл игры
running = True
while running:
   clock.tick(FPS)
   for event in pygame.event.get():
      if event.type == pygame.QUIT:
         running = False
         sys.exit()
         
   # Обновление
   allSprites.update()
   
   # Рендеринг      
   screen.fill(colors.WHITE)
   allSprites.draw(screen)
   
   # Переворот, для быстрого отображения
   pygame.display.flip()
   
pygame.quit()