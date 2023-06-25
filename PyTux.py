# import pygame
import pygame
# import sys
import sys

# print the PyTux info
print("Welcome to PyTux!")
print("PyTux is a Pygame-based game for Linux.")
print("PyTux is a game about Tux, the Linux mascot, and his adventures.")
print("PyTux is currently in development.")
print("PyTux is currently in version 0.0.0.")
print("PyTux is licensed under the GNU GPL v3.")
print("PyTux is made by the PyTux Team.(currently only Choc12.)")
print("PyTux is made in Python 3.10.6.")
print("PyTux is made in Pygame 2.5.2.")
print("PyTux is made in Pop!_OS 22.04.")

# pygame.init()
pygame.init(), pygame.display.set_mode((640, 480), pygame.RESIZABLE), pygame.display.set_caption("PyTux")
pygame.display.flip(), pygame.display.update(), pygame.display.set_icon(pygame.image.load("images/icon.png"))

# pygame.mixer.init()
maintheme = pygame.mixer.Sound("sounds/maintheme.ogg")
maintheme.play()

# main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
# quit PyTux
pygame.quit()