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


# Start the game
pygame.init()
game_width = 1000   
game_height = 650
screen = pygame.display.set_mode((game_width, game_height))
running = True

class Camera:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.pos = Vector2(x,y)

    def blit(self, pic, p):
        x,y = p
        screen.blit(pic, (x -self.x, y -self.y))

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
player = pygame.Rect( (game_width - size) / 2, (game_height-size) /2, size, size)


class Snake:
    def __init__(self,x,y,follow_part, isHead):
        self.x = x
        self.y = y
        if isHead:
            self.speed = 0.2
        else:
            self.speed = 0.1
        self.hitbox = pygame.Rect(0, 0, 150, 150)
        self.pic = pygame.image.load("tremmer\Tremor Scales.png")
        self.pic_small = pygame.transform.scale(self.pic, (150,150))
        self.pic_small.set_colorkey((255,255,255))
        self.follow_part = follow_part
        self.isHead = isHead

    def draw(self):
        cam.blit(self.pic_small , (self.x , self.y))

    def update (self):
        if self.isHead:
            follow_x = player_x
            follow_y = player_y
        else:
            follow_x = self.follow_part.x
            follow_y = self.follow_part.y
            
        if self.x > follow_x:
            self.x += -self.speed
            
        if self.x < follow_x:
            self.x += self.speed
                
        if self.y < follow_y:
            self.y += self.speed
                
        if self.y > follow_y:
            self.y += -self.speed

    

    def distance(self):
        f_x = self.follow_part.x
        f_y = self.follow_part.y
        self.d = math.sqrt( self.x**2 + self.y**2 )





snake = []

follow_part = None
for i in range (0,5):
    new_part = Snake(300,300 + i *100,follow_part, i == 0)
    snake.append(new_part)
    follow_part = new_part
    
speed = 1
player_x = player.x
player_y = player.y



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
    pygame.draw.rect(screen,(255,255,255),player)
    for s in snake:
        s.update()
    for s in snake:
        s.draw()


    
    if pygame.mouse.get_pressed()[0]:
        mouse_x, mouse_y = pygame.mouse.get_pos()


        if game_width / 2 > mouse_x - size /2:
            cam.x += -speed
            player_x += -speed
                    
        if game_width / 2 < mouse_x - size /2:
            cam.x += speed
            player_x += speed
                    
        if game_height /2 < mouse_y - size /2:
            cam.y += speed
            player_y += speed
                    
        if game_height /2 > mouse_y - size /2:
            cam.y += -speed
            player_y += -speed


    # Tell pygame to update the screen
    pygame.display.update()
    print(cam.x)
    print(player.x)
    print(snake[0].x)

