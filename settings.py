# This file was created by: Chris Cozort
# Content from Chris Bradfield; Kids Can Code
# KidsCanCode - Game Development with Pygame video series
# Video link: https://youtu.be/OmlQ0XCvIn0 

# game settings 
WIDTH = 1080
HEIGHT = 480
FPS = 30

# player settings
PLAYER_JUMP = 30
PLAYER_GRAV = 1.5
PLAYER_FRIC = 0.2

# developer shortcuts
SCREENRIGHT = WIDTH -100
SCREENLEFT = 0 +100
SCREENBOTTOM = HEIGHT -50
SCREENTOP = 0 +50

# define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (239, 204, 0)

shiftright = 325 #300
shiftdown = 50 #100

camMapBG = (WIDTH/2 -(350/2) +shiftright, HEIGHT/2 -((350/2)/2) +shiftdown, 'CamMap.png')

CamButtonWidth = 30
CamButtonLength = CamButtonWidth/1.5

CAMSWITCH_LIST = [(WIDTH /2 +103 +shiftright, HEIGHT /2 -57 +shiftdown, CamButtonWidth, CamButtonLength),
                  (WIDTH /2 +147 +shiftright, HEIGHT /2 +6 +shiftdown, CamButtonWidth, CamButtonLength),
                  (WIDTH /2 +47 +shiftright, HEIGHT /2 -57 +shiftdown, CamButtonWidth, CamButtonLength),
                  (WIDTH /2 -49 +shiftright, HEIGHT /2 -57 +shiftdown, CamButtonWidth, CamButtonLength),
                  (WIDTH /2 +47 +shiftright, HEIGHT /2 -27 +shiftdown, CamButtonWidth, CamButtonLength),
                  (WIDTH /2 -47 +shiftright, HEIGHT /2 +40 +shiftdown, CamButtonWidth, CamButtonLength),
                  (WIDTH /2 -145 +shiftright, HEIGHT /2 +7 +shiftdown, CamButtonWidth/1.25, CamButtonLength/1.25),
                  (WIDTH /2 -145 +shiftright, HEIGHT /2 +28 +shiftdown, CamButtonWidth/1.25, CamButtonLength/1.25),
                  (WIDTH /2 -145 +shiftright, HEIGHT /2 +47 +shiftdown, CamButtonWidth/1.25, CamButtonLength/1.25),
                  (WIDTH /2 -110 +shiftright, HEIGHT /2 +65 +shiftdown, CamButtonWidth/1.25, CamButtonLength/1.25)]

BACKGROUND_LIST = [('Dino.png')]

BOT1_POSITION = [(0, HEIGHT/2 -200, 100, 200), (0, HEIGHT/2 -200, 100, 200)]
BOT2_POSITION = [(WIDTH /2, HEIGHT /2 -200, 100, 200)]
BOT3_POSITION = [(WIDTH -100, HEIGHT /2 -200, 100, 200)]
