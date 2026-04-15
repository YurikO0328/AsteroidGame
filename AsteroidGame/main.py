import pygame
import math
import random
pygame.init()

sw = 800
sh = 800

bg = pygame.image.load("images/background.png")
alienImg = pygame.image.load("images/alienship.png")
playerRocket = pygame.image.load("images/sateliteship.png")
asteroid50 = pygame.image.load("images/asteroid1")
asteroid100 = pygame.image.load("images/asteroid2")
asteroid150 = pygame.image.load("images/asteroid3")

shoot = pygame.mixer.Sound("soundfx/shoot.wav")
bangLargeSound = pygame.mixer.Sound("soundfx/bangLarge")
bangSmallSound = pygame.mixer.Sound("soundfx/bangSmall")
shoot.set_voulme(.25)
bangLargeSound.set_volume(.25)
bangSmallSound.set_volume(.25)

pygame.display.set_caption("Asteroids")
win = pygame.display.set_mode((sw,sh))
clock = pygame.time.Clock()

gameover = False
lives = 3
score = 0
rapidFire = False
rfstart = -1
isSoundOn = True
highscore = 0

class Player(object):
    def __init__ (self):
        self.img = playerRocket
        self.w = self.img.get_width()
        self.h = self.img.get_height()
        self.x = sw//2
        self.y = sh//2
        self.angle = 0
        self.rotatedSurf = pygame.transform.rotate(self.img,self.angle)
        self.rotatedRect = self.rotatedSurf.get_rect()
        self.rotatedRect.center = (self.x, self.y)
        self.cosine = math.cos(math.radians(self.angle + 90))
        self.sine = math.sin(math.radians(self.angle +90))
        self.head = (self.x + self.cosine * self.w//2, self.y - self.sine * self.h//2)

    def draw(self,win):
        win.blit(self.rotatedSurf, self.rotatedRect)

    def turnLeft(self):
        self.angle += 5
        self.rotatedSurf = pygame.transform.rotate(self.img, self.angle)
        self.rotatedRect = self.rotatedSurf.get_rect()
        self.rotatedRect.center = (self.x,self.y)
        self.cosine = math.cos(math.radians(self.angle+90))
        self.sine = math.sin(math.radians(self.anle+90))
        self.head = (self.x + self.cosine * self.w//2, self.y - self.sine * self.h//2)
    
    def turnRight(self):
        self.angle -= 5
        self.rotatedSurf = pygame.transform.rotate(self.img, self.angle)
        self.rotatedRect = self.rotatedSurf.get_rect()
        self.rotatedRect.center = (self.x,self.y)
        self.cosine = math.cos(math.radians(self.angle+90))
        self.sine = math.sin(math.radians(self.anle+90))
        self.head = (self.x + self.cosine * self.w//2, self.y - self.sine * self.h//2)
    
    def moveForward(self):
        self.x += self.cosine * 6
        self.y -= self.sine * 6
        self.rotatedSurf = pygame.transform.rotate(self.img, self.angle)
        self.rotatedRect = self.rotatedSurf.get_rect()
        self.rotatedRect.center = (self.x,self.y)
        self.cosine = math.cos(math.radians(self.angle+90))
        self.sine = math.sin(math.radians(self.anle+90))
        self.head = (self.x + self.cosine * self.w//2, self.y - self.sine * self.h//2)

    def update(self):
        if self.x > sw + 50:
            self.x = 0
        elif self.x < 0 - self.w:
            self.x = sw
        elif self.y < -50:
            self.y = sh
        elif self.y > sh +50:
            self.y = 0

class Bullet(object):
    def __init__(self):
        self.point = player.head
        self.x, self.y = self.point
        self.w = 4
        self.h = 4
        self.c = player.cosine
        self.s = player.sine
        self.xv = self.c * 10
        self.yv = self.s *10

    def move(self):
        self.x += self.xv
        self.y -= self.yv

    def draw(self, win):
        pygame.draw.rect(win, (255,255,255), [self.x, self.y, self.w, self.h])

    def checkOffScreen(self):
        if self.x < -50 or self.x > sw or self.y > sh or self.y < -50:
            return True
        
class Asteroid(object):
    def __init__(self, rank):
        self.rank = rank
        if self.rank == 1:
            self.image = asteroid50
        elif self.rank == 2:
            self.image = asteroid100
        elif self.rank == 3:
            self.image = asteroid150

        self.w = 50 * rank
        self.h = 50 * rank
        self.ranPoint = random.choice([random.randrange(0, sw-self.w), random.choice([-1 * self.h-5,sh+5]),(random.choice([-1*self.w-5, sw+5]), random.randrange(0, sh -self.h))])
        self.x, self.y = self.ranPoint
        if self.x < sw//2 :
            self.xdir = 1
        else:
            self.xdir = -1

        if self.y < sh//2:
            self.ydir = 1
        else:
            self.ydir = 1
        self.xv = self.xdir * random.randrange(1,3)
        self.yv = self.ydir * random.randrange(1,3)

    def draw(self, win):
        win.blit(self.image, ( self.x, self.y))

class Star(object):
    def __init__(self):
        self.img = Star
        self.w = self.img.get_width()
        self.h = self.img.get_height()
        self.ranPoint = random.choice([(random.randrange(0, sw-self.w), random.choice([-1*self.h-5, sh+5])),(random.choice([-1*self.w-5, sw+5]),random.randrange(0, sh-self.h))])
        self.x, self.y = self.ranPoint
        if self.x < sw //2:
            self.xdir = 1
        else:
            self.xdir = -1
        if self.y < sh//2:
            self.ydir = 1
        else:
            self.ydir = -1
