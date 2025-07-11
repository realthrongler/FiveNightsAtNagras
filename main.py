# Programmer(s): Noah, Logan, Max
# Date: 29/05/25
# Description: Five Night's at Freddy's but with Mr.Nagra and us

#Thanks to Max for designing and creating all of the assets (and pixabay for the audio assets)
#Thanks to Logan for programming
import pygame
from pygame import * # type: ignore
from pygame.sprite import * # type: ignore
import time
import random
pygame.mixer.init()
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
CAPTION = "Five Nights At Thong's"
pygame.mixer.set_num_channels(10)
PHONE_CHANNEL = pygame.mixer.Channel(0) #For playing phone voicelines
MUSIC_CHANNEL = pygame.mixer.Channel(1)  #For playing Logan's music
JUMPSCARE_CHANNEL = pygame.mixer.Channel(2) #For playing any jumpscare sound (no way multiple of them happen at once)
AMBIENCE_CHANNEL = pygame.mixer.Channel(3) #For playing the spooky ambience
GLASS_CHANNEL = pygame.mixer.Channel(4) #For playing Max's glass tapping/glass breaking noises
LOGAN_CHANNEL = pygame.mixer.Channel(5) #For playing Logan's voicelines
STATIC_CHANNEL = pygame.mixer.Channel(6) #For playing Noah's static
ACTIONS_CHANNEL = pygame.mixer.Channel(7) #For playing sounds involved with player actions (they will never coincide)
ENDING_CHANNEL = pygame.mixer.Channel(8) #For playing the winning music and also Mr.Nagra's rubble and voiceline sounds
MENUMUSIC_CHANNEL = pygame.mixer.Channel(9)

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
"CanDisableMusic": False,
"CanFlashlight": False,
"LookingAtDoor": False,
"ScreamingAtMax": False,
"DoorClosed": False,
"MusicBlaring": False,
"NightActive": False,
"ComputerOff": False,
"State": "MENU", #Variable for determining player location, including "WINDOW", "DOOR", "DESK", "CAMERA", "MENU", "WIN"
"ComputerTime": 0, #Storing time that the computer startup started to check if the player can use the computer again
"Night": 1, 
"Camera": 1, #Defaults to Logan's hall, 2 is storage room, 3 is just outside storage room, 4 is bench, 5 is mr.nagra chair
"StartTime": 0.00} #Float for storing the time the night started in milliseconds

animatronicHandler = {
    "MaxProgress": 0, #Percentage values, 100 being full progress and triggering an attack, after which is reset to zero (except Logan)
    "NagraProgress": 0,
    "LoganProgress": 0.00, #Logan's value is a float so he can make progress as soon as the music starts playing, and not at an interval
    "NoahChance": 0,
    "MaxLevel": 0, #AI levels, an integer in between 0 and 20
    "NagraLevel": 0,
    "LoganLevel": 0,
    "NoahLevel": 0,
    "MaxAttacking": False, #Booleans for drawing the correct image when each enemy is attacking
    "NagraAttacking": False,
    "NoahAttacking": False,
    "LoganAtDoor": False, #It does not matter if the door is open or closed, this is just for drawing purposes (logan cannot be stopped)
    "WindowBroken": False,
    "MaxInterval": 0, #Empty numbers for storing the start time of the night (since it's relative) plus the attack intervals in milliseconds
    "NagraInterval": 0, #For example, Mr.Nagra's interval for checking movement is 5 seconds, so we'll take the time started and add 5000 milliseconds
    "LoganInterval": 0, #If the current time is equal to the interval or greater, roll for movement.
    "NoahInterval": 0,
    "StaticStarted": False
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
    actions["State"] = ""
    screen.fill(BLACK)
    pygame.display.flip()
    StoryIntroduction()

def StoryIntroduction():
    MENUMUSIC_CHANNEL.fadeout(2000)
    pygame.time.wait(2000)
    image = pygame.image.load("Assets/Sprites/Opening_Poster.png")
    screen.fill(BLACK)
    introposter_rect = image.get_rect()
    screen.blit(image, introposter_rect)
    pygame.display.flip()

    font = pygame.font.Font("Assets/Sprites/Sans.ttf", 36)

    start_time = pygame.time.get_ticks()
    clicked = False

    # Wait for click loop
    while not clicked:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                clicked = True

        current_time = pygame.time.get_ticks()

        # Show text after 5 seconds
        if (current_time - start_time) >= 5000:
            text = font.render("Click anywhere to continue", True, (RED))
            text_rect = text.get_rect(center=(screen.get_width() // 2, screen.get_height() - 25))
            screen.blit(image, introposter_rect)  # Redraw background/poster
            screen.blit(text, text_rect)
            pygame.display.flip()

    NightStart(actions["Night"])

def DrawDeskScreen():
    actions["State"] = "DESK"
    actions["CanCamera"] = True
    actions["CanWindow"] = True
    actions["CanDoor"] = True
    actions["CanDisableMusic"] = False

    screen.fill(BGCOLOUR)
    #Drawing desk
    image = pygame.image.load("Assets/Sprites/Full_Room.png")
    rect = image.get_rect()
    screen.blit(image, rect)

def DrawWindow():
    actions["State"] = "WINDOW"
    actions["CanCamera"] = False
    actions["CanDoor"] = False
    
    screen.fill(BGCOLOUR)

    if animatronicHandler["MaxAttacking"] == False:
        image = pygame.image.load("Assets/Sprites/Window.png")
        rect = image.get_rect()
        screen.blit(image, rect)
    if animatronicHandler["MaxAttacking"] == True:
        image = pygame.image.load("Assets/Sprites/Max_Jumpscare2.jpg")
        rect = image.get_rect()
        screen.blit(image, rect)
    
def RunToDoor():
    actions["State"] = "RUNNING"
    Running_transition()
    DrawAtDoor()

def DrawAtDoor():
    actions["State"] = "DOOR"
    actions["CanCamera"] = False
    actions["CanWindow"] = False
    actions["CanClose"] = True
    
    #Drawing different door image depending on who is there and door is open
    if animatronicHandler["NagraAttacking"] == False and animatronicHandler["LoganAtDoor"] == False and actions["DoorClosed"] == False:
        screen.fill(BGCOLOUR)
        image = pygame.image.load("Assets/Sprites/Door_Open.png").convert()
        rect = image.get_rect()
        screen.blit(image, rect)
    elif animatronicHandler["NagraAttacking"] == True and animatronicHandler["LoganAtDoor"] == False and actions["DoorClosed"] == False:
        screen.fill(BGCOLOUR)
        image = pygame.image.load("Assets/Sprites/NagraDoorOpen.jpg").convert()
        rect = image.get_rect()
        screen.blit(image, rect)
    elif animatronicHandler["NagraAttacking"] == True and animatronicHandler["LoganAtDoor"] == True and actions["DoorClosed"] == False:
        screen.fill(BGCOLOUR)
        image = pygame.image.load("Assets/Sprites/LoganNagraDoorOpened.jpg").convert()
        rect = image.get_rect()
        screen.blit(image, rect)
    elif animatronicHandler["NagraAttacking"] == False and animatronicHandler["LoganAtDoor"] == True and actions["DoorClosed"] == False:
        screen.fill(BGCOLOUR)
        image = pygame.image.load("Assets/Sprites/LoganDoorOpen.jpg").convert()
        rect = image.get_rect()
        screen.blit(image, rect)
    
    #Drawing different door image based on who is there and door is closed
    if actions["DoorClosed"] == True and animatronicHandler["NagraAttacking"] == False and animatronicHandler["LoganAtDoor"] == False:
        screen.fill(BGCOLOUR)
        image = pygame.image.load("Assets/Sprites/Door_Close.png")
        rect = image.get_rect()
        screen.blit(image, rect)
    elif actions["DoorClosed"] == True and animatronicHandler["NagraAttacking"] == True and animatronicHandler["LoganAtDoor"] == False:
        screen.fill(BGCOLOUR)
        image = pygame.image.load("Assets/Sprites/NagraDoorClosed.jpg")
        rect = image.get_rect()
        screen.blit(image, rect)
    elif actions["DoorClosed"] == True and animatronicHandler["NagraAttacking"] == False and animatronicHandler["LoganAtDoor"] == True:
        screen.fill(BGCOLOUR)
        image = pygame.image.load("Assets/Sprites/LoganDoorClosed.jpg")
        rect = image.get_rect()
        screen.blit(image, rect)
    elif actions["DoorClosed"] == True and animatronicHandler["NagraAttacking"] == True and animatronicHandler["LoganAtDoor"] == True:
        screen.fill(BGCOLOUR)
        image = pygame.image.load("Assets/Sprites/LoganNagraDoorClosed.jpg")
        rect = image.get_rect()
        screen.blit(image, rect)
    
def RunToComputer():
    actions["State"] = "RUNNING"
    Running_transition()
    DrawDeskScreen()

def RunToWindow():
    actions["State"] = "RUNNING"
    Running_transition()
    DrawWindow()

def OpenCameras():
    actions["State"] = "CAMERA"
    actions["CanDisableMusic"] = True
    actions["CanDoor"] = False
    actions["CanWindow"] = False
    DrawCameras()

def UpCameras():
    camera = actions["Camera"]
    if camera + 1 == 6:
        actions["Camera"] = 1
        pygame.display.flip()
    else:
        actions["Camera"] += 1
        pygame.display.flip()

def DrawCameras():
    #Logan hall camera
    if actions["Camera"] == 1 and animatronicHandler["LoganLevel"] == 0: 
        image = pygame.image.load("Assets/Sprites/LoganHall1.png")
        rect = image.get_rect()
        screen.blit(image, rect)
    elif actions["Camera"] == 1 and animatronicHandler["LoganLevel"] != 0 and animatronicHandler["LoganProgress"] <= 25:
        image = pygame.image.load("Assets/Sprites/LoganHall2.png")
        rect = image.get_rect()
        screen.blit(image, rect)
    elif actions["Camera"] == 1 and animatronicHandler["LoganLevel"] != 0 and animatronicHandler["LoganProgress"] <= 50 and animatronicHandler["LoganProgress"] > 25:
        image = pygame.image.load("Assets/Sprites/LoganHall3.png")
        rect = image.get_rect()
        screen.blit(image, rect)
    elif actions["Camera"] == 1 and animatronicHandler["LoganLevel"] != 0 and animatronicHandler["LoganProgress"] <= 75 and animatronicHandler["LoganProgress"] > 50:
        image = pygame.image.load("Assets/Sprites/LoganHall4.png")
        rect = image.get_rect()
        screen.blit(image, rect)
    elif actions["Camera"] == 1 and animatronicHandler["LoganLevel"] != 0 and animatronicHandler["LoganProgress"] >= 90 and animatronicHandler["LoganProgress"] < 100:
        image = pygame.image.load("Assets/Sprites/LoganHall1.png")
        rect = image.get_rect()
        screen.blit(image, rect)

    #Storage room camera
    if actions["Camera"] == 2 and animatronicHandler["NagraProgress"] <= 25:
        image = pygame.image.load("Assets/Sprites/NagraStorage1.png")
        rect = image.get_rect()
        screen.blit(image, rect)
    elif actions["Camera"] == 2 and animatronicHandler["NagraProgress"] > 25:
        image = pygame.image.load("Assets/Sprites/NagraStorage2.png")
        rect = image.get_rect()
        screen.blit(image, rect)

    #Hallway camera
    if actions["Camera"] == 3 and animatronicHandler["NagraProgress"] > 25 and animatronicHandler["NagraProgress"] <= 50:
        image = pygame.image.load("Assets/Sprites/NagraHall1.png")
        rect = image.get_rect()
        screen.blit(image, rect)
    elif actions["Camera"] == 3 and (animatronicHandler["NagraProgress"] > 50 or animatronicHandler["NagraProgress"] < 25):
        image = pygame.image.load("Assets/Sprites/NagraHall3.png")
        rect = image.get_rect()
        screen.blit(image, rect)
    
    #Bench camera
    if actions["Camera"] == 4 and animatronicHandler["NagraProgress"] > 50 and animatronicHandler["NagraProgress"] < 75:
        image = pygame.image.load("Assets/Sprites/NagraBench1.png")
        rect = image.get_rect()
        screen.blit(image, rect)
    elif actions["Camera"] == 4 and (animatronicHandler["NagraProgress"] > 75 or animatronicHandler["NagraProgress"] < 50):
        image = pygame.image.load("Assets/Sprites/NagraBench4.png")
        rect = image.get_rect()
        screen.blit(image, rect)
    
    #Chair camera
    if actions["Camera"] == 5 and animatronicHandler["NagraProgress"] > 75 and animatronicHandler["NagraProgress"] < 100:
        image = pygame.image.load("Assets/Sprites/NagraChair3.png")
        rect = image.get_rect()
        screen.blit(image, rect)
    elif actions["Camera"] == 5 and (animatronicHandler["NagraProgress"] >= 100 or animatronicHandler["NagraProgress"] < 75):
        image = pygame.image.load("Assets/Sprites/NagraChair1.png")
        rect = image.get_rect()
        screen.blit(image, rect)
        #Mr.Nagra is now at the door

def DownCameras():
    camera = actions["Camera"]
    if camera - 1 == 0:
        actions["Camera"] = 5
        pygame.display.flip()
    else:
        actions["Camera"] -= 1
        pygame.display.flip()
    
def CloseCameras():
    actions["CanDisableMusic"] = False
    actions["CanDoor"] = True
    actions["CanWindow"] = True
    actions["State"] = "DESK"
    
def ScreamAtMax():
    actions["ScreamingAtMax"] = True
    Scream1 = pygame.mixer.Sound("Assets/Audio/PlayerScream1.mp3")
    Scream2 = pygame.mixer.Sound("Assets/Audio/PlayerScream2.mp3")
    choice = random.randint(1,2)
    if choice == 1 and ACTIONS_CHANNEL.get_busy() == False:
        ACTIONS_CHANNEL.play(Scream1)
    elif choice == 2 and ACTIONS_CHANNEL.get_busy() == False:
        ACTIONS_CHANNEL.play(Scream2)
    animatronicHandler["MaxAttacking"] = False
    
def MaybePlayMusic():
    chance = random.randint(0, 50)
    if chance < animatronicHandler["LoganLevel"]:
        PlayMusic()

def MaxMovement():
    chance = random.randint(0, 35) 
    print("max checked")

    if animatronicHandler["MaxAttacking"] == True and actions["NightActive"] == True and actions["State"] != "MENU":
        MaxWindowBreak()
        pygame.time.wait(2000)
        MaxJumpscare()

    if chance < animatronicHandler["MaxLevel"] and animatronicHandler["MaxAttacking"] == False:
        animatronicHandler["MaxAttacking"] = True
        noisechoice = random.randint(1,2)
        if noisechoice == 1:
            sound = pygame.mixer.Sound("Assets/Audio/Glass_Knocking_1.mp3")
            GLASS_CHANNEL.play(sound)
        elif noisechoice == 2:
            sound = pygame.mixer.Sound("Assets/Audio/Glass_Knocking_2.mp3")
            GLASS_CHANNEL.play(sound)
        
def NagraMovement():
    chance = random.randint(1, 40)
    if animatronicHandler["NagraAttacking"] == True and actions["DoorClosed"] == False:
        NagraJumpscare()
    elif animatronicHandler["NagraAttacking"] == True and actions["DoorClosed"] == True:
        animatronicHandler["NagraProgress"] = 0
        animatronicHandler["NagraAttacking"] = False
        pygame.display.flip()
    if chance < animatronicHandler["NagraLevel"]:
        animatronicHandler["NagraProgress"] += 26
    if animatronicHandler["NagraProgress"] >= 100:
        animatronicHandler["NagraAttacking"] = True

def NoahCheckAttack():
    chance = random.randint(1, 40)
    print(chance < animatronicHandler["NoahLevel"])
    if animatronicHandler["StaticStarted"] == True:
        NoahJumpScare()
    if chance < animatronicHandler["NoahLevel"]:
        animatronicHandler["StaticStarted"] = True
    
def NoahJumpScare():
    screen.fill(BGCOLOUR)
    NoahAttackImage = pygame.image.load("Assets/Sprites/NoahJumpscare.png")
    NoahAttackImageRect = NoahAttackImage.get_rect()
    NoahAttackSound = pygame.mixer.Sound("Assets/Audio/Noah_Buildup.mp3")
    JUMPSCARE_CHANNEL.play(NoahAttackSound)
    for i in range(0, 700):
        screen.blit(NoahAttackImage, NoahAttackImageRect)
        pygame.display.flip()

    
    actions["State"] = "JUMPSCARE"
    GameLoss()

def LoganJumpscare():
    screen.fill(BGCOLOUR)
    jumpscare = pygame.mixer.Sound("Assets/Audio/Logan_Jumpscare.mp3")
    JUMPSCARE_CHANNEL.play(jumpscare)
    image = pygame.image.load("Assets/Sprites/LoganJumpscare.png")
    rect = image.get_rect()
    for i in range(0, 700):
        screen.blit(image, rect)
        pygame.display.flip()
    
    
    actions["State"] = "JUMPSCARE"
    GameLoss()

def CheckInterval():
    time = pygame.time.get_ticks()

    if time >= animatronicHandler["NagraInterval"]: 
        animatronicHandler["NagraInterval"] += 7000 #7 second intervals
        NagraMovement()
    elif time >= animatronicHandler["LoganInterval"] and actions["NightActive"] == True and actions["State"] != "MENU": 
        animatronicHandler["LoganInterval"] += 15000 #15 second intervals
        MaybePlayMusic()
    elif time >= animatronicHandler["MaxInterval"] and actions["NightActive"] == True and actions["State"] != "MENU": 
        animatronicHandler["MaxInterval"] += 10000 #10 second intervals
        MaxMovement()
    elif time >= animatronicHandler["NoahInterval"] and actions["NightActive"] == True and actions["State"] != "MENU": 
        animatronicHandler["NoahInterval"] += 15000 #15 second intervals
        NoahCheckAttack()

def MaxWindowBreak():
    animatronicHandler["WindowBroken"] = True
    sound = pygame.mixer.Sound("Assets/Audio/GlassBreak.mp3")
    GLASS_CHANNEL.play(sound)

def MaxJumpscare():
    screen.fill(BGCOLOUR)
    image = pygame.image.load("Assets/Sprites/Max_Jumpscare4.png")
    rect = image.get_rect()
    jumpscare = pygame.mixer.Sound("Assets/Audio/Max_Jumpscare.mp3")
    JUMPSCARE_CHANNEL.play(jumpscare)
    for i in range(0, 700):
        screen.blit(image, rect)
        pygame.display.flip()
    
    actions["State"] = "JUMPSCARE"
    GameLoss()

def ComputerShutoff():
    actions["ComputerOff"] = True
    actions["State"] = "DESK"

    ShutoffSound = pygame.mixer.Sound("Assets/Audio/ComputerOff.mp3")
    ACTIONS_CHANNEL.play(ShutoffSound)

def ComputerPowerOn():
    actions["CanDoor"] = False
    actions["CanWindow"] = False
    StartSound1 = pygame.mixer.Sound("Assets/Audio/ComputerOn.mp3")
    StartSound2 = pygame.mixer.Sound("Assets/Audio/ComputerOnTwo.mp3")
    
    ACTIONS_CHANNEL.play(StartSound1)
    ACTIONS_CHANNEL.queue(StartSound2)
    pygame.time.wait(int(StartSound2.get_length()))
    
    actions["CanDoor"] = True
    actions["CanWindow"] = True
    actions["ComputerOff"] = False

def NagraJumpscare():
    screen.fill(BGCOLOUR)
    NagraJumpscareImage = pygame.image.load("Assets/Sprites/NagraJumpscare.png")
    NagraJumpscareImageRect = NagraJumpscareImage.get_rect()
    NagraJumpscareSound = pygame.mixer.Sound("Assets/Audio/Nagra_Jumpscare.mp3")
    JUMPSCARE_CHANNEL.play(NagraJumpscareSound)
    pygame.display.flip()
    for i in range(0, 200):
        print(i)
        screen.blit(NagraJumpscareImage, NagraJumpscareImageRect)
        pygame.display.flip()
    
    actions["State"] = "JUMPSCARE"
    GameLoss()

def CloseDoor():
    actions["CanCamera"] = False
    actions["CanFlashlight"] = False

def ShutOffMusic():
    if actions["State"] == "CAMERA" and actions["CanDisableMusic"] == True and actions["ComputerOff"] == False:
        MUSIC_CHANNEL.stop()
        actions["MusicBlaring"] = False
        
def PlayMusic():
    actions["MusicBlaring"] = True
    musicNumber = random.randint(1,2)
    if musicNumber == 1:
        song = pygame.mixer.Sound("Assets/Audio/DJ_Toenail.mp3")
        MUSIC_CHANNEL.play(song)
    elif musicNumber == 2:
        song = pygame.mixer.Sound("Assets/Audio/ThickOfIt.mp3")
        MUSIC_CHANNEL.play(song)

def NightWin():
    actions["NightActive"] = False
    actions["CanLook"] = False
    actions["CanClose"] = False
    actions["CanCamera"] = False
    actions["CanDisableMusic"] = False
    actions["MusicBlaring"] = False
    actions["CanDoor"] = False
    actions["CanWindow"] = False
    actions["CanFlashlight"] = False
    animatronicHandler["NagraProgress"] = 0
    animatronicHandler["NagraAttacking"] = False
    animatronicHandler["LoganAtDoor"] = False
    animatronicHandler["LoganProgress"] = 0.00
    AMBIENCE_CHANNEL.stop()
    MUSIC_CHANNEL.stop()
    PHONE_CHANNEL.stop()
    ACTIONS_CHANNEL.stop()
    PHONE_CHANNEL.stop()
    LOGAN_CHANNEL.stop()

    win_image = pygame.image.load("Assets/Sprites/Win_clock.png")
    rect = win_image.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2))
    sound = pygame.mixer.Sound("Assets/Audio/Alarm_Clock.mp3")
    sound.play()

    start_time = pygame.time.get_ticks()
    flash_interval = 500  # ms
    show = True

    while pygame.time.get_ticks() - start_time < 6000:  # 6 seconds
        screen.fill((0, 0, 0))
        if show:
            screen.blit(win_image, rect)
        pygame.display.flip()
        pygame.time.delay(flash_interval)
        show = not show
    if actions["Night"] + 1 == 6:
        actions["State"] = "WIN"
    elif actions["Night"] + 1 != 6:
        actions["Night"] += 1
        NightStart(actions["Night"])

def NightStart(night):
    #Setting start time for tracking when the night is over (after 4 minutes and 30 seconds)
    actions["StartTime"] = pygame.time.get_ticks()
    #Setting variables
    actions["NightActive"] = True
    actions["State"] = "DESK"
    actions["CanCamera"] = True
    actions["CanLook"] = True

    #Introduction to night
    screen.fill(BLACK)
    font = pygame.font.Font("Assets/Sprites/Sans.ttf", 24)
    text7 = font.render("Night "+ str(actions["Night"]), True, (red))
    text_rect7 = text7.get_rect(center=(640, 360))
    screen.blit(text7, text_rect7)
    pygame.display.flip()
    pygame.time.wait(5000)

    FirstAudio = pygame.mixer.Sound("Assets/Audio/Night1Audio.mp3")
    SecondAudio = pygame.mixer.Sound("Assets/Audio/Night2Audio.mp3")
    ThirdAudio = pygame.mixer.Sound("Assets/Audio/Night3Audio.mp3")
    if night == 1:
        PHONE_CHANNEL.play(FirstAudio)
    elif night == 2:
        PHONE_CHANNEL.play(SecondAudio)
    elif night == 3:
        PHONE_CHANNEL.play(ThirdAudio)

    #Updating initial intervals for animatronic movement checks
    animatronicHandler["MaxInterval"] = actions["StartTime"] + 10000
    animatronicHandler["NagraInterval"] = actions["StartTime"] + 7000
    animatronicHandler["LoganInterval"] = actions["StartTime"] + 15000
    #Setting AI levels for each animatronic based on the night
    if night == 1:
        animatronicHandler["NagraLevel"] = 5
        animatronicHandler["MaxLevel"] = 5
        animatronicHandler["NoahLevel"] = 0
        animatronicHandler["LoganLevel"] = 0
    elif night == 2:
        animatronicHandler["NagraLevel"] = 7
        animatronicHandler["MaxLevel"] = 10
        animatronicHandler["NoahLevel"] = 0
        animatronicHandler["LoganLevel"] = 5
    elif night == 3:
        animatronicHandler["NagraLevel"] = 10
        animatronicHandler["MaxLevel"] = 12
        animatronicHandler["NoahLevel"] = 5
        animatronicHandler["LoganLevel"] = 10
    elif night == 4:
        animatronicHandler["NagraLevel"] = 14
        animatronicHandler["MaxLevel"] = 15 
        animatronicHandler["NoahLevel"] = 10 
        animatronicHandler["LoganLevel"] = 14 
    elif night == 5:
        animatronicHandler["NagraLevel"] = 17
        animatronicHandler["MaxLevel"] = 17
        animatronicHandler["NoahLevel"] = 17
        animatronicHandler["LoganLevel"] = 17
    DrawDeskScreen()

def CheckWin():
    if pygame.time.get_ticks() >= actions["StartTime"] + 270000 and actions["NightActive"] == True:
        NightWin()

def Running_transition():
    fade_surface = pygame.Surface((screen.get_width(), screen.get_height()))
    fade_surface.fill((0, 0, 0))
    footsteps = pygame.mixer.Sound("Assets/Audio/footsteps.mp3")
    ACTIONS_CHANNEL.play(footsteps)
    # Fade to black (metallica reference?)
    for alpha in range(0, 256, 5): 
        fade_surface.set_alpha(alpha)
        screen.blit(fade_surface, (0, 0))
        pygame.display.flip()
        pygame.time.delay(30)  # fade speed, can change later

    # holds the black screen for a sec, can change later

def GameLoss():
    actions["State"] = "MENU"
    actions["NightActive"] = False
    actions["CanCamera"] = False
    actions["CanClose"] = False
    actions["MusicBlaring"] = False
    MUSIC_CHANNEL.stop()
    animatronicHandler["StaticStarted"] = False
    STATIC_CHANNEL.stop()
    actions["CanDisableMusic"] = False
    actions["ComputerOff"] = False
    actions["CanWindow"] = False
    actions["CanDoor"] = False
    animatronicHandler["NagraProgress"] = 0
    animatronicHandler["LoganProgress"] = 0.00

def DrawUltimateSuperCoolSigmaWin():
    image = pygame.image.load("Assets/Sprites/Ending_Poster.png")
    rect = image.get_rect()

    screen.blit(image, rect)
    pygame.display.flip()
    

play_valve_intro()
MenuSong = pygame.mixer.Sound("Assets/Audio/MenuTheme.mp3")
MENUMUSIC_CHANNEL.play(MenuSong)

# MAIN GAME LOOP
running = True
while running:  

    # keep loop running at the right speed 
    clock.tick(FPS)

    # process input (events)
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

        #Detecting space bar input for the door
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and actions["CanClose"] == True and actions["State"] == "DOOR":
                sound = pygame.mixer.Sound("Assets/Audio/DoorClose.mp3")
                ACTIONS_CHANNEL.play(sound)
                actions["DoorClosed"] = True
            if event.key == pygame.K_SPACE:
                if actions["State"] == "DESK" and actions["CanCamera"] == True and actions["ComputerOff"] == False:
                    OpenCameras()
                elif actions["State"] == "DESK" and actions["CanCamera"] == True and actions["ComputerOff"] == True:
                    sound = pygame.mixer.Sound("Assets/Audio/denied.mp3")
                    ACTIONS_CHANNEL.play(sound)
            if event.key == pygame.K_DOWN:
                if actions["State"] == "CAMERA":
                    DrawDeskScreen()

            #Space bar input for cameras
            if event.key == pygame.K_SPACE and actions["CanCamera"] == True and actions["State"] == "CAMERA":
                OpenCameras()

            #X key input for turning off the cameras
            if event.key == pygame.K_x:
                if actions["State"] == "CAMERA":
                    animatronicHandler["StaticStarted"] = False
                    STATIC_CHANNEL.stop()
                    ComputerShutoff()
                elif actions["State"] == "DESK" and actions["ComputerOff"] == True:
                    ComputerPowerOn()
            
            #Space bar input for window (scaring off max)
            if event.key == pygame.K_SPACE:
                if actions["State"] == "WINDOW" and animatronicHandler["MaxAttacking"] == True:
                    ScreamAtMax()

            #Arrow input for camera switching
            if event.key == pygame.K_RIGHT and actions["State"] == "CAMERA":
                UpCameras()
            if event.key == pygame.K_LEFT and actions["State"] == "CAMERA":
                DownCameras()
            
            #M key for shutting off music
            if event.key == pygame.K_m and actions["MusicBlaring"] == True:
                print("music should shut off now")
                ShutOffMusic()

        #Detecting keyup on the spacebar for the door
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE or actions["State"] != "DOOR":
                actions["DoorClosed"] = False
        
        if event.type == pygame.MOUSEBUTTONDOWN and actions["State"] == "WIN":
            screen.fill(BGCOLOUR)
            pygame.display.flip()
            Rubble = pygame.mixer.Sound("Assets/Audio/rubble.mp3")
            Voiceline = pygame.mixer.Sound("Assets/Audio/Nagra_Voiceline#2.mp3")
            pygame.time.wait(3000)
            ENDING_CHANNEL.play(Rubble)
            pygame.time.wait(2700)
            ENDING_CHANNEL.play(Voiceline)
            pygame.time.wait(2500)
            actions["State"] = "MENU"

    ### ADD ANY OTHER EVENTS HERE (KEYS, MOUSE, ETC.) ### 
    if pygame.mouse.get_pressed()[0] and actions["State"] == "MENU":
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
    
    if actions["State"] == "MENU" and MENUMUSIC_CHANNEL.get_busy() == False:
        MENUMUSIC_CHANNEL.play(MenuSong)

    if actions["State"] == "DESK":
        DrawDeskScreen()

    if actions["State"] == "WINDOW":
        DrawWindow()

    if actions["State"] == "DOOR":
        DrawAtDoor()
    
    if actions["State"] == "CAMERA":
        DrawCameras()
        
    # game loop updates (including movement)
    ### ADD ANY GAME LOOP UPDATES HERE ###

    # check for keypresses
    keys = pygame.key.get_pressed()
    
    #Running around the room
    if keys[K_LEFT] and actions["CanDoor"] == True and actions["State"] == "DESK":
        RunToDoor()
    if keys[K_UP] and actions["State"] == "DESK":
        RunToWindow()
    if keys[K_DOWN] and (actions["State"] == "WINDOW" or actions["State"] == "DOOR"):
        RunToComputer()
    
    CheckWin()

    if actions["NightActive"] == True:
        CheckInterval()

    #Making sure static is playing if the file ends but static playing is true
    if animatronicHandler["StaticStarted"] == True and STATIC_CHANNEL.get_busy() == False:
        STATIC_CHANNEL.play(pygame.mixer.Sound("Assets/Audio/Static.mp3"))    
        
    #Logan's attack mechanic and jumpscare
    if actions["MusicBlaring"] == True:
        animatronicHandler["LoganProgress"] += 0.2
        print(animatronicHandler["LoganProgress"])
        voice1 = pygame.mixer.Sound("Assets/Audio/Logan_Voiceline_Pt1.mp3")
        voice2 = pygame.mixer.Sound("Assets/Audio/Logan_Voiceline_Pt2.mp3")
        if animatronicHandler["LoganProgress"] == 25:
            LOGAN_CHANNEL.play(voice1)
        elif animatronicHandler["LoganProgress"] == 69:
            LOGAN_CHANNEL.play(voice2)
        
        if animatronicHandler["LoganProgress"] > 100:
            LoganJumpscare()
    
    #playing music if none is playing already and music is supposed to be blaring
    if actions["MusicBlaring"] == True and MUSIC_CHANNEL.get_busy() == False:
        PlayMusic()
    
    if actions["MusicBlaring"] == False and MUSIC_CHANNEL.get_busy() == False:
        MUSIC_CHANNEL.stop()
    #ambience playing
    if AMBIENCE_CHANNEL.get_busy() == False and actions["NightActive"] == True:
        song = random.randint(1, 2)
        if song == 1:
            file = pygame.mixer.Sound("Assets/Audio/Ambience.mp3")
            AMBIENCE_CHANNEL.play(file)
        elif song == 2:
            file = pygame.mixer.Sound("Assets/Audio/BoneChillingAmbience.mp3")
            AMBIENCE_CHANNEL.play(file)
    
    if animatronicHandler["LoganProgress"] > 90:
        animatronicHandler["LoganAtDoor"] = True

    if actions["State"] == "WIN":
        DrawUltimateSuperCoolSigmaWin()
    # game loop drawing
    ### ADD ANY GAME LOOP DRAWINGS HERE ###
    
    # update position of sprites
    
    # render sprites on screen
    allSprites.draw(screen)
    
    # ***AFTER*** drawing everything, flip (update) the display
    pygame.display.flip()
    
pygame.quit()