import pygame

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

    def blit(self, pic):
        pass

    # def rect(self, rect, color):
    #     rect = rect.                # move rectangle before drawing.
    #     pygame.draw.rect(screen, color, rect)

mouse_x = 0
mouse_y = 0
cam = Camera(0,0)


size = 10
player = pygame.Rect( (game_width - size) / 2, (game_height-size) /2, size, size)
snake = pygame.Rect(0, 0, 150, 150)
snake_pic = pygame.image.load("Tremor Scales.png")
snake_pic_small = pygame.transform.scale(snake_pic, (150,150))
snake_pic_small.set_colorkey((255,255,255))

speed = 1



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
    screen.blit(snake_pic_small, (snake.x, snake.y))
    screen.rect(player,(255,255,255))

    
    if pygame.mouse.get_pressed()[0]:
        mouse_x, mouse_y = pygame.mouse.get_pos()


    if game_width / 2 > mouse_x - size /2:
        cam.x += -speed
                
    if game_width / 2 < mouse_x - size /2:
        cam.x += speed
                
    if game_height /2 < mouse_y - size /2:
        cam.y += speed
                
    if game_height /2 > mouse_y - size /2:
        cam.y += -speed


    # Tell pygame to update the screen
    pygame.display.update()

