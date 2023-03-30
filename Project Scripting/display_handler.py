import pygame
import settings

class Display():
    def __init__(this, width : int = 100, height : int = 100):
        pygame.display.init()
        pygame.display.set_mode((width, height))
        pygame.display.set_caption(settings.name)
        pass
    
    def resize(this, width : int = 100, height : int = 100):
        pygame.display.set_mode((width, height))