# This file was created by: Chris Cozort
# Content from Chris Bradfield; Kids Can Code
# KidsCanCode - Game Development with Pygame video series
# Video link: https://youtu.be/OmlQ0XCvIn0 

# game settings 
WIDTH = 940
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


CAMSWITCH_LIST = [(WIDTH /2, HEIGHT /2, 50, 50),
                  (WIDTH /2 +100, HEIGHT /2 +100, 50, 50),
                  (WIDTH /2 -100, HEIGHT /2 +100, 50, 50)]

BACKGROUND_LIST = [('Dino.png')

]