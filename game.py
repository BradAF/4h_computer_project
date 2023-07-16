import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((500,700))
pygame.display.set_caption('holosim_program7_asteroidbelt')
clock = pygame.time.Clock()

space_surface = pygame.image.load('graphics/space.png').convert()

meteor_surface = pygame.image.load('graphics/meteor.png').convert_alpha()
meteor_rect = meteor_surface.get_rect(midtop = (250,0))

ship_surface = pygame.image.load('graphics/shipV.png').convert_alpha()
ship_rect = ship_surface.get_rect(midbottom = (250,600))
def __init__(self):
    pygame.sprite.Sprite.__init__(self)
    self.movex = 0
    self.frame = 0
def control(self,x):
    self.movey += x
def update(self):
    self.rect.x = self.rect.x + self.movex
ship_list = pygame.sprite.Group()
ship_list.add(ship)
steps = 10



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT or event.key == ord('a'):
                ship.control(-steps,1)
            if event.key == pygame.K_LEFT or event.key == ord ('d'):
                print('left')

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT or event.key == ord('a'):
                print('right stop')
            if event.key == pygame.K_LEFT or event.key == ord ('d'):
                print('left stop')

    screen.blit(space_surface,(0,0))
    meteor_rect.y += 2
    if meteor_rect.top >= 700: meteor_rect.top = -10
    screen.blit(meteor_surface,meteor_rect)
    screen.blit(ship_surface,ship_rect)

    if ship_rect.colliderect(meteor_rect):
        print('collision')

    pygame.display.update()
    clock.tick(60)