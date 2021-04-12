import pygame
import os

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

    def blit(self, pic, p):
        x,y = p
        screen.blit(pic, (x -self.x, y -self.y))

    # def rect(self, rect, color):
    #     rect = rect.                # move rectangle before drawing.
    #     pygame.draw.rect(screen, color, rect)

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
while running:
    # Makes the game stop if the player clicks the X or presses esc
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
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

