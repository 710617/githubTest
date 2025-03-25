import pygame
from pygame.locals import *

#define fps
clock = pygame.time.Clock()
fps = 60


screen_width = 600
screen_height = 600

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Space Invanders')


#load image
bg = pygame.image.load("img/bg.png")

def draw_bg():
    screen.blit(bg, (0, 0))


#create spaceship class
class Spaceship(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("img/spaceship.png")
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]


    def update(self):
        #set movement speed
        speed = 8

        #get key press
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= speed
        if key[pygame.K_RIGHT] and self.rect.right < screen_width:
            self. rect.x += speed


#create sprite groups
spaceship_group = pygame.sprite.Group()


#create player
spaceship = Spaceship(int(screen_width / 2), screen_height - 100)
spaceship_group.add(spaceship)



run =True
while run:

    clock.tick(fps)

    #draw background
    draw_bg()

    #event handlers
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False



            #update spaceship
            spaceship.update()


            #draw sprite group
            spaceship_group.draw(screen)


            pygame.display.update()

pygame.quit()
