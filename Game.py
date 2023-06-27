import pygame
import sys
print("Loading PyTux...")
print("You are in Level 1: Tuxtorial.")
pygame.init()
screen = pygame.display.set_mode((1280, 720), pygame.RESIZABLE)
pygame.display.set_caption("PyTux")
pygame.display.flip()
pygame.display.update()
pygame.display.set_icon(pygame.image.load("images/icon.png"))
pygame.mixer.music.load("sounds/chipdisko.ogg")
pygame.mixer.music.play(-1)
setclock = pygame.time.Clock()
FPS = 60
color = (173, 216, 230)
screen.fill(color)
levelformat = open("levels/level1.lvl", "r")
level = levelformat.read()
format = level.split("\n")
for i in range(len(format)):
    for j in range(len(format[i])):
        if format[i][j] == "X":
            pygame.draw.rect(screen, (255, 255, 255), (j * 32, i * 32, 32, 32))
            tile = pygame.draw.rect(screen, (0, 0, 0), (j * 32, i * 32, 32, 32), 1)
pygame.draw.rect(screen, (0, 0, 0), (250, 200, 150, 50))


player = pygame.sprite.Sprite()
player.image = pygame.image.load("images/tux.png")
player.rect = player.image.get_rect()
player.rect.x = 0
player.rect.y = 0

screen.blit(player.image, player.rect)

pygame.KEYUP

pygame.display.update()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    setclock.tick(FPS)
    pygame.display.update()