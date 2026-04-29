import pygame
import random
pygame.init()

sw = 800
sh = 800

win = pygame.display.set_mode((sw, sh))
pygame.display.set_caption("Cube Jump")

clock = pygame.time.Clock()

white = (255,255, 255)
black = (0,0,0)

class Player(object):
    def __init__(self):
        self.w = 50
        self.h = 50
        self.x = sw//2 - self.w//2
        self.y = sh - self.h - 10
        self.vel = 5
        self.isJump = False
        self.jumpCount = 10

    def draw(self, win):
        pygame.draw.rect(win, black, (self.x, self.y, self.w, self.h ))

    def move(self, keys):
        if keys[pygame.K_LEFT] and self.x > 0:
            self.x -= self.vel
        if keys[pygame.K_RIGHT] and self.x < sw - self.w:
            self.x += self.vel

        if not self.isJump:
            if keys[pygame.K_UP]:
                self.isJump = True
        else:
            if self.jumpCount >= -10:
                neg = 1
                if self.jumpCount < 0:
                    neg = -1
                self.y -= (self.jumpCount ** 2) * 0.3 * neg
                self.jumpCount -= 1
            else:
                self.isJump = False
                self.jumpCount = 10

def redrawGameWindow():
    win.fill(white)
    player.draw(win)
    pygame.display.update()

player = Player()

run = True
while run:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    player.move(keys)

    redrawGameWindow()

pygame.quit()