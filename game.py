import pygame
from sys import exit
import os
import random

pygame.init()

# Set up main display. The clock is used to control frame rate.
screen = pygame.display.set_mode((500,700))
pygame.display.set_caption('Star Trek: Asteroid Belt Evasion')
clock = pygame.time.Clock()
game_active = True
frame_count = 0
score = 0 # Initialize score
pixel_font = pygame.font.Font('font/Pixeltype.ttf',50)

# Creating a background image.
space_surface = pygame.image.load('graphics/space.png').convert()

class Meteor(pygame.sprite.Sprite):
    def __init__(self, image, start_pos):
        super().__init__()
        self.image=image
        self.rect = self.image.get_rect()
        self.rect.topleft = start_pos
        self.speed = random.randint(1,4)
        self.rotation = random.randint(-1,1)

    def update(self):
        self.rect.y += self.speed
        if self.rect.top > pygame.display.get_surface().get_height():
            self.kill()

meteor_image = pygame.image.load('graphics/meteor.png').convert_alpha()
meteors = pygame.sprite.Group()

def create_meteor(start_pos):
    new_meteor = Meteor(meteor_image, start_pos)
    meteors.add(new_meteor)

class Ship(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        self.movex = 0
        self.frame = 0
        img = pygame.image.load(os.path.join('graphics', 'shipV.png')).convert_alpha()
        self.images.append(img)
        self.image = self.images[0]
        self.rect = self.image.get_rect(midbottom = (250,600))

    def control(self,x):
        self.movex += x
        self.update()
        self.movex = 0
    
    def update(self):
        self.rect.x = self.rect.x + self.movex
        self.rect.clamp_ip(screen.get_rect())

ship = Ship()
ship_list = pygame.sprite.Group()
ship_list.add(ship)
steps = 10

while True:
    if game_active:
        
        screen.blit(space_surface,(0,0))
        ship_list.draw(screen)

        frame_count += 1
        # Add scoring functionality, so that the score increments every second.
        if frame_count % 60 == 0:
            score += 10 
        score_display = pixel_font.render(f'Score: {score}', True, (255, 255, 255)) #Display score
        screen.blit(score_display, (10, 10)) 

        if frame_count == 30:
            create_meteor((random.randint(10, 700-meteor_image.get_width()), -meteor_image.get_height()))
        if frame_count == 60:
            create_meteor((ship.rect.x,0))
            frame_count = 0

        meteors.update()
        meteors.draw(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT or event.key == ord('d'):
                    ship.control(steps)
                if event.key == pygame.K_LEFT or event.key == ord ('a'):
                    ship.control(-steps)

        if pygame.sprite.spritecollide(ship,meteors,True):
            game_active = False
    else:
        screen.fill('Red')
        restart_message = pixel_font.render('Press SPACEBAR To Restart',False,(0,0,0))
        restart_rect = restart_message.get_rect(center = (250,350))
        screen.blit(restart_message,restart_rect)

        score_message = pixel_font.render(f'Your Score: {score}',False,(0,0,0)) #Display final score
        score_rect = score_message.get_rect(center = (250,400))
        screen.blit(score_message,score_rect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game_active = True
                    meteors.empty()
                    score = 0 #Reset score
    
    pygame.display.update()
    clock.tick(60)