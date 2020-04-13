import pygame
import sys
from pygame.locals import *

RED = (255, 0, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

leftBatPos = 200
leftBatVel = 0

rightBatPos = 200
rightBatVel = 0

ballx = 320
bally = 240
ballvx = 3
ballvy = 3

FPS = 30
fpsClock = pygame.time.Clock()

score = [0, 0]

pygame.init()
SCREEN = pygame.display.set_mode((640, 480))
pygame.display.set_caption('PingPong')

font = pygame.font.SysFont("comicsansms", 60)
font.set_italic(True)

# Game Loop
while True:

    SCREEN.fill(WHITE)

    pygame.draw.circle(SCREEN, BLACK, (int(ballx), int(bally)), 10)

    pygame.draw.rect(SCREEN, RED, (0, leftBatPos, 20, 80))

    pygame.draw.rect(SCREEN, RED, (620, rightBatPos, 20, 80))

    leftScore = font.render(str(score[0]), True, RED)
    rightScore = font.render(str(score[1]), True, RED)
    leftScoreRect = leftScore.get_rect()
    rightScoreRect = rightScore.get_rect()
    leftScoreRect.center = (40, 40)
    rightScoreRect.center = (600, 40)

    SCREEN.blit(leftScore, leftScoreRect)
    SCREEN.blit(rightScore, rightScoreRect)

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_w:
                leftBatVel = -5
            elif event.key == K_s:
                leftBatVel = 5
            elif event.key == K_u:
                rightBatVel = -5
            elif event.key == K_j:
                rightBatVel = 5
        if event.type == KEYUP:
            if event.key == K_w or event.key == K_s:
                leftBatVel = 0
            elif event.key == K_u or event.key == K_j:
                rightBatVel = 0

    if leftBatPos >= 0 and leftBatVel < 0:
        leftBatPos += leftBatVel
    elif leftBatPos <= 400 and leftBatVel > 0:
        leftBatPos += leftBatVel

    if rightBatPos >= 0 and rightBatVel < 0:
        rightBatPos += rightBatVel
    elif rightBatPos <= 400 and rightBatVel > 0:
        rightBatPos += rightBatVel

    if bally < 10 or bally > 470:
        ballvy *= -1

    ballx += ballvx
    bally += ballvy

    if ballx < 30:
        if pygame.Rect(0, leftBatPos, 20, 80).colliderect((ballx-10, bally+10, 20, 20)):
            ballvx *= -1.1
            ballvy *= 1.1
        elif ballvx < 0:
            score[1] += 1
            ballx = 320
            bally = 240
            ballvx = 3
            ballvy = 3
    if ballx > 610:
        if pygame.Rect(620, rightBatPos, 20, 80).colliderect((ballx-10, bally+10, 20, 20)):
            ballvx *= -1.1
            ballvy *= 1.1
        elif ballvx > 0:
            score[0] += 1
            ballx = 320
            bally = 240
            ballvx = 3
            ballvy = 3

    pygame.display.update()

    fpsClock.tick(FPS)
