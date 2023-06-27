# import pygame
import pygame
# import pygame_widgets
import pygame_widgets
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
screen = pygame.display.set_mode((640, 480), pygame.RESIZABLE)
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
# set the PyTux text
text("Welcome to PyTux!", 225, 10, (0, 0, 0), 30)

# button to start the game
startbutton = pygame.draw.rect(screen, (0, 0, 0), (250, 200, 150, 50))
text("Start", 300, 210, (255, 255, 255), 30)
# when the start button is pressed
whenstartbutton = pygame.mouse.get_pressed()
if whenstartbutton[0]:
    # play the game
    whenstartbutton = False
    print("Playing the game...")
    # quit PyTux
    pygame.quit()
    # run the game
    exec(open("game.py").read())
# button to quit PyTux
quitbutton = pygame.draw.rect(screen, (0, 0, 0), (250, 300, 150, 50))
text("Quit", 300, 310, (255, 255, 255), 30)
# when the quit button is pressed
whenquitbutton = pygame.mouse.get_pressed()
if whenquitbutton[0]:
    # quit PyTux
    whenquitbutton = True
    print("Quitting PyTux...")
    pygame.quit()
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





# pygame.mixer.init()
maintheme = pygame.mixer.Sound("sounds/maintheme.ogg")
# play the main theme
maintheme.play()

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