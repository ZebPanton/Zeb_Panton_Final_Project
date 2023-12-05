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
        self.lookAngle = 0
        self.CameraMode = False
        self.CameraCooldown = 10
        self.CameraScreen = 0
        self.CamsList = []
        self.clickflag = False
        
    def new(self):
        # create a group for all sprites
        self.score = 0
        self.all_sprites = pg.sprite.Group()
        self.all_animatronics = pg.sprite.Group()
        self.all_buttons = pg.sprite.Group()
        # instantiate classes
        # self.player = Player(self)
        # add instances to groups

        # credit to Mr. Cozort for giving me this idea of instantiating all the buttons at once
        # https://www.w3schools.com/python/python_classes.asp
        x = 0
        for b in CAMSWITCH_LIST:
            # instantiation of the Button class
            cswitch = Button(*b)
            cswitch.name = 0 + x
            self.CamsList.append(cswitch)
            x += 1
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
        # https://stackoverflow.com/questions/10990137/pygame-mouse-clicking-detection for "flags"
        if (mouse[0] < SCREENRIGHT - 50 or mouse[0] > SCREENLEFT + 50) and (mouse[1] > SCREENBOTTOM) and not self.hovered:
            self.CameraMode = not self.CameraMode
            print("CameraMode is on:",self.CameraMode)
        self.hovered = (mouse[0] < SCREENRIGHT + 50 or mouse[0] > SCREENLEFT - 50) and mouse[1] > SCREENBOTTOM

        # what the game does while player is looking at cams
        if self.CameraMode:
            for cams in self.CamsList:
            # instantiation of the Button class
                self.all_sprites.add(cams)
                self.all_buttons.add(cams)

            # my detection for if the player hits a button
            # pretty sure there's a better way to do this gotta ask Mr. Cozort has one
            x = 0
            for cams in self.CamsList:
                if cams.is_clicked() and not self.clickflag:
                    print("you clicked on cam", cams.name)
                    self.CameraScreen = cams.name
                x += 1
            self.clickflag = pg.mouse.get_pressed()[0]

        # what the game does while player is looking in office
        else:
            # deletes all instances of the camera buttons after CameraMode is False
            for cams in self.CamsList:
                cams.kill()
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
