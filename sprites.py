from typing import Any
import pygame as pg
from pygame.sprite import Sprite

from pygame.math import Vector2 as vec
import os
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
        

        

class HoverRect(Sprite):
    def __init__(self, x, y, w, h):
        Sprite.__init__(self)
        self.image = pg.Surface((w, h))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        # self.kind = kind
        self.pos = vec(WIDTH, HEIGHT)

    # def update(self):

class Button(Sprite):
    def __init__(self, x, y, w, h):
        Sprite.__init__(self)
        self.image = pg.Surface((w, h))
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.rect.x = x - w/2
        self.rect.y = y - h/2
        # self.kind = kind
        self.pos = vec(WIDTH/2, HEIGHT/2)
        self.clickflag = False
        # self.clicked = False
        self.name = 0
    # https://www.w3schools.com/python/python_classes.asp
    # def __str__(self):
        # return f"camera({self.name})"
    def update(self):
        # # https://stackoverflow.com/questions/10990137/pygame-mouse-clicking-detection
        # if (self.rect.collidepoint(pg.mouse.get_pos()) and pg.mouse.get_pressed()[0]) and not self.clickflag:
        #     print("button clicked")
        #     # return self.name
        # self.clickflag = pg.mouse.get_pressed()[0] and self.rect.collidepoint(pg.mouse.get_pos())
        pass
    # def update(self):
    #     return pg.mouse.get_pressed()[0] and self.rect.collidepoint(pg.mouse.get_pos())
    def is_clicked(self):
        return pg.mouse.get_pressed()[0] and self.rect.collidepoint(pg.mouse.get_pos())
            
    
# class Background(Sprite):
#     def __init__(self, photo):
#         # self.image = pg.Surface((WIDTH, HEIGHT))
#         # self.image.fill(BLUE)
#         self.image = pg.image.load(os.path.join(img_folder, photo)).convert()
#         self.rect = self.image.get_rect()
#         self.rect.x = 0
#         self.rect.y = 0
#         self.pos = vec(WIDTH/2, HEIGHT/2)
