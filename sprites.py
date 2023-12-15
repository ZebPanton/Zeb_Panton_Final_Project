from typing import Any
import pygame as pg
from pygame.sprite import Sprite

from pygame.math import Vector2 as vec
import os
from random import randint
from settings import *


# setup asset folders here - images sounds etc.
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, 'images')
snd_folder = os.path.join(game_folder, 'sounds')

# class Player(Sprite):
#     def __init__(self, game):
#         self.game = game
#         self.image = pg.image.load(os.path.join(img_folder, 'Dino.png')).convert()
#     def controls(self):
        

        

class Animatronic(Sprite):
    def __init__(self, x, y, w, h):
        Sprite.__init__(self)
        self.image = pg.Surface((w, h))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = 1
        self.location = 0
        self.pos = vec(WIDTH, HEIGHT)
        self.path = []

    # def update(self):
        # every "hour" the probabilty to move goes up

    def movement_opportunity(self):
        moveChance = randint(1, 20 - self.speed)
        if moveChance == 1:
            self.location += 1

class Button(Sprite):
    def __init__(self, x, y, w, h):
        Sprite.__init__(self)
        self.image = pg.Surface((w, h))
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.rect.x = x - w/2
        self.rect.y = y - h/2
        # self.kind = kind
        self.pos = vec(WIDTH, HEIGHT)
        self.clickflag = False
        self.name = 0
    def update(self):
        pass
    def is_clicked(self):
        return pg.mouse.get_pressed()[0] and self.rect.collidepoint(pg.mouse.get_pos())
            
    
class Background(Sprite):
    def __init__(self, x, y, photo):
        Sprite.__init__(self)
        self.image = pg.image.load(os.path.join(img_folder, photo))
        self.rect = self.image.get_rect()
        self.rect.x = x 
        self.rect.y = y
        self.pos = vec(WIDTH/2, HEIGHT/2)
        