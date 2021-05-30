# importing packages
import pygame

# initializing pygame
pygame.init()
# makeing a window
screen = pygame.display.set_mode((700, 500))
pygame.display.set_caption("Naruto ninja Battles")

# creating arrays of walking images
naruto_right = [pygame.image.load('assets\\run1.png'), pygame.image.load('assets\\run2.png'),
                pygame.image.load('assets\\run3.png'), pygame.image.load('assets\\run4.png')]
naruto_left = [pygame.image.load('assets\\l1.png'), pygame.image.load('assets\\l2.png'),
               pygame.image.load('assets\\l3.png'), pygame.image.load('assets\\l4.png')]

Mh = pygame.image.load('assets\\mhealth.png')
Nh = pygame.image.load('assets\\nhealth.png')
nh = pygame.transform.scale(Nh, (80, 80))
mh = pygame.transform.scale(Mh, (80, 80))
nd = pygame.transform.scale(pygame.image.load('assets\\nd.png'), (75, 45))

hit = pygame.mixer.Sound("assets\\hit.wav")
theme = pygame.mixer.music.load("assets\\theme.wav")

pygame.mixer.music.play()
# creating a clock
clock = pygame.time.Clock()


# creating a class player to use for players
class player():
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 9
        self.left = False
        self.right = False
        self.walkcount = 0
        self.jump = False
        self.jumpcount = 10
        self.stand = True
        self.hitbox = (self.x + 10, self.y + 5, 80, 80)
        self.health = 200

    # draw function to add all the animations and feature of player
    def draw(self, screen):
        if self.health > 0:
            if self.walkcount + 1 >= 12:
                self.walkcount = 0

            if not (self.stand):
                self.hitbox = (self.x, self.y + 5, 65, 70)
                if self.left:
                    screen.blit(naruto_left[self.walkcount // 4], (self.x, self.y + 8))
                    self.walkcount += 1
                elif self.right:
                    screen.blit(naruto_right[self.walkcount // 4], (self.x, self.y + 8))
                    self.walkcount += 1
            else:
                if self.right:
                    screen.blit(pygame.image.load('assets\\standing right.png'), (self.x, self.y))
                else:
                    screen.blit(pygame.image.load('assets\\standing left.png'), (self.x, self.y))
                self.hitbox = (self.x, self.y + 5, 37, 70)
            nabar_bg = pygame.draw.rect(screen, (0, 25, 255), (70, 40, 220, 30))
            nbar2 = pygame.draw.rect(screen, (255, 0, 0), (80, 45, 200, 20))
            nabar = pygame.draw.rect(screen, (25, 255, 0), (80, 45, self.health, 20))
        else:
            if over:
                text = font.render('Madara wins.Click r to replay', True, (0, 30, 255), (0, 0, 100))
                screen.blit(text, (100, 200))
                screen.blit(nd, (self.x, self.y + 40))
            else:
                self.vel = 9
                nabar_bg = pygame.draw.rect(screen, (0, 25, 255), (70, 40, 220, 30))
                nbar2 = pygame.draw.rect(screen, (255, 0, 0), (80, 45, 200, 20))
                nabar = pygame.draw.rect(screen, (25, 255, 0), (80, 45, self.health, 20))

        # pygame.draw.rect(screen,(0,0,255),self.hitbox,2)

    def hit(self):
        if self.health > 0:
            self.health -= 5
            print('Naruto:' + str(self.health))
        else:
            print("naruto died")


class Shuriken():
    def __init__(self, x, y, width, height, facing):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.facing = facing
        self.vel = 8 * facing

    def draw(self, screen):
        screen.blit(pygame.image.load('assets\\shuriken.png'), (self.x, self.y))
        self.hitbox = (self.x, self.y, 40, 40)
        # pygame.draw.rect(screen,(0,0,255),self.hitbox,2)


class enemy():
    madara_right = [pygame.image.load('assets\\mr1.png'), pygame.image.load('assets\\mr2.png'),
                    pygame.image.load('assets\\mr3.png'), pygame.image.load('assets\\mr4.png')]
    madara_left = [pygame.image.load('assets\\ml1.png'), pygame.image.load('assets\\ml2.png'),
                   pygame.image.load('assets\\ml3.png'), pygame.image.load('assets\\ml4.png')]

    def __init__(self, x, y, width, height, start, end):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.end = end
        self.start = start
        self.path = [self.start, self.end]
        self.speed = 12
        self.walkcount = 0
        self.hitbox = (self.x, self.y, 60, 65)
        self.health = 200

    def draw(self, screen):
        if self.health > 0:
            self.move()
            if self.walkcount + 1 >= 12:
                self.walkcount = 0
            if self.speed > 0:
                screen.blit(self.madara_right[self.walkcount // 4], (self.x, self.y))
                self.walkcount += 1
            else:
                screen.blit(self.madara_left[self.walkcount // 4], (self.x, self.y))
                self.walkcount += 1
            self.hitbox = (self.x, self.y, 60, 65)
            mbar_bg = pygame.draw.rect(screen, (0, 25, 255), (400, 40, 220, 30))
            mbar2 = pygame.draw.rect(screen, (255, 0, 0), (410, 45, 200, 20))
            mabar = pygame.draw.rect(screen, (25, 255, 0), (410, 45, self.health, 20))
        else:
            if over:
                self.speed = 0
                text = font.render('Naruto wins. Click R to replay', True, (0, 30, 255), (0, 0, 100))
                screen.blit(text, (100, 200))
                screen.blit(pygame.image.load('assets\\md4.png'), (self.x, self.y + 20))
        # pygame.draw.rect(screen,(0,0,255),self.hitbox,2)

    def move(self):
        if self.speed > 0:
            if self.x + self.speed < self.end:
                self.x += self.speed
            else:
                self.speed = self.speed * -1
                self.walkcount = 0

        else:
            if self.x - self.speed > self.path[0]:
                self.x += self.speed
            else:
                self.speed = self.speed * -1
                self.walkcount = 0

    def hit(self):
        if self.health > 0:
            self.health -= 10
            print('madara:' + str(self.health))
        else:
            print("madara died")


run = True


# drawing the window design
def redraw_window():
    screen.fill((153, 217, 234))
    screen.fill((51, 189, 13), rect=[0, 500 - 40, 700, 40])
    screen.fill((128, 94, 0), rect=[0, 500 - 25, 700, 25])
    screen.blit(pygame.image.load('assets\\bg.png'), (0, 0))
    naruto.draw(screen)
    madara.draw(screen)
    screen.blit(nh, (10, 10))
    screen.blit(mh, (595, 10))
    for shuriken in shurikens:
        shuriken.draw(screen)
    pygame.display.update()


font = pygame.font.SysFont('comicsans', 50, True)

# player Naruto
naruto = player(50, 385, 50, 46)
madara = enemy(300, 393, 70, 100, 30, 690)
over = False
shurikens = []
throwspeed = 0
# game loop
while run:
    # framerate
    clock.tick(40)

    if throwspeed > 0:
        throwspeed += 1

    if throwspeed > 3:
        throwspeed = 0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    if naruto.health > 0 and madara.health > 0:
        if naruto.hitbox[1] < madara.hitbox[1] + madara.hitbox[3] and naruto.hitbox[1] + naruto.hitbox[3] > \
                madara.hitbox[1]:
            if naruto.hitbox[0] + naruto.hitbox[2] > madara.hitbox[0] and naruto.hitbox[0] < madara.hitbox[0] + \
                    madara.hitbox[2]:
                naruto.hit()
                hit.play()
    else:
        if naruto.health == 0:
            if not over:
                naruto.vel = 0
                over = True

    for shuriken in shurikens:
        if madara.health > 0:
            if shuriken.hitbox[1] + round(shuriken.hitbox[3] / 2) > madara.hitbox[1] and shuriken.hitbox[1] + round(
                    shuriken.hitbox[3] / 2) < madara.hitbox[1] + madara.hitbox[3]:
                if shuriken.hitbox[0] + shuriken.hitbox[2] > madara.hitbox[0] and shuriken.hitbox[0] + shuriken.hitbox[
                    2] < madara.hitbox[0] + madara.hitbox[2]:
                    madara.hit()
                    hit.play()
                    shurikens.pop(shurikens.index(shuriken))
        else:
            if not over:
                madara.speed = 0
                over = True

        if shuriken.x < 700 and shuriken.x > 0:
            shuriken.x += shuriken.vel
        else:
            shurikens.pop(shurikens.index(shuriken))

    keys = pygame.key.get_pressed()

    if keys[pygame.K_SPACE] and throwspeed == 0:
        if naruto.left:
            facing = -1
        else:
            facing = 1

        if len(shurikens) < 5:
            shurikens.append(
                Shuriken(round(naruto.x + naruto.width // 2), (naruto.y + naruto.height // 2), 40, 40, facing))
        throwspeed = 1

    if keys[pygame.K_LEFT] and naruto.x > naruto.vel:
        naruto.x -= naruto.vel
        naruto.stand = False
        naruto.right = False
        naruto.left = True
    elif keys[pygame.K_RIGHT] and naruto.x < 700 - naruto.width - naruto.vel:
        naruto.x += naruto.vel
        naruto.stand = False
        naruto.left = False
        naruto.right = True
    else:
        naruto.stand = True
        naruto.walkcount = 0
    if not naruto.jump:
        if keys[pygame.K_UP]:
            naruto.jump = True
    else:
        if naruto.jumpcount >= -10:
            neg = 1
            if naruto.jumpcount < 0:
                neg = -1
            naruto.y -= (naruto.jumpcount ** 2) * 0.5 * neg
            naruto.jumpcount -= 1
        else:
            naruto.jump = False
            naruto.jumpcount = 10
    if keys[pygame.K_r]:
        naruto.health = 200
        madara.health = 200
        naruto.vel = 9
        madara.speed = 8

    redraw_window()
