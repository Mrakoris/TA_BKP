import random
from datetime import datetime, timedelta

import os
import time
import pygame
from pygame.rect import Rect

import config as conf
from game import Game
from player import Player
from text_box import TextBox
from text_object import TextObject

import colors



class TextAdventure(Game):
   def __init__(self):
      Game.__init__(self, 'Текстовое Приключение: Обычные истории', 
                    conf.screen_wight, conf.screen_height, 
                    conf.background_image, conf.frame_rate)