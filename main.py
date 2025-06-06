# Programmer(s): Max, Logan, Noah
# Date: 29/05/25
# Description: Five Night's at Freddy's but with Mr.Nagra and us
import pygame
from pygame import * # type: ignore
from pygame.sprite import * # type: ignore
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

#Variables for determining whether the play can perform certain actions
actions = {"CanWindow": False,
"CanDoor": False,
"CanCamera": False,
"CanClose": False,
"CanLook": False,
"CanDisableMusic": False,
"CanFlashlight": False,
"LookingAtDoor": False,
"FlashlightActive": False,
"DoorClosed": False,
"MusicBlaring": False,
"NightActive": False,
"ComputerOff": False,
"State": "MENU", #Variable for determining player location, including "WINDOW", "DOOR", "DESK", "CAMERA", "MENU", "LOOKING", "WIN", "LOSS"
"Night": 1,
"Camera": 1, #Defaults to Logan's hall
"StartTime": 0.00} #Float for storing the time the night started in milliseconds

animatronicHandler = {
    "MaxProgress": 0.00, #Percentage values, 1.00 being full progress and triggering an attack, after which is reset to zero (except Logan)
    "NagraProgress": 0.00,
    "LoganProgress": 0.00,
    "NoahChance": 0,
    "MaxAttacking": False, #Booleans for drawing the correct image when each enemy is attacking
    "NagraAttacking": False,
    "NoahAttacking": False, #Logan has no attacking variable because he cannot be stopped
    "WindowBroken": False,
    "MaxInterval": 0, #Empty numbers for storing the start time of the night (since it's relative) plus the attack intervals in milliseconds
    "NagraInterval": 0, #For example, Mr.Nagra's interval for checking movement is 5 seconds, so we'll take the time started and add 5000 milliseconds
    "LoganInterval": 0, #If the current time is equal to the interval or greater, roll for movement.
}

def play_valve_intro():
    pygame.init()
    pygame.mixer.init()

    # Load music and image
    audio_path = "Assets/Audio/Valve_intro.mp3"
    image_path = "Assets/Sprites/ValveIntro.jpg"
    pygame.mixer.music.load(audio_path)
    music_length = pygame.mixer.Sound(audio_path).get_length()

    # Fade timings
    audio_fade_in_duration = 4.0
    fade_out_duration = 3.0
    image_fade_in_duration = 6.0
    image_fade_in_delay = 2.0
    image_fade_out_early = 2.0

    # Set up display
    screen = pygame.display.set_mode((1280, 720))
    image = pygame.image.load(image_path).convert_alpha()
    image_rect = image.get_rect(center=(1280 // 2, 720 // 2))

    pygame.mixer.music.set_volume(0.0)
    pygame.mixer.music.play(loops=0)

    clock = pygame.time.Clock()
    start_time = time.time()

    running = True
    while running:
        elapsed = time.time() - start_time

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                break

        # === Audio Fade Logic ===
        if elapsed < audio_fade_in_duration:
            volume = elapsed / audio_fade_in_duration
        elif elapsed >= music_length - fade_out_duration:
            fade_out_progress = (elapsed - (music_length - fade_out_duration)) / fade_out_duration
            volume = max(0.0, 1.0 - fade_out_progress)
        else:
            volume = 1.0

        pygame.mixer.music.set_volume(volume)

        # === Image Alpha Logic ===
        if elapsed < image_fade_in_delay:
            image_alpha = 0
        elif elapsed < image_fade_in_delay + image_fade_in_duration:
            progress = (elapsed - image_fade_in_delay) / image_fade_in_duration
            image_alpha = int(min(255, progress * 255))
        elif elapsed > music_length - fade_out_duration - image_fade_out_early:
            progress = (elapsed - (music_length - fade_out_duration - image_fade_out_early)) / fade_out_duration
            image_alpha = int(max(0, (1 - progress) * 255))
        else:
            image_alpha = 255

        image.set_alpha(image_alpha)
        screen.fill((0, 0, 0))
        screen.blit(image, image_rect)
        pygame.display.flip()

        if elapsed >= music_length:
            running = False

        clock.tick(60)

    pygame.mixer.music.pause()
    pygame.mixer_music.unload()
    pygame.mixer_music.set_volume(1.0)
        
def DrawMenuScreen():
        pygame.font.get_fonts()
        pygame.font.SysFont("Assets/Sprites/Sans.ttf", 56, bold=False, italic=False)
        MenuImage = pygame.image.load("Assets/Sprites/MenuScreen.png").convert_alpha()
        Image_Rect = MenuImage.get_rect()
        red = (200, 50, 0)

        font = pygame.font.Font("Assets/Sprites/Sans.ttf", 56)
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
        
        screen.fill(BLACK)

        screen.blit(MenuImage, Image_Rect)
        screen.blit(text1, text_rect)
        screen.blit(text2, text_rect2)
        screen.blit(text3, text_rect3)
        screen.blit(text4, text_rect4)
        screen.blit(text5, text_rect5)
        screen.blit(text6, text_rect6)

        pygame.display.flip()

def NewGamePressed():
    print("Newgame")
    actions["State"] = ""
    screen.fill(BLACK)
    pygame.display.flip()
    StoryIntroduction()

def StoryIntroduction():
    print("intro")
    #Cleaning up
    pygame.mixer_music.fadeout(2000)
    pygame.mixer_music.unload()
    #Draw the newspaper here
    #fade in and out with a for loop so it only runs once or twice (we can have 2 for loops)
    NightStart(actions["Night"])

def DrawDeskScreen():
    actions["State"] = "DESK"
    actions["CanLook"] = True
    actions["CanCamera"] = True
    actions["CanWindow"] = True
    actions["CanDoor"] = True

def DrawWindow():
    pass
    
def LookAtDoor():
    actions["State"] = "LOOKING"
    actions["CanCamera"] = False
    actions["CanFlashlight"] = True

def DrawLookingOver():
    pass

def RunToDoor():
    actions["CanCamera"] = False
    actions["CanFlashlight"] = False
    actions["CanDisableMusic"] = False
    actions["CanClose"] = False
    actions["CanLook"] = False
    #color screen black/draw fading rectangle that covers entire screen while playing running sound

    #After running
    actions["State"] = "DOOR"
    actions["CanCamera"] = False
    actions["CanFlashlight"] = True
    
def DrawAtDoor():
    pass

def RunToComputer():
    actions["State"] = "RUNNING"
    #Play running sound here
    DrawDeskScreen()

def RunToWindow():
    actions["State"] = "RUNNING"
    #Running sound

    actions["State"] = "WINDOW"

def OpenCameras():
    actions["State"] = "CAMERA"
    actions["CanDoor"] = False
    actions["CanWindow"] = False

def SwitchCameras(camera):
    pass

def CloseCameras():
    actions["CanDisableMusic"] = False
    actions["State"] = "DESK"
    
def Flashlight():
    actions["FlashlightActive"] = True

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
    animatronicHandler["WindowBroken"] = True

def MaxJumpscare():
    pass

def NoahAppear():
    actions["CanCamera"] = False

def ComputerShutoff():
    actions["ComputerOff"] = True

def ComputerPowerOn():
    #Play computer startup sound
    #Computer cannot be used for a little bit, 5 seconds maybe?
    actions["ComputerOff"] = False

def NagraJumpscare():
    pass

def CloseDoor():
    actions["CanCamera"] = False
    actions["CanFlashlight"] = False

def ShutOffMusic():
    pass
        
def PlayMusic():
    actions["MusicBlaring"] = True
    pass

def GameOverScreen():
    pass

def RetryButtonPressed():
    pass

def NightWin():
    actions["NightActive"] = False
    actions["Night"] += 1
    actions["CanLook"] = False
    actions["CanClose"] = False
    actions["CanCamera"] = False
    actions["CanDisableMusic"] = False
    actions["MusicBlaring"] = False
    actions["CanDoor"] = False
    actions["CanWindow"] = False
    actions["CanFlashlight"] = False
    actions["State"] = "WIN"
    #Play winning music here
    #Draw winning clock or something here

def NightStart(night):
    actions["NightActive"] = True
    actions["State"] = "DESK"
    actions["CanCamera"] = True
    actions["CanLook"] = True
    actions["StartTime"] = pygame.time.get_ticks()
    DrawDeskScreen()


def CheckWin():
    if pygame.time.get_ticks() >= actions["StartTime"] + 270000:
        NightWin()

play_valve_intro()
MenuSong = pygame.mixer_music.load("Assets/Audio/MenuTheme.mp3")

# MAIN GAME LOOP
running = True
while running:  
    # keep loop running at the right speed 
    clock.tick(FPS)
    # process input (events)
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False      
    ### ADD ANY OTHER EVENTS HERE (KEYS, MOUSE, ETC.) ### 
    if pygame.mouse.get_pressed()[0]:
        red = (200, 50, 0)
        font = pygame.font.Font("Assets/Sprites/Sans.ttf", 56)
        text5 = font.render("Start Game", True, (red))
        text_rect5 = text5.get_rect(center=(185, 450))
        text6 = font.render("Quit", True, (red))
        text_rect6 = text6.get_rect(center=(80, 550))
        mouse_pos = pygame.mouse.get_pos()
        if text_rect5.collidepoint(mouse_pos) and actions["NightActive"] != True:
           NewGamePressed()
        elif text_rect6.collidepoint(mouse_pos):
            running = False    
    if actions["State"] == "MENU":
        DrawMenuScreen()
    
    if actions["State"] == "MENU" and pygame.mixer_music.get_busy() == False:
        pygame.mixer_music.play()

    if actions["State"] == "DESK":
        DrawDeskScreen()

    if actions["State"] == "WINDOW":
        DrawWindow()
        
    # game loop updates (including movement)
    ### ADD ANY GAME LOOP UPDATES HERE ###

    # check for keypresses
    #keys = pygame.key.get_pressed()
    
    #if keys[K_LEFT]:
        # do something
    #if keys[K_RIGHT]:
        # do something 
    CheckWin()
    # game loop drawing
    ### ADD ANY GAME LOOP DRAWINGS HERE ###
    
    # update position of sprites
    
    # render sprites on screen
    allSprites.draw(screen)
    
    # ***AFTER*** drawing everything, flip (update) the display
    pygame.display.flip()
    
pygame.quit()
