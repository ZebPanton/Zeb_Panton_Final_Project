# This file(s) was created by: Zeb Panton
# Huge inspiration from the fact my cousin, Mark Panton Solomita, could make fnaf on scratch https://scratch.mit.edu/projects/645165777/
# content from kids can code: http://kidscancode.org/blog/

'''
############# Overview #############


############## Ideas ##############
Fnaf


############## To Do ##############


'''

# import libraries and modules
import pygame as pg
from pygame.sprite import Sprite
import random
from random import randint
import os
from settings import *
from sprites import *
import math


vec = pg.math.Vector2

# setup asset folders here - images sounds etc.
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, 'images')
snd_folder = os.path.join(game_folder, 'sounds')

class Game:
    def __init__(self):
        # init pygame and create a window
        pg.init()
        pg.mixer.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption("Singular Night at Wherever")
        self.clock = pg.time.Clock()
        self.running = True
    
        # load in variables I'm going to be using in loop
        self.lookAngle = 0
        self.CameraMode = False
        # self.CameraCooldown = 10
        self.hovered = False
        
    def new(self):
        # create a group for all sprites
        self.score = 0
        self.all_sprites = pg.sprite.Group()
        self.all_animatronics = pg.sprite.Group()
        self.all_buttons = pg.sprite.Group()
        # instantiate classes
        # self.player = Player(self)
        # add instances to groups

        self.run()
    
    def run(self):
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()

    def update(self): 
        self.all_sprites.update()
        mouse = pg.mouse.get_pos()

        # if player mouse = bottom of screen then toggle off camera mode
        if mouse[0] > SCREENRIGHT + 50 or mouse[0] > SCREENLEFT - 50 and mouse[1] > SCREENBOTTOM and not self.hovered:
            # cooldown so camera isnt just spamming
            # if self.CameraCooldown <= 0:
            self.CameraMode = not self.CameraMode
            self.CameraCooldown = 10
            print("CameraMode is on:",self.CameraMode)
        self.hovered = mouse[0] > SCREENRIGHT + 50 or mouse[0] > SCREENLEFT - 50 and mouse[1] > SCREENBOTTOM

        if self.CameraMode:
            pass
        else:
            '''
            detects when player's mouse is on edge of screen then camera looks around
            found out that the mouse position was a tuple and just needed the x coordinate
            https://www.w3schools.com/python/python_tuples.asp'''
            if mouse[0] > SCREENRIGHT:
                self.lookAngle += 1
                print("player is looking right")
            elif mouse[0] < SCREENLEFT:
                self.lookAngle -= 1
                print("player is looking left")

        # restrain how far player is able to look around
        if 30 < self.lookAngle:
            self.lookAngle = 30
        elif -30 > self.lookAngle:
            self.lookAngle = -30

        # self.CameraCooldown -= 1
        # print(self.CameraMode)
        # print(mouse)
        # print(self.lookAngle)

    def events(self):
        for event in pg.event.get():
        # check for closed window
            if event.type == pg.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False
                
    def draw(self):
        ############ Draw ################
        # draw the background screen
        self.screen.fill(BLACK)
        # draw all sprites
        self.all_sprites.draw(self.screen)
        # buffer - after drawing everything, flip display
        pg.display.flip()
    
    # def draw_text(self, text, size, color, x, y):
    #     

    def show_start_screen(self):
        pass
    def show_go_screen(self):
        pass

g = Game()
while g.running:
    g.new()


pg.quit()
