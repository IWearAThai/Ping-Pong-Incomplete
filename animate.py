import pygame
import sys
import time
import random
from pygame.locals import *
from playsound import playsound



pygame.init()
pygame.mixer.init()


moveLeft = False
moveRight = False
moveDown = False
moveUp = False

playerScore = 0
computerScore = 0

WINDOWWIDTH = 800
WINDOWHEIGHT = 400

ws = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), 0, 32)

pygame.display.set_caption('PONG')

DOWNLEFT = 'downleft'
DOWNRIGHT = 'downright'
UPLEFT = 'upleft'
UPRIGHT = 'upright'

randomDirection = [DOWNLEFT, DOWNRIGHT, UPLEFT, UPRIGHT]

MOVESPEED = 4

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# b1 = {'rect': pygame.Rect(300, 80, 50, 100), 'color': RED, 'dir': UPRIGHT}
b2 = {'rect': pygame.Rect(400, 200, 20, 20), 'color': GREEN, 'dir': random.choice(randomDirection)}
# b3 = {'rect': pygame.Rect(100, 150, 60, 60), 'color': BLUE, 'dir': DOWNLEFT}

playerPaddleRight = pygame.Rect(750, 150, 20, 100)
playerPaddleTop = pygame.Rect(550, 25, 100, 20)
playerPaddleBottom = pygame.Rect(550, 350, 100, 20)
middleLine = pygame.Rect(400, 0, 10, 400)
computerPaddleLeft = pygame.Rect(50, 150, 20, 100)
computerPaddleTop = pygame.Rect(200, 25, 100, 20)
computerPaddleBottom = pygame.Rect(200, 350, 100, 20 )

boxes = [b2]

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_LEFT:
                moveRight = False
                moveLeft = True
            if event.key == K_RIGHT:
                moveRight = True
                moveLeft = False
            if event.key == K_UP:
                moveUp = True
                moveDown = False
            if event.key == K_DOWN:
                moveDown = True
                moveUp = False
        if event.type == KEYUP:
            if event.key == K_LEFT:
                moveLeft = False
            if event.key == K_RIGHT:
                moveRight = False
            if event.key == K_UP:
                moveUp = False
            if event.key == K_DOWN:
                moveDown = False

    ws.fill(WHITE)

    for b in boxes:
        if b['dir'] == DOWNLEFT:
            b['rect'].left -= MOVESPEED
            b['rect'].top += MOVESPEED
        if b['dir'] == DOWNRIGHT:
            b['rect'].left += MOVESPEED
            b['rect'].top += MOVESPEED
        if b['dir'] == UPLEFT:
            b['rect'].left -= MOVESPEED
            b['rect'].top -= MOVESPEED
        if b['dir'] == UPRIGHT:
            b['rect'].left += MOVESPEED
            b['rect'].top -= MOVESPEED

        if moveDown and playerPaddleRight.bottom < WINDOWWIDTH:
            playerPaddleRight.top += MOVESPEED
        if moveUp and playerPaddleRight.top > 0:
            playerPaddleRight.top -= MOVESPEED
        if moveRight:
            playerPaddleBottom.right += MOVESPEED
            playerPaddleTop.right += MOVESPEED
        if moveLeft:
            playerPaddleBottom.left -= MOVESPEED
            playerPaddleTop.left -= MOVESPEED

        if b['rect'].top < 0 and b['rect'].left < 400:
            playerScore += 1
            b['rect'].center

        if b['rect'].top < 0 and b['rect'].right > 400:
            computerScore += 1
            b['rect'].center

        if b['rect'].bottom > WINDOWHEIGHT and b['rect'].left < 400:
            playerScore += 1
            b['rect'].center

        if b['rect'].bottom > WINDOWHEIGHT and b['rect'].right > 400:
            computerScore += 1
            b['rect'].center

        if b['rect'].left < 0:
            playerScore += 1
            b['rect'].center

        if b['rect'].right > WINDOWWIDTH:
            computerScore += 1
            b['rect'].center

        if playerPaddleBottom.colliderect(b['rect']):
            if b['dir'] == DOWNRIGHT:
                b['dir'] = UPRIGHT
            if b['dir'] == DOWNLEFT:
                b['dir'] = UPLEFT
            playsound('pingpong.wav')

        if playerPaddleTop.colliderect(b['rect']):
            if b['dir'] == UPLEFT:
                b['dir'] = DOWNLEFT
            if b['dir'] == UPRIGHT:
                b['dir'] = DOWNRIGHT
            playsound('pingpong.wav')

        if playerPaddleRight.colliderect(b['rect']):
            if b['dir'] == DOWNRIGHT:
                b['dir'] = DOWNLEFT
            if b['dir'] == UPRIGHT:
                b['dir'] = UPLEFT
            playsound('pingpong.wav')

        if computerPaddleTop.colliderect(b['rect']):
            if b['dir'] == UPLEFT:
                b['dir'] = DOWNLEFT
            if b['dir'] == UPRIGHT:
                b['dir'] = DOWNRIGHT
            playsound('pingpong.wav')

        if computerPaddleBottom.colliderect(b['rect']):
            if b['dir'] == DOWNRIGHT:
                b['dir'] = UPRIGHT
            if b['dir'] == DOWNLEFT:
                b['dir'] = UPLEFT
            playsound('pingpong.wav')

        if computerPaddleLeft.colliderect(b['rect']):
            if b['dir'] == DOWNLEFT:
                b['dir'] = DOWNRIGHT
            if b['dir'] == UPLEFT:
                b['dir'] = UPRIGHT
            playsound('pingpong.wav')

        pygame.draw.rect(ws, b['color'], b['rect'])
        pygame.draw.rect(ws, RED, playerPaddleRight)
        pygame.draw.rect(ws, RED, playerPaddleBottom)
        pygame.draw.rect(ws, RED, playerPaddleTop)
        pygame.draw.rect(ws, BLACK, middleLine)
        pygame.draw.rect(ws, BLUE, computerPaddleLeft)
        pygame.draw.rect(ws, BLUE, computerPaddleBottom)
        pygame.draw.rect(ws, BLUE, computerPaddleTop)

    pygame.display.update()
    time.sleep(0.02)