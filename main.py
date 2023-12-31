# This file(s) was created by: Zeb Panton
# Huge inspiration from the fact my cousin, Mark Panton Solomita, could make fnaf on scratch https://scratch.mit.edu/projects/645165777/
# content from kids can code: http://kidscancode.org/blog/

'''
############# Overview #############
Player is person stuck in a single room and has to use the cameras
to keep track of the enemies trying to get to their room. Once the enemy
gets to their room they lose. The player can use the information from the 
camera to their advantage so they can know what to do to prevent themselves from being killed
############## To Do ##############
Add "animatronics"
- each animatronic has a set path through the map
- each animatronic has a chance to move every movement tick
- when an animatronic makes it to the player they lose
- only show up in the cam that is on their location
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

    def new(self):
        # load in variables I'm going to be using in loop
        self.CameraMode = False
        self.CameraScreen = 0
        self.CamsList = []
        self.clickflag = False
        self.officeinstantiated = False
        self.camsinstantiated = False
        self.door1opened, self.door2opened = True, True
        self.doors = [self.door1opened, self.door2opened]

        # create a group for all sprites
        self.score = 0
        self.all_sprites = pg.sprite.Group()
        self.all_animatronics = pg.sprite.Group()
        self.all_buttons = pg.sprite.Group()
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

        self.camMap = Background(*camMapBG)

        DoorButt1 = Button(30, HEIGHT/2, 50, 50)
        DoorButt2 = Button(WIDTH -30, HEIGHT/2, 50, 50)
        DoorButt1.image.fill(RED)
        DoorButt2.image.fill(RED)
        DoorButt2.name = 1
        self.DoorButtList = [DoorButt1, DoorButt2]

        Bot1 = Animatronic(0, HEIGHT/2, 100, 200)
        Bot2 = Animatronic(WIDTH /2, HEIGHT /2, 100, 200)
        Bot3 = Animatronic(WIDTH -100, HEIGHT /2, 100, 200)

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

        # if player mouse = bottom of screen then toggle on/off camera mode
        # https://stackoverflow.com/questions/10990137/pygame-mouse-clicking-detection for "flags"
        if (mouse[0] < SCREENRIGHT - 50 or mouse[0] > SCREENLEFT + 50) and (mouse[1] > SCREENBOTTOM) and not self.hovered:
            self.CameraMode = not self.CameraMode
            print("CameraMode is on:",self.CameraMode)
        self.hovered = (mouse[0] < SCREENRIGHT + 50 or mouse[0] > SCREENLEFT - 50) and mouse[1] > SCREENBOTTOM

        # what the game does while player is looking at cams
        if self.CameraMode:
            if not self.camsinstantiated:
                for cams in self.CamsList:
                    self.all_sprites.add(cams)
                    self.all_buttons.add(cams)
                for doors in self.DoorButtList:
                    doors.kill()
                self.all_sprites.add(self.camMap)
                self.camsinstantiated = True
                self.officeinstantiated = False
                print("cams have been instantiated")

            # my detection for if the player hits a cam button
            x = 0
            for cams in self.CamsList:
                if cams.is_clicked() and not self.clickflag:
                    print("you clicked on cam", cams.name)
                    self.CameraScreen = cams.name
                x += 1
            self.clickflag = pg.mouse.get_pressed()[0]


        # what the game does while player is looking in office
        else:
            # only need to run this line once so made a system to make sure
            if not self.officeinstantiated: 
                for cams in self.CamsList:
                    cams.kill()
                for doorbutt in self.DoorButtList:
                    self.all_sprites.add(doorbutt)
                    self.all_buttons.add(doorbutt)
                self.camMap.kill()
                self.camsinstantiated = False
                self.officeinstantiated = True
                print("office has been instantiated")

            # if door button clicked then door = closed/opened
            for doorbutt in self.DoorButtList:
                if doorbutt.is_clicked() and not self.clickflag:
                    self.doors[doorbutt.name] = not self.doors[doorbutt.name]
                    print(self.doors[doorbutt.name])
                    # print(doorbutt.name)
            self.clickflag = pg.mouse.get_pressed()[0]




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
