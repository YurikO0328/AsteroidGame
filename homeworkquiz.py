import pygame
import random
import sys
pygame.init()

sw = 1000
sh = 700

win = pygame.display.set_mode((sw,sh))
pygame.display.set_caption("Eco Quiz")
clock = pygame.time.Clock()

bgColor = (210,210,210)
white = (255,255,255)
black = (0,0,0)

dark1 = (20,20,20)
dark2 = (60,60,60)

score = 0
questionNum = 0
run = True

fontBig = pygame.font.SysFont("Arial",40)
fontMed = pygame.font.SysFont("Arial",28)
fontSmall = pygame.font.SysFont("Arial",26)

questions = [
    {"question":"Solar power is renewable.","answers":["True","False"],"correct":0},
    {"question":"Plastic bottles cannot be recycled.","answers":["True","False"],"correct":1},
    {"question":"Biking is eco friendly.","answers":["True","False"],"correct":0},
    {"question":"Carbon dioxide harms the planet.","answers":["True","False"],"correct":0},
    {"question":"Leaving lights on saves energy.","answers":["True","False"],"correct":1},
    {"question":"Trees help clean the air.","answers":["True","False"],"correct":0},
    {"question":"Ice caps are melting.","answers":["True","False"],"correct":0},
    {"question":"Compost is made from food waste.","answers":["True","False"],"correct":0},
    {"question":"Fixing leaks saves water.","answers":["True","False"],"correct":0},
    {"question":"Coal is renewable.","answers":["True","False"],"correct":1}]

boxes = [
    pygame.Rect(80,500,380,120),
    pygame.Rect(540,500,380,120)
]

boxColors = [dark1,dark2]

while run:
    clock.tick(60)

    win.fill(bgColor)

    scoreText = fontMed.render("Score: "+str(score),1,black)
    questionText = fontBig.render(questions[questionNum]["question"],1,black)

    win.blit(scoreText,(30,20))
    win.blit(questionText,(sw//2-questionText.get_width()//2,220))

    for i in range(2):
        pygame.draw.rect(win,boxColors[i],boxes[i],border_radius=20)

        answerText = fontSmall.render(questions[questionNum]["answers"][i],1,white)

        win.blit(answerText,(boxes[i].x+boxes[i].width//2-answerText.get_width()//2,boxes[i].y+boxes[i].height//2-answerText.get_height()//2))

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            mousePos = pygame.mouse.get_pos()

            for i in range(2):

                if boxes[i].collidepoint(mousePos):

                    if i == questions[questionNum]["correct"]:
                        score += 100
                        questionNum += 1

                        if questionNum >= len(questions):
                            win.fill(bgColor)

                            winText = fontBig.render("YOU WON! FINAL SCORE: "+str(score),1,black)

                            win.blit(winText,(sw//2-winText.get_width()//2,sh//2-winText.get_height()//2))

                            pygame.display.update()
                            pygame.time.delay(4000)

                            pygame.quit()
                            sys.exit()

                    else:
                        pygame.quit()
                        sys.exit()

    pygame.display.update()

pygame.quit()