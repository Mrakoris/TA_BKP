import pygame

from game_object import GameObject


class Player(GameObject):
   def __init__(self, x, y, w, h, color, offset):
      GameObject.__init__(self, x, y, w, h)
      self.color = color
      self.offset = offset
      self.moving_left = False
      self.moving_right = False
      self.moving_top = False
      self.moving_bottom = False
      
   def draw(self, surface):
      pygame.draw.rect(surface, self.color, self.bounds)
      