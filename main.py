import os
import random
import pygame
import time

class Player(object):
    def __init__(self):
        self.rect = pygame.Rect(32, 32, 16, 16)

    def move(self, dx, dy):
        if dx != 0:
            self.move_single_axis(dx, 0)
        if dy != 0:
            self.move_single_axis(0, dy)

    def move_single_axis(self, dx, dy):
        self.rect.x += dx
        self.rect.y += dy
        for wall in walls:
            if self.rect.colliderect(wall.rect):
                if dx > 0:
                    self.rect.right = wall.rect.left
                if dx < 0:
                    self.rect.left = wall.rect.right
                if dy > 0:
                    self.rect.bottom = wall.rect.top
                if dy < 0:
                    self.rect.top = wall.rect.bottom

class Wall(object):
    def __init__(self, pos):
        walls.append(self)
        self.rect = pygame.Rect(pos[0], pos[1], 16, 16)



#######################################################
os.environ["SDL_VIDEO_CENTERED"] = "1"
pygame.init()

font = pygame.font.SysFont("comicsansms", 20)
win_txt = font.render("We have a Winner!", True, (128,128,128))
pygame.display.set_caption("[HnS Game]")
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
walls = []
player = Player()


level = [
"WWWWWWWWWWWWWWWWWWWWWWWWWW",
"W   E                    W",
"W         WWWWWWWW     W W",
"W   WWWWWW       W       W",
"W   W        WWWW        W",
"W WWW  WWWW              W",
"W   W     W W            W",
"W   W     W   WWW WWWWWWWW",
"W   WWW WWW   W W  WWWWWWW",
"W     W   W   W W  WWWWWWW",
"WWW   W   WWWWW W  WWWWWWW",
"W W      WW        WWWWWWW",
"W W   WWWW   WWW   WWWWWWW",
"W     W        W   WWWWWWW",
"WWWWWWWWWWWWWWWWWWWWWWWWWW",
]

x = y = 0
for row in level:
    for col in row:
        if col == "W":
            Wall((x, y))
        if col == "E":
            end_rect = pygame.Rect(x, y, 16, 16)
        x += 16
    y += 16
    x = 0

running = True
while running:
    clock.tick(60)

    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False
        if e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE:
            running = False

    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT]:
        player.move(-2, 0)
    if key[pygame.K_RIGHT]:
        player.move(2, 0)
    if key[pygame.K_UP]:
        player.move(0, -2)
    if key[pygame.K_DOWN]:
        player.move(0, 2)

    if player.rect.colliderect(end_rect):
        screen.blit(win_txt, (500,10))
        pygame.display.update()
        time.sleep(2)
        running = False

    screen.fill((0, 0, 0))
    for wall in walls:
        pygame.draw.rect(screen, (128,128,128), wall.rect)

    pygame.draw.rect(screen, (255, 0, 0), end_rect)
    pygame.draw.rect(screen, (0,128,0), player.rect)

    pygame.display.flip()
