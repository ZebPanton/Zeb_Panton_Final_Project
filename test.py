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

CAMSCREEN_LIST = [WHITE, BLACK, RED, GREEN, BLUE]

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
        pg.display.set_caption("Testing site for DIY Fnaf")
        self.clock = pg.time.Clock()
        self.running = True
    
        # load in variables I'm going to be using in loop
        self.lookAngle = 0
        self.CameraMode = False
        self.CameraCooldown = 10
        # self.clicked = False
        self.CameraScreen = BLACK
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
            self.all_sprites.add(cswitch)
            self.all_buttons.add(cswitch)
            x += 1
            print(b)

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
        
        # if button #0 clicked go to screen 0 and if button #1 clicked go to screen 1
        x = 0
        for cams in self.CamsList:
            if cams.is_clicked() and not self.clickflag:
                print("you clicked on cam", cams.name)
                self.CameraScreen = CAMSCREEN_LIST[cams.name]
            x += 1
        self.clickflag = pg.mouse.get_pressed()[0]

        # print(self.CameraScreen)

    def events(self):
        for event in pg.event.get():
        # check for closed window
            if event.type == pg.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False
            
            # https://stackoverflow.com/questions/10990137/pygame-mouse-clicking-detection

            
    def draw(self):
        ############ Draw ################
        # draw the background screen
        self.screen.fill(self.CameraScreen)
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





# from https://stackoverflow.com/questions/41064365/pygame-detecting-mouse-cursor-over-object

# def main():
#     pg.init()
#     FPS = 30
#     fpsClock = pg.time.Clock()
#     screen = pg.display.set_mode((600, 400))
#     cat = pg.image.load(os.path.join(img_folder, 'Dino.png')).convert()
#     rect = cat.get_rect(x=300, y=100)  # Create rectangle the same size as 'Dino.png'.

#     while True:
#         if rect.collidepoint(pg.mouse.get_pos()):
#             print("The mouse cursor is hovering over the Dino")

#         for event in pg.event.get():
#             if event.type == QUIT:
#                 pg.quit()
#                 sys.exit()

#         screen.blit(cat, rect)  # Use your rect to position the cat.
#         pg.display.flip()
#         fpsClock.tick(FPS)
# main()