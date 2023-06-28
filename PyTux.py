# by Choc12

## GPLv3
# This program is free software: you can redistribute it and/or
# modify it under the terms of the GNU General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

# import pygame
import pygame
# import pygame_widgets
import pygame_widgets
from pygame_widgets.button import Button
# import sys
import sys

# print the PyTux info
print("Welcome to PyTux!")
print("PyTux is a Pygame-based game for Linux, Windows And MacOS.")
print("PyTux is a game about Tux, the Linux mascot, and his adventures.")
print("PyTux is currently in development.")
print("PyTux is currently in version 0.0.0.")
print("PyTux is licensed under the GNU GPL v3.")
print("PyTux is made by the PyTux Team.(currently only Choc12.)")
print("PyTux is made in Python 3.11.4.")
print("PyTux is made in Pygame 2.5.0.")
print("PyTux is made in Visual Studio Code 1.79.2.")
print("PyTux is made in Windows 10.")

# pygame.init()
pygame.init()
# set the PyTux window
screen = pygame.display.set_mode((1280, 720), pygame.RESIZABLE)
# set the PyTux window title
pygame.display.set_caption("PyTux")
pygame.display.flip() 
# update the PyTux window
pygame.display.update()
# set the PyTux window icon
pygame.display.set_icon(pygame.image.load("images/icon.png"))
# set the clock
setclock = pygame.time.Clock()

# set the PyTux FPS
FPS = 60
# set the PyTux background
color = (173, 216, 230)
screen.fill(color)
# set the PyTux text
textcolor = (0, 0, 0)
def text(text, x, y, textcolor, size):
    font = pygame.font.SysFont("Arial", size)
    text = font.render(text, True, textcolor)
    screen.blit(text, (x, y))
# show the PyTux Logo
logo = pygame.image.load("images/logo.png")
screen.blit(logo, (500, 100))
# set the PyTux text
text("Welcome to PyTux!", 500, 10, (0, 0, 0), 30)
# button to start the game
button = Button(
    screen, 250, 200, 150, 50, text='Start', fontSize=30,
    margin=20,
    inactiveColour=(0, 0, 0),
    pressedColour=(255, 0, 0),
    radius=20,
    onClick=lambda: print('Click')
)
# when the start button is pressed
whenbutton = pygame.mouse.get_pressed()
if whenbutton[0]:
    # start the game
    whenbutton = True
    print("Starting PyTux...")
    exec(open("level1.py").read())
# press enter to start the game
whenenter = pygame.key.get_pressed()
if whenenter[pygame.K_RETURN]:
    # start the game
    whenenter = False
    print("Starting PyTux...")
    exec(open("level1.py").read())
# button to quit PyTux
quitbutton = Button(
    screen, 250, 300, 150, 50, text='Quit', fontSize=30,
    margin=20,
    inactiveColour=(0, 0, 0),
    pressedColour=(255, 0, 0),
    radius=20,
    onClick=lambda: print('Click')
)
# when the quit button is pressed
whenquitbutton = pygame.mouse.get_pressed()
if whenquitbutton[0]:
    # quit PyTux
    whenquitbutton = False
    print("Quitting PyTux...")
    sys.exit()
# button to go view the credits
creditsbutton = pygame.draw.rect(screen, (0, 0, 0), (250, 400, 150, 50))
text("Credits", 300, 410, (255, 255, 255), 30)
# when the credits button is pressed
whencreditsbutton = pygame.mouse.get_pressed()
if whencreditsbutton[0]:
    # open Credits file
    whencreditsbutton = False
    print("Opening Credits file...")
    exec(open("Credits").read())
# button to go view the license
licensebutton = pygame.draw.rect(screen, (0, 0, 0), (250, 500, 150, 50))
text("License", 300, 510, (255, 255, 255), 30)
# when the license button is pressed
whenlicensebutton = pygame.mouse.get_pressed()
if whenlicensebutton[0]:
    # open License file
    whenlicensebutton = False
    print("Opening License file...")
    exec(open("Copying").read())





# pygame.mixer.init()
maintheme = pygame.mixer.Sound("sounds/maintheme.ogg")
# play the main theme
maintheme.play(loops=-1)
# loop the main theme

pygame.display.update()
# main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
# quit PyTux
pygame.quit()
print("Quitting PyTux...")