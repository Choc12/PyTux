import pygame
import sys
pygame.init()
screen = pygame.display.set_mode((640, 480), pygame.RESIZABLE)
pygame.display.set_caption("PyTux")
pygame.display.flip()
pygame.display.update()
pygame.display.set_icon(pygame.image.load("images/icon.png"))
setclock = pygame.time.Clock()
FPS = 60
color = (173, 216, 230)
screen.fill(color)
TILESIZEX = 32
TILESIZEY = 32