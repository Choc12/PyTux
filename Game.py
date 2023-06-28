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