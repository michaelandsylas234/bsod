import pygame
from pygame.locals import *

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.surf = pygame.Surface((20, 20))
        self.surf.fill((255, 255, 255))
        self.rect = self.surf.get_rect()

    def move_left(self):
        self.move(-5, 0)

    def move_right(self, shifted):
        if shifted:
            self.move(35, 0)
        else:
            self.move(5, 0)

    def move_up(self):
        self.move(0, -5)

    def move_down(self):
        self.move(0, 5)


    def move(self, x, y):
        self.rect.move_ip(x,y)


pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.key.set_repeat(1, 250)

player = Player()

running = True

while running:
    for event in pygame.event.get():
        shifted  = pygame.key.get_mods() & pygame.KMOD_LSHIFT or pygame.key.get_mods() & pygame.KMOD_RSHIFT
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            if event.key == K_LEFT:
                player.move_left()
            if event.key == K_RIGHT:
                player.move_right(shifted)
            if event.key == K_UP:
                player.move_up()
            if event.key == K_DOWN:
                player.move_down()


        elif event.type == pygame.QUIT:
            running = False


    screen.fill((0, 0, 0))
    screen.blit(player.surf, player.rect)
    pygame.display.flip()



