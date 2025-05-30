import pygame
from main import WIDTH
from main import HEIGHT
from main import screen
from main import BGCOLOUR

IntroImage = pygame.image.load("ValveIntro.jpg").convert_alpha()
PoweredBy = pygame.image.load("PoweredBySource.jpg").convert_alpha()
IntroImage = pygame.image.load("ValveIntro.jpg").convert_alpha()
#PoweredBy = pygame.image.load("PoweredBySource.jpg").convert_alpha()
def StudioIntroduction():
    print("function run")
    Valve_Rect = IntroImage.get_rect()
   #Power_Rect = PoweredBy.get_rect()
    alpha = 255
    Valve_Rect.center = (WIDTH // 2, HEIGHT // 2)
    #Power_Rect.center = (WIDTH // 2, HEIGHT // 2)

    for i in range(255, 0, -1):
        alpha -= 1
        pygame.time.wait(1)
        IntroImage.set_alpha(alpha)

        screen.fill(BGCOLOUR)
        screen.blit(IntroImage, Valve_Rect)
        pygame.display.flip()

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
