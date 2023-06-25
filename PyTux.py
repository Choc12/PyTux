# import pygame
import pygame

print("Welcome to PyTux!")

pygame.init(), pygame.display.set_mode((640, 480)), pygame.display.set_caption("PyTux")
pygame.display.flip()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False