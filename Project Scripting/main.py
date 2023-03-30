import pygame
import sys
import display_handler


playing = True

if __name__ == "__main__":
    while (playing == True):    
        display = display_handler.Display()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.display.quit()
                pygame.mixer.quit()
                pygame.quit()
                sys.exit()