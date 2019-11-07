import os
import pygame


from playAgain import *
Y = 275
pygame.init()
walkRight = [pygame.image.load(os.path.join("images", "R%s.png") % frame) for frame in range (1,10)]
walkLeft = [pygame.image.load('images/L%s.png' % frame) for frame in range(1,10)]
class player(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 5
        self.isJump = False
        self.jumpCount = 10
        self.left = False
        self.right = False
        self.walkCount = 0
        self.standing = True
        self.hitbox = (self.x+17,self.y+5, 29, 58)
    def hit(self,win):
        self.isJump = False
        self.jumpCount = 10
        self.x = 60
        self.y = 275
        self.walkCount = 0
        font1 = pygame.font.SysFont('comicsans',100)
        text = font1.render('-5',1,(255,0,0))
        win.blit(text,(250-(text.get_width()/2),200))
        pygame.display.update()
        i = 0
        while i < 100:
            pygame.time.delay(10)
            i+=1
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    i = 301
                    pygame.quit()

    def won(self,win):
        font1 = pygame.font.SysFont('comicsans', 50)
        text = font1.render('You won,Congatulations!', 1, (255, 0, 0))
        win.blit(text, (250 - (text.get_width() / 4), 200))
        pygame.display.update()

        go = True
        while go:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:

                    pygame.quit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        return True
    def loose(self,win):
        font1 = pygame.font.SysFont('comicsans', 50)
        text = font1.render('Unfortunately,you`ve lost!', 1, (255, 0, 0))
        win.blit(text, (250 - (text.get_width() / 4), 200))
        pygame.display.update()
        go = True
        while go:
            pygame.time.delay(100)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    go = False
                    pygame.quit()

                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        return True








    def draw(self, win):
        if self.walkCount + 1 >= 27:
            self.walkCount = 0
        if not self.standing:
            if self.left:
                win.blit(walkLeft[self.walkCount // 3], (self.x, self.y))
                self.walkCount += 1
            elif self.right:
                win.blit(walkRight[self.walkCount // 3], (self.x, self.y))
                self.walkCount += 1
        else:
            if self.right:
                win.blit(walkRight[0], (self.x, self.y))
            else:
                win.blit(walkLeft[0], (self.x, self.y))
        self.hitbox = (self.x + 17, self.y + 5, 29, 58)
        #pygame.draw.rect(win,(255,0,0),self.hitbox,1)