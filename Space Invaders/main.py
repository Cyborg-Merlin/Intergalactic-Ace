import pygame
from player import *

class Game():

    def __init__(self):
        pygame.display.init()
        pygame.display.set_mode((500, 500))

        self.player = Player()
        self.game_Running = True


    def update(self):
        pygame.display.update()
        
        self.player.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                self.game_Running = False
        
        pass

    def draw(self):
        pygame.display.get_surface().fill("Black")
        self.player.draw(pygame.display.get_surface())
        pygame.display.flip()
        pass

game = Game()

while(game.game_Running == True):
    game.update()
    if (game.game_Running == True):
        game.draw()
    