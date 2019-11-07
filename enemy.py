import pygame
pygame.init()

hitSound = pygame.mixer.Sound("music/hit.wav")
class enemy():




    def __init__(self, x, y, width, height, end,level):
        self.level = level
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.end = end
        self.path = [self.x, self.end]
        self.walkCount = 0
        self.vel = 4*self.level
        self.hitbox = (self.x + 17, self.y+2, 31,57)
        self.health = 10
        self.visible = True
        self.walkRight = [pygame.image.load('images/enemy/{}/R%sE.png'.format(self.level) % frame) for frame in range(1, 12)]
        for i in range(len(self.walkRight)):
            self.walkRight[i] = pygame.transform.scale(self.walkRight[i],(64,64))

        #self.walkLeft = [pygame.image.load('images/enemy/{}/L%sE.png'.format(self.level) % frame) for frame in range(1, 12)]

    def draw(self, win):
        self.move()
        if self.visible:
            if self.walkCount + 1 >= 18:
                self.walkCount = 0
            if self.vel > 0:
                #win.blit(zombieWalkRight[self.walkCount//3],(self.x,self.y))
                win.blit(self.walkRight[self.walkCount // 3], (self.x, self.y))
                self.walkCount += 1
            else:
                win.blit(pygame.transform.flip(self.walkRight[self.walkCount // 3],True,False), (self.x, self.y))
                #win.blit(self.walkLeft[self.walkCount // 3], (self.x, self.y))
                self.walkCount += 1
            pygame.draw.rect(win, (255, 0, 0), (self.hitbox[0], self.hitbox[1] - 20, 50, 10))
            pygame.draw.rect(win, (0,128,0), (self.hitbox[0],self.hitbox[1] - 20,50 - (5*(10-self.health)),10))
            self.hitbox = (self.x + 17, self.y + 2, 31, 57)

    def move(self):
        if self.vel > 0:
            if self.x + self.vel < self.path[1]:
                self.x += self.vel
            else:
                self.vel *= -1
                self.walkCount = 0
        else:
            if self.x + self.vel >= self.path[0]:

                self.x += self.vel

            else:
                self.vel *= -1
                self.walkCount = 0

        #pygame.draw.rect(win,(255,0,0),self.hitbox,2)
    def hit(self):
        hitSound.play()
        if self.health > 1:
            self.health -= 1
        else:
            self.visible = False
