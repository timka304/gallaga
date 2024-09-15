import pygame
import random
import pgzrun

WIDTH = 800
HEIGHT = 800

ship = Actor("ship")
ship.pos = (WIDTH/2, HEIGHT-100)

bug = Actor("bug")

speed = 5

bugs = []
bullets = []

for x in range(8):
    for y in range(4):
        bugs.append(Actor("bug"))
        bugs[-1].x = 100+50*x
        bugs[-1].y = 80+50*y


score = 0

direction = 1

ship.dead = False

ship.countdown = 90

def displayScore():
    screen.draw.text(str(score), (20,20))

def gameOver():
    screen.draw.text("Game Over", (WIDTH/2, HEIGHT/2))

def on_key_down(key):
    if ship.dead == False:
        if key == keys.SPACE:
            bullets.append(Actor("bullet"))
            bullets[-1].x = (ship.x)
            bullets[-1].y = (ship.y-30)

def update():
    global score, direction
    move_down = False
    #ship movement
    if ship.dead == False:
        if keyboard.left:
            ship.x -= speed
            if ship.x <= 0:
                ship.x = 0
        elif keyboard.right:
            ship.x += speed
            if ship.x >= WIDTH:
                ship.x = WIDTH
    #bullet shoot

    for bullet in bullets:
        if bullet.y <= 0:
            bullets.remove(bullet)

        else:
            bullet.y -= 10

    #position of the last bug
    if len(bugs) == 0:
        gameOver()

    if len(bugs) > 0 and (bugs[-1].x > WIDTH-80 or bugs[0].x < 80):
        move_down = True

        direction = direction*-1

    for bug in bugs:
        bug.x += 5*direction
        if move_down == True:
            bug.y += 80
        if bug.y > HEIGHT:
            bugs.remove(bug)

        for bullet in bullets:
            if bug.colliderect(bullet):
                score += 100
                bullets.remove(bullet)
                bugs.remove(bug)
            if len(bugs) == 0:
                    gameOver()

        if bug.colliderect(ship):
            ship.dead = True
    if ship.dead == True:
        ship.countdown -= 1
    if ship.countdown == 0:
        ship.dead = False
        ship.countdown = 90

def draw():
    screen.clear()
    screen.blit("nightsky", (0, 0))
    for bullet in bullets:
        bullet.draw()
    for bug in bugs:
        bug.draw()
    if ship.dead == False:
        ship.draw()
    displayScore()
    if len(bugs) == 0:
        gameOver()

pgzrun.go()