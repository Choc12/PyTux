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

import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("images/tux.png")
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0
        self.xvel = 0
        self.yvel = 0
        self.onGround = False
        self.jump = False
        self.jumpHeight = 10
        self.jumpCount = 0
        self.gravity = 0.5
        self.speed = 5
        self.jumpSound = pygame.mixer.Sound("sounds/jump.wav")
        self.jumpSound.set_volume(0.5)
        self.jumpSound.play()
        self.jumpSound.fadeout(1000)
        self.jumpSound.stop()
        screen.blit(self.image, self.rect)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.xvel = -self.speed
        if keys[pygame.K_RIGHT]:
            self.xvel = self.speed
        if keys[pygame.K_UP]:
            self.jump = True
        if keys[pygame.K_DOWN]:
            self.yvel = self.speed
        if not self.onGround:
            self.yvel += self.gravity
        self.rect.x += self.xvel
        self.rect.y += self.yvel
        if self.jump:
            if self.jumpCount < self.jumpHeight:
                self.yvel = -self.speed
                self.jumpCount += 1
            else:
                self.jump = False
                self.jumpCount = 0
        if self.rect.bottom > 720:
            self.rect.bottom = 720
            self.onGround = True
            self.yvel = 0
        if self.rect.top < 0:
            self.rect.top = 0
            self.yvel = 0
        if self.rect.left < 0:
            self.rect.left = 0
            self.xvel = 0
        if self.rect.right > 1280:
            self.rect.right = 1280
            self.xvel = 0
        screen.blit(self.image, self.rect)

class TileMap():
    def __init__(self, tilesize):
        pygame.init()
        self.tilesize = tilesize
        self.images = []
        self.images.append(pygame.transform.scale(pygame.image.load("tiles/smallblock.png"), (self.tilesize, self.tilesize)))
        self.array = [[0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0],
[1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0],
[1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,1,0,0,0,0,0,0,0,0,0],
[1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0],
[1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0],
[1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0],
[1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0],
[1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0],
[1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0]]
    def drawMap(self, surface, location):
            for i,row in enumerate(self.array):
                for j,tile in enumerate(row):
                    if tile > 0:
                        surface.blit(self.images[tile - 1], (location[0] + j * self.tilesize, location[1] + i * self.tilesize))

pygame.init()

tm = TileMap(32)

screen = pygame.display.set_mode((1280, 720), pygame.RESIZABLE)
pygame.display.set_caption("PyTux")
pygame.display.set_icon(pygame.image.load("images/icon.png"))

done = False

clock = pygame.time.Clock()

pygame.mixer.music.load("sounds/chipdisko.ogg")
pygame.mixer.music.play(-1)


while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.fill(pygame.color.Color("lightblue"))

    tm.drawMap(screen, (0,0))


    pygame.display.flip()

    clock.tick(60)