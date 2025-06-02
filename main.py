# Programmer(s): Max, Logan, Noah
# Date: 29/05/25
# Description: Five Night's at Freddy's but with Mr.Nagra and us
import pygame
from pygame import * # type: ignore
from pygame.sprite import * # type: ignore
from functions import *
import time
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

#Variables for determining whether the play can perform certain actions
CanWindow = False
CanDoor = False
CanCamera = False
CanClose = False
CanDisableMusic = False
CanFlashlight = False
LookingAtDoor = False
FlashlightActive = False
DoorClosed = False
MusicBlaring = False
#Variable for determining player location, including "WINDOW", "DOOR", "DESK", "CAMERA", "MENU", "INTRODUCTION"
State = ""
def DrawMenuScreen():
        State = "MENU"
        pygame.font.get_fonts()
        pygame.font.SysFont("Sans.ttf", 56, bold=False, italic=False)

        red = (200, 50, 0)

        screen = pygame.display.set_mode((1280, 720))
        font = pygame.font.Font("Sans.ttf", 56)
        text1 = font.render("Five", True, (red))
        text_rect = text1.get_rect(center=(90, 50))
        text2 = font.render("Nights", True, (red))
        text_rect2 = text2.get_rect(center=(120, 125))
        text3 = font.render("At", True, (red))
        text_rect3 = text3.get_rect(center=(60, 200))
        text4 = font.render("Mr. Nagras", True, (red))
        text_rect4 = text4.get_rect(center=(175, 275))
        text5 = font.render("Start Game", True, (red))
        text_rect5 = text5.get_rect(center=(185, 450))
        text6 = font.render("Quit", True, (red))
        text_rect6 = text6.get_rect(center=(80, 550))


        while State == "MENU":
            screen.fill((0, 0, 0))
            screen.blit(text1, text_rect)
            screen.blit(text2, text_rect2)
            screen.blit(text3, text_rect3)
            screen.blit(text4, text_rect4)
            screen.blit(text5, text_rect5)
            screen.blit(text6, text_rect6)

            pygame.display.flip()

def NewGamePressed():
    State = "INTRODUCTION"
    StoryIntroduction()

def StoryIntroduction():
    pass

def DrawDeskScreen():
    pass

def LookAtDoor():
    CanCamera = False
    CanFlashlight = True
    #Draw looking over here

def RunToDoor():
    State = "DOOR"
    CanCamera = False
    #Draw door here

def RunToComputer():
    #Disable player and play running sound

    DrawDeskScreen()

def RunToWindow():
    #Disable player and play running sound

    State = "WINDOW"
    CanFlashlight = True
    CanCamera = False

def OpenCameras():
    State = "CAMERA"
    CanDoor = False
    CanWindow = False

def SwitchCameras(camera):
    pass

def CloseCameras():
    State = "DESK"
    DrawDeskScreen()
    CanDisableMusic = False
    CanCamera = True
    

def Flashlight():
    FlashlightActive = True

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
    CanWindow = False

def MaxJumpscare():
    pass

def NoahAppear():
    CanCamera = False

def ComputerShutoff():
    CanCamera = False

def ComputerPowerOn():
    pass

def NagraJumpscare():
    pass

def CloseDoor():
    CanCamera = False
    CanFlashlight = False

def ShutOffMusic():
    if State == "CAMERAS":
        MusicBlaring = False
        

def PlayMusic():
    MusicBlaring = True
    pass

def GameOverScreen():
    pass

def RetryButtonPressed():
    pass

def NightWin():
    pass

NightActive = False
def NightStart():
    NightActive = True
    StartTime = pygame.time.get_ticks()
    EndTime = StartTime + 270000

    State = "DESK"
    CanCamera = True
    CanWindow = True
    CanDoor = True


        
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
