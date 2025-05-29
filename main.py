# Programmer(s): Max, Logan, Noah
# Date: 29/05/25
# Description: Five Night's at Freddy's but with Mr.Nagra and us

import pygame
from pygame import * # type: ignore
from pygame.sprite import * # type: ignore

# define colour constants
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
### ADD ANY OTHER COLOUR CONSTANTS HERE ###

# define system constants
FPS = 60
WIDTH = 1280
HEIGHT = 720
BGCOLOUR = BLACK ### CHANGE AS NEEDED ###
CAPTION = "Five Nights at Mr.Thong's"

# initialize pygame, create window, start the clock
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(CAPTION)
clock = pygame.time.Clock()

### ADD YOUR SPRITE CLASSES HERE ###

#class ImageSprite(Sprite):
#    def __init__(self, x, y, filename):                    # NEW sprite at (x,y)
#        Sprite.__init__(self)                              # init the Sprite object
#        self.image = image.load(filename).convert()        # loads the image from filename as the sprite  
#        self.rect = self.image.get_rect()                  # creates the rectangle around the sprite
#        self.rect.center = (x//2,y//2)                           

#    # semi-optional part
#    def update(self):
#        ### ADD MOVEMENT MODIFIERS HERE ###
#        self.rect.x += 5
#        self.rect.y -= 2
#        self.rect.center = (x//2,y//2)  
        

### ADD SPRITE INSTANCES HERE ###

#sprite = ImageSprite(x, y, "INSERT_IMAGE_FILENAME.jpg")

# group sprites
allSprites = pygame.sprite.Group()

def StudioIntroduction():
    pass

def MenuScreen():
    pass

def NewGamePressed():
    pass

def SettingsPressed():
    pass

def StoryIntroduction():
    pass

def DrawOfficeScreen():
    pass

def LookAtDoor():
    pass

def RunToDoor():
    pass

def RunToComputer():
    pass

def RunToWindow():
    pass

def OpenCameras():
    pass

def SwitchCameras(camera):
    pass

def CloseCameras():
    pass

def Flashlight():
    pass

def LoganMovement():
    pass

def MaxMovement():
    pass

def NoahMovement():
    pass

def NagraMovement():
    pass

def LoganJumpscare():
    pass

def MaxWindowBreak():
    pass

def MaxJumpscare():
    pass

def NoahAppear():
    pass

def ComputerShutoff():
    pass

def ComputerPowerOn():
    pass

def NagraJumpscare():
    pass

def CloseDoor():
    pass

def ShutOffMusic():
    pass

def PlayMusic():
    #DJ toenail here
    pass

def GameOverScreen():
    pass

def RetryButtonPressed():
    pass

def NightWin():
    pass

def NightStart():
    pass

# game loop
running = True
while running:
    # keep loop running at the right speed 
    clock.tick(FPS)
    # process input (events)
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        
        ### ADD ANY OTHER EVENTS HERE (KEYS, MOUSE, ETC.) ###
        
    # game loop updates (including movement)
    ### ADD ANY GAME LOOP UPDATES HERE ###
    
    # check for keypresses
    #keys = pygame.key.get_pressed()
    
    #if keys[K_LEFT]:
        # do something
    #if keys[K_RIGHT]:
        # do something 
    
    # game loop drawing
    ### ADD ANY GAME LOOP DRAWINGS HERE ###
    
    # background fill
    screen.fill(BGCOLOUR)
    
    # update position of sprites
    
    
    # render sprites on screen
    allSprites.draw(screen)
    
    # ***AFTER*** drawing everthing, flip (update) the display
    pygame.display.flip()
    
pygame.quit()
