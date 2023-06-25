# import pygame
import pygame
import sys

print("Welcome to PyTux!")
print("PyTux is a Pygame-based game for Linux.")
pygame.init(), pygame.display.set_mode((640, 480), pygame.RESIZABLE), pygame.display.set_caption("PyTux")
pygame.display.flip(), pygame.display.update(), pygame.display.set_icon(pygame.image.load("images/icon.png"))
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
pygame.quit()