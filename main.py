# Programmer(s): Max, Logan, Noah
# Date: 29/05/25
# Description: Five Night's at Freddy's but with Mr.Nagra and us

from pygame import * # type: ignore
from pygame.sprite import * # type: ignore
from functions import *

import random
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

pygame.mixer.init()

# Load music
pygame.mixer.music.load("Valve_intro.mp3")
music_length = pygame.mixer.Sound("Valve_intro.mp3").get_length()

# Fade settings
audio_fade_in_duration = 4.0
fade_out_duration = 3.0

# Image-specific timing
image_fade_in_duration = 6.0
image_fade_in_delay = 2.0         # Delay image fade-in by 2 seconds
image_fade_out_early = 2.0        # Start fade-out 2 sec *before* audio fade-out

# Start music
pygame.mixer.music.set_volume(0.0)
pygame.mixer.music.play(loops=0)
start_ticks = pygame.time.get_ticks()

# Display setup
screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Valve Intro")

# Load image and center it
image = pygame.image.load("ValveIntro.png").convert_alpha()
image_rect = image.get_rect(center=(1280 // 2, 720 // 2))

clock = pygame.time.Clock()

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

        
running = True
while running:
    current_ticks = pygame.time.get_ticks()
    elapsed_seconds = (current_ticks - start_ticks) / 1000.0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # === Audio Fade-In ===
    if elapsed_seconds < audio_fade_in_duration:
        audio_progress = elapsed_seconds / audio_fade_in_duration
        volume = min(1.0, audio_progress)
    else:
        volume = 1.0

    # === Audio Fade-Out ===
    if elapsed_seconds >= music_length - fade_out_duration:
        fade_out_progress = (elapsed_seconds - (music_length - fade_out_duration)) / fade_out_duration
        volume = max(0.0, 1.0 - fade_out_progress)

    # === Image Alpha (Fade-In with Delay) ===
    image_alpha = 255  # default to full opacity

    if elapsed_seconds < image_fade_in_delay:
        image_alpha = 0  # completely hidden before fade starts
    elif elapsed_seconds < image_fade_in_delay + image_fade_in_duration:
        fade_progress = (elapsed_seconds - image_fade_in_delay) / image_fade_in_duration
        image_alpha = int(min(255, fade_progress * 255))

    # === Image Fade-Out (Start Early) ===
    image_fade_out_start = music_length - fade_out_duration - image_fade_out_early
    if elapsed_seconds >= image_fade_out_start:
        fade_progress = (elapsed_seconds - image_fade_out_start) / fade_out_duration
        image_alpha = int(max(0, (1.0 - fade_progress) * 255))

    # Apply audio and image settings
    pygame.mixer.music.set_volume(volume)
    image.set_alpha(image_alpha)

    # Draw
    screen.fill((0, 0, 0))
    screen.blit(image, image_rect)
    pygame.display.flip()

    clock.tick(60)


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
