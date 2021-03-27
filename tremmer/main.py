import pygame

# Start the game
pygame.init()
game_width = 1000
game_height = 650
screen = pygame.display.set_mode((game_width, game_height))
running = True



player = pygame.Rect(200, 200, 100, 100)
snake = pygame.Rect(0, 0, 150, 150)
snake_pic = pygame.image.load("Tremor Scales.png")
snake_pic_small = pygame.transform.scale(snake_pic, (150,150))
snake_pic_small.set_colorkey((255,255,255))



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
    pygame.draw.rect(screen, (255, 255, 0), player)
    screen.blit(snake_pic_small, (snake.x, snake.y))

    
    if player_turn and pygame.mouse.get_pressed()[0]:
        mouse_x, mouse_y = pygame.mouse.get_pos()
        if player.x > mouse_x:
            v_x += -speed
                
        if player.x < mouse_x:
            v_x += speed
                
        if player.y < mouse_y:
            v_y += speed
                
        if player.y > mouse_y:
            v_y += -speed


    # Tell pygame to update the screen
    pygame.display.update()

