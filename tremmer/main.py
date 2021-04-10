import pygame as pg
from pygame.math import Vector2
import os
import math

class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

class SnakePart(pg.sprite.Sprite):

    def __init__(self, image, pos, offset, tail_len):
        super().__init__()
        self.image = image
        # A reference to the original image to preserve the quality.
        self.orig_image = self.image
        self.rect = self.image.get_rect(center=pos)
        self.pos = Vector2(pos)  # The original center position/pivot point.
        self.offset = offset*.5  # We shift the sprite 50 px to the right.
        self.angle = 0
        if tail_len > 0:
            self.tail = SnakePart(image, pos + Vector2(0,snake_size), offset, tail_len - 1)
        else:
            self.tail = None
            
    def get_all_parts(self):
        
        if self.tail == None:
            return [self]
        else:
            return [self] + self.tail.get_all_parts()

    def update(self,t,cam):
        self.angle += math.cos(t/500)
        self.rotate()
        self.pos += cam.pos
        if self.tail != None:
            self.tail.update(t,cam)

    def rotate(self):
        """Rotate the image of the sprite around a pivot point."""
        # Rotate the image.
        self.image = pg.transform.rotozoom(self.orig_image, -self.angle, .5)
        # Rotate the offset vector.
        offset_rotated = self.offset.rotate(self.angle)
        # Create a new rect with the center of the sprite + the offset.
        self.rect = self.image.get_rect(center=self.pos+offset_rotated)



class Camera:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.pos = Vector2(x,y)


    # def rect(self, rect, color):
    #     rect = rect.                # move rectangle before drawing.
    #     pg.draw.rect(screen, color, rect)


# Start the game
pg.init()
game_width = 1000
game_height = 650

center = Point(1000/2, 650/2)

screen = pg.display.set_mode((game_width, game_height))
running = True


mouse_x = 0
mouse_y = 0
cam = Camera(0,0)


size = 10
player = pg.Rect( (game_width - size) / 2, (game_height-size) /2, size, size)

snake_size = 50
snake = pg.Rect(0, 0, 150, 150)
print(os.getcwd())

snake_head = SnakePart(pg.image.load("tremmer\Tremor Scales.png"),(320, 240),Vector2(0, 88),5)
snake_group = pg.sprite.RenderPlain(snake_head.get_all_parts())

speed = .2



# ***************** Loop Land Below *****************
# Everything under 'while running' will be repeated over and over again
getTicksLastFrame = 0
while running:
    t = pg.time.get_ticks()
    deltaTime = (t - getTicksLastFrame)
    getTicksLastFrame = t
    # Makes the game stop if the player clicks the X or presses esc
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        if event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
            running = False
    screen.fill((102, 51, 0))
    snake_head.update(t,cam)
    snake_group.draw(screen)
    pg.draw.rect(screen,(255,255,255),player)

    if pg.mouse.get_pressed()[0]:
        mouse_x, mouse_y = pg.mouse.get_pos()
        print((mouse_x - center.x)/(game_width/4))
        if mouse_x - center.x > size/2:
            print(-speed, -(mouse_x - center.x)/(game_width/4)*speed)
            cam.x += max(-speed, -(mouse_x - center.x)/(game_width/4)*speed)*deltaTime
        if mouse_x - center.x < -size/2:
            cam.x += min(speed, -(mouse_x - center.x)/(game_width/4)*speed)*deltaTime
        if mouse_y - center.y < -size /2:
            cam.y += max(speed, -(mouse_y - center.y)/(game_height/4)*speed)*deltaTime
        if mouse_y - center.y > size /2:
            cam.y += min(-speed, -(mouse_y - center.y)/(game_height/4)*speed)*deltaTime

    # Tell pygame to update the screen
    pg.display.update()
