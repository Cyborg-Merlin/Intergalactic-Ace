import pygame

class Player():
    def __init__(self) -> None:
        # center of the screen
        self.position_x = 0.0
        self.position_y = 0.0
        self.speed = 0.1

        # this player's sprite
        self.sprite = pygame.sprite.Sprite()

        # create a new surface and set it to be equal to the sprite's image
        self.sprite.image = pygame.Surface((16, 16))

        # color the new surface red
        self.sprite.image.fill("RED")

        # set this player's sprites's rect to be equal to the surface's rect
        self.sprite.rect = self.sprite.image.get_rect()
        
        # create a new sprite group for the player
        self.sprite_Group = pygame.sprite.Group()

        # add the player's sprite to the player's sprite group
        self.sprite.add(self.sprite_Group)

    # draw this sprite to whatever surface is needed
    def draw(self, surface) -> None:
        self.sprite.rect.x = round(self.position_x) + 250
        self.sprite.rect.y = round(self.position_y) + 250
        self.sprite_Group.draw(surface)
        pass

    # update this object
    def update(self):
        if pygame.key.get_pressed()[pygame.K_RIGHT]:
            self.position_x += self.speed
            print("RIGHT")
        if pygame.key.get_pressed()[pygame.K_LEFT]:
            self.position_x += -1.0 * self.speed
            print("LEFT")
    pass

class Player_Bullet_Group():
    def __init__():
        pass

    def update():
        pass

    def draw():
        pass

    pass

class Player_Bullet():
    def __init__():

        pass

    def destroySelf():

        pass

    def update():

        pass

    def draw():

        pass
    
    pass
