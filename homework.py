import pygame
import random
from pygame.locals import *

pygame.init()

clock = pygame.time.Clock()
fps = 60
screen_width =1400
screen_height = 600

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("TNT Dodge")

scroll_speed = 6
game_over = False
spawn_frequency = 900
last_spawn = pygame.time.get_ticks()

tnt_img =pygame.image.load("tnt.png")
car_img =pygame.image.load("car.png")

class Car(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = car_img
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[K_LEFT] and self.rect.left > 0:
            self.rect.x -= 8
        if keys[K_RIGHT] and self.rect.right < screen_width:
            self.rect.x += 8

class TNT(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = tnt_img
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def update(self):
        self.rect.y +=  scroll_speed
        if self.rect.top > screen_height:
            self.kill()

car_group = pygame.sprite.Group()
tnt_group = pygame.sprite.Group()

car = Car(screen_width //2, screen_height - 80)
car_group.add(car)

run = True
while run:

    clock.tick(fps)
    screen.fill((255, 255, 255))

    car_group.draw(screen)
    tnt_group.draw(screen)

    car_group.update()
    tnt_group.update()

    if not game_over:
        now = pygame.time.get_ticks()
        if now - last_spawn > spawn_frequency:
            x_pos = random.randint(50, screen_width - 50)
            tnt = TNT(x_pos, -50)
            tnt_group.add(tnt)
            last_spawn = now

    if pygame.sprite.groupcollide(car_group, tnt_group,False, False):
        game_over = True
        pygame.quit()
        exit()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()