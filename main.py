from random import randint

import pygame
import os
from playAgain import *
from player import *
from enemy import *
MAX_LVL = 2
pygame.init()
BULLET_WIDTH = 15
BULLET_HEIGHT = 7
WIDTH = 719
HEIGHT = 404

music = pygame.mixer.music.load("music/music.mp3")
bulletSound = pygame.mixer.Sound("music/bullet.wav")
#MUSIC WHILE GAME IS ON
#pygame.mixer.music.play(-1)
win = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

char = pygame.image.load(os.path.join("images", "standing.png"))
ammo = pygame.image.load('images/bullet2.png')






class projectile():
    def __init__(self, x, y, radius, color, facing):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.facing = facing
        self.vel = 8 * facing

    def draw(self, win):

        win.blit(ammo,(self.x,self.y))
       # pygame.draw.circle(win, self.color, (self.x, self.y), self.radius)


def redrawGameWindow(x,man,goblins,score,bullets,bg):
    font_score = pygame.font.SysFont('comicsans', 30, True)
    win.blit(bg, (x, 0))
    win.blit(bg,(WIDTH+x,0))
    text = font_score.render("Score: " + str(score),1,(255,0,0))
    win.blit(text,(390,10))
    man.draw(win)
    for goblin in goblins:
        goblin.draw(win)
    for bullet in bullets:
        bullet.draw(win)
    pygame.display.update()





def main():
    bg2 = pygame.image.load('images/bg/bg2.png')
    bg3 = pygame.image.load('images/bg/zombieBG.jpg')
    bg1 = pygame.image.load('images/bg/moving_bg.png')
    bg = bg1
    level = 1
    goblins = []
    score = 0
    shootLoop = 0

    def initGame(level):
        if level == 1:
            enemy_amount = 1
            p = randint(50,300)
            for i in range(enemy_amount):
                e = enemy(130+50*i,275,64,64,300+50*i,1)
                goblins.append(e)
       # g2 = enemy(130, 275, 64, 64, 450)
        if level == 2:


            enemy_amount = 1
            p = randint(50, 300)
            for i in range(enemy_amount):
                e = enemy(130 + 50 * i, 275, 64, 64, 300 + 50 * i, 2)
                goblins.append(e)


    man = player(0, 275, 64, 64)
    initGame(1)



    bullets = []
    run = True
    current_x = 0

    while run:
        for goblin in goblins:
            if goblin.visible:
                if man.hitbox[1] < goblin.hitbox[1]+goblin.hitbox[3] and man.hitbox[1] + man.hitbox[3] > goblin.hitbox[1]:
                    if man.hitbox[0] + man.hitbox[2] > goblin.hitbox[0] and man.hitbox[0] < goblin.hitbox[2]+goblin.hitbox[0]:

                        man.hit(win)
                        score -=5

            else:
                goblins.pop(goblins.index(goblin))


        if len(goblins) == 0 and level == MAX_LVL:

            bullets = []
            bg = bg2
            redrawGameWindow(current_x, man, goblins, score, bullets,bg)

            restart = man.won(win)
            if restart:
                score = 0
                shootLoop = 0
                player.x = 0
                bg = bg1

                initGame(1)
        elif len(goblins) == 0:
            level +=1
            bg = bg2
            redrawGameWindow(current_x, man, goblins, score, bullets,bg)
            initGame(level)





        clock.tick(27)
        if shootLoop > 0:
            shootLoop += 1
        if shootLoop > 3:
            shootLoop = 0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        for bullet in bullets:
            # bullet height = 7, bullet width = 15
            for goblin in goblins:
                #checking if bullet hits goblin
                if goblin.visible:
                    if bullet.y + BULLET_HEIGHT > goblin.hitbox[1] and bullet.y - BULLET_HEIGHT < goblin.hitbox[1] + goblin.hitbox[3]:
                        if bullet.x + BULLET_WIDTH > goblin.hitbox[0] and bullet.x - BULLET_WIDTH < goblin.hitbox[0]+goblin.hitbox[2]:

                            goblin.hit()
                            score +=1
                            if bullet in bullets:
                                bullets.pop(bullets.index(bullet))

            if bullet.x < WIDTH and bullet.x > 0:
                bullet.x += bullet.vel
            else:
                bullets.pop(bullets.index(bullet))

        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and shootLoop == 0:
            bulletSound.play()
            if man.left:
                facing = -1
            else:
                facing = 1
            if len(bullets) < 5:
                bullets.append(
                    projectile(round(man.x + man.width // 2), round(man.y + man.height // 2), 6, (0, 0, 0), facing))
            shootLoop = 1
        if keys[pygame.K_LEFT] and man.x - man.vel >= 0:
            man.x -= man.vel
            man.left = True
            man.right = False
            man.standing = False
        elif keys[pygame.K_RIGHT]:
            if man.x + man.vel + man.width < WIDTH:
                man.x += man.vel
                man.right = True
                man.left = False
                man.standing = False

        else:
            man.standing = True
            man.walkCount = 0
        if not man.isJump:
            if keys[pygame.K_UP]:
                man.isJump = True
                man.right = False
                man.left = False
                man.walkCount = 0
        else:
            if man.jumpCount >= - 10:
                neg = 1
                if man.jumpCount < 0:
                    neg = -1

                if man.y + man.height - (man.jumpCount ** 2) * 0.5 * neg < HEIGHT:
                    man.y -= (man.jumpCount ** 2) * 0.5 * neg
                    man.jumpCount -= 1
                else:
                    man.isJump = False
                    man.jumpCount = 10


            else:
                man.isJump = False
                man.jumpCount = 10
        if not man.standing:
            if current_x > -WIDTH:
                current_x -=1
            else:
                current_x = 0
        redrawGameWindow(current_x,man,goblins,score,bullets,bg)

    #play_again()
main()