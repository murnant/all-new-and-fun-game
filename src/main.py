import pygame

# Start the game
pygame.init()
game_width = 1000
game_height = 650
screen = pygame.display.set_mode((game_width, game_height))
clock = pygame.time.Clock()
running = True
screen_border_Y = pygame.Rect(0, -1, game_width, 1)
screen_border_Y2 = pygame.Rect(0, game_height, game_width, 1)
screen_border_x = pygame.Rect(0, -1, 1, game_height)
screen_border_x2 = pygame.Rect(game_width, 0, 1, game_height)

v_x = 0
v_y = 0

enemy_size = 30
enemy_v_x = 0
enemy_v_y = 0
class Enemy():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.v_x = 0
        self.v_y = 0
        self.hot = 255
        self.hitbox = pygame.Rect(self.x, self.y, enemy_size, enemy_size)
        

    def update(self, screen):
            self.hot -= 5
            if self.hitbox.colliderect(hitbox) and self.hot >= 0:
                self.v_x = v_x * 2
                self.v_y = v_y * 2
            self.v_x *= 0.95
            self.v_y *= 0.95
            self.x += self.v_x
            self.y += self.v_y
            self.hitbox = pygame.Rect(self.x, self.y, enemy_size, enemy_size)
            if self.hot >= 0:
                pygame.draw.rect(screen, (255, self.hot, 0), self.hitbox)
            else:
                pygame.draw.rect(screen, (255, 0, 0), self.hitbox)

speed_of_game = 50
class Setting():
    def __init__(self, x, y, do):
        self.x = x
        self.y = y
        self.do = do
        self.hitbox = pygame.Rect(self.x, self.y, 30, 30)
        
    def update(self, screen):
        if pygame.mouse.get_pressed()[0] and self.hitbox.colliderect(mouse_clicker):
            self.do()
        pygame.draw.rect(screen, (255, 255, 0), self.hitbox)

            
        
size = 40
ray_on = True
ray = 120
hitbox = pygame.Rect(game_width / 2 - size / 2,600, size, size)
enemy_hitbox = pygame.Rect(game_width / 2 - enemy_size / 2, 450, enemy_size, enemy_size)
hp_bar = pygame.Rect(30, 0, 25, 25)
hp_bar2 = pygame.Rect(60, 0, 25, 25)
hp_bar3 = pygame.Rect(90, 0, 25, 25)
hp = 3
enemy_trasher = pygame.Rect(0, game_height, game_width, 10)
mouse_clicker = pygame.Rect(0, 0, 1, 1)

score = 0

f = open("high_score", "r")
high_score = int(f.read())
f.close()

enemies = []
def speed_up(self):
    speed_of_game += 1000
settings = [Setting(30, 30, speed_up)]

# ***************** Loop Land Below *****************
# Everything under 'while running' will be repeated over and over again
while True:
    keys = pygame.key.get_pressed()
    # Makes the game stop if the player clicks the X or presses esc
    for event in pygame.event.get():
        if event.type == pygame.QUIT or keys[pygame.K_SPACE]:
            running = True
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False

    screen.fill((0,0,0))
    mouse_x, mouse_y = pygame.mouse.get_pos()

    mouse_clicker.x = mouse_x
    mouse_clicker.y = mouse_y

    pygame.draw.rect(screen, (255, 0, 0), hitbox)
    pygame.draw.rect(screen, (255, 255, 0), enemy_hitbox)
    pygame.draw.rect(screen, (255, 255, 0), enemy_trasher)
    if hp == 1:
        pygame.draw.rect(screen, (255, 0, 0), hp_bar)
    if hp == 1 or  hp == 2:
        pygame.draw.rect(screen, (255, 0, 0), hp_bar2)
    if hp == 1 or hp == 2 or hp == 3:
        pygame.draw.rect(screen, (255, 0, 0), hp_bar3)

    score_font = pygame.font.SysFont("mvboli", 30)
    score_text = score_font.render("Score :"+str(score), True, (255,0,255))


    if enemy_hitbox.colliderect(hitbox):
        score += 1
        enemies.append(Enemy(enemy_hitbox.x, enemy_hitbox.y))


    screen.blit(score_text, (30, 60))
    if running:
        #move code
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            v_x += 1
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            v_x -= 1
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            v_y += 1
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            v_y -= 1
            
        v_x*= 0.9
        v_y*= 0.9
        hitbox.x += v_x
        hitbox.y += v_y

        #enemy move code
        if hitbox.x >= enemy_hitbox.x:
            enemy_v_x -= 1

        if hitbox.x <= enemy_hitbox.x:
            enemy_v_x += 1
            
        if hitbox.y <= enemy_hitbox.x:
            enemy_v_y += 1

        if hitbox.y >= enemy_hitbox.x:
            enemy_v_y -= 1

        #ray code
        if keys[pygame.K_SPACE] and ray_on:
            if hitbox.x >= enemy_hitbox.x:
                enemy_v_x += 2

            if hitbox.x <= enemy_hitbox.x:
                enemy_v_x -= 2
            
            if hitbox.y <= enemy_hitbox.x:
                enemy_v_y -= 2

            if hitbox.y >= enemy_hitbox.x:
                enemy_v_y += 2
        enemy_v_x*= 0.6
        enemy_hitbox.x += enemy_v_x

        enemy_v_y*= 0.6
        enemy_hitbox.y += enemy_v_y

        #enemy trasher code
        enemy_trasher.y -= 0.0000000000001
        if enemy_trasher.y == 0:
            enemy_trasher.y = game_height

        #kill code
        if hitbox.colliderect(screen_border_Y):
            hp -=1
            hitbox.x = game_width / 2 - size / 2
            hitbox.y = 600
            v_y = 0
            v_x = 0
        
            enemy_hitbox.x = game_width / 2 - enemy_size / 2
            enemy_hitbox.y = 450
            enemy_v_y = 0
            enemy_v_x = 0

        if hitbox.colliderect(screen_border_Y2):
            hp -=1
            hitbox.x = game_width / 2 - size / 2
            hitbox.y = 600
            v_y = 0
            v_x = 0
        
            enemy_hitbox.x = game_width / 2 - enemy_size / 2
            enemy_hitbox.y = 450
            enemy_v_y = 0
            enemy_v_x = 0

        if hitbox.colliderect(screen_border_x):
            hp -=1
            hitbox.x = game_width / 2 - size / 2
            hitbox.y = 600
            v_y = 0
            v_x = 0
        
            enemy_hitbox.x = game_width / 2 - enemy_size / 2
            enemy_hitbox.y = 450
            enemy_v_y = 0
            enemy_v_x = 0

        if hitbox.colliderect(screen_border_x2):
            hp -=1
            hitbox.x = game_width / 2 - size / 2
            hitbox.y = 600
            v_y = 0
            v_x = 0
        
            enemy_hitbox.x = game_width / 2 - enemy_size / 2
            enemy_hitbox.y = 450
            enemy_v_y = 0
            enemy_v_x = 0



        if enemy_hitbox.colliderect(screen_border_Y):
            hp -=1
            hitbox.x = game_width / 2 - size / 2
            hitbox.y = 600
            v_y = 0
            v_x = 0
        
            enemy_hitbox.x = game_width / 2 - enemy_size / 2
            enemy_hitbox.y = 450
            enemy_v_y = 0
            enemy_v_x = 0

        if enemy_hitbox.colliderect(screen_border_Y2):
            hp -=1
            hitbox.x = game_width / 2 - size / 2
            hitbox.y = 600
            v_y = 0
            v_x = 0
        
            enemy_hitbox.x = game_width / 2 - enemy_size / 2
            enemy_hitbox.y = 450
            enemy_v_y = 0
            enemy_v_x = 0

        if enemy_hitbox.colliderect(screen_border_x):
            hp -=1
            hitbox.x = game_width / 2 - size / 2
            hitbox.y = 600
            v_y = 0
            v_x = 0
        
            enemy_hitbox.x = game_width / 2 - enemy_size / 2
            enemy_hitbox.y = 450
            enemy_v_y = 0
            enemy_v_x = 0

        if enemy_hitbox.colliderect(screen_border_x2):
            hp -=1
            hitbox.x = game_width / 2 - size / 2
            hitbox.y = 600
            v_y = 0
            v_x = 0
        
            enemy_hitbox.x = game_width / 2 - enemy_size / 2
            enemy_hitbox.y = 450
            enemy_v_y = 0
            enemy_v_x = 0
        if hp <= 0:
            running = False


        #texst code
        if score > high_score :
            f = open("high_score", "w")
            f.write(str(score))
            f.close()

        
        high_score_font = pygame.font.SysFont("mvboli", True)
        high_score_text = score_font.render("high Score :"+str(high_score), True, (255,0,0))

        #ray code more
        if keys[pygame.K_SPACE] and ray_on:
            pygame.draw.line(screen, (255,0,255), (hitbox.x +size /2,hitbox.y +size /2), (enemy_hitbox.x +enemy_size /2,enemy_hitbox.y +enemy_size /2), 10)
            ray -= 3
        if ray <= 0:
            ray_on = False
        if not ray_on and not ray == 120:
            ray += 1
        if ray == 120:
            ray_on = True

        #enemy update code
        for enemy in enemies :
            enemy.update(screen)
        for enemy in enemies:
            if enemy.hitbox.colliderect(enemy_trasher):
                #enemies.remove(enemy)
                enemy.hot = 255
        for enemy in enemies:
            if enemy.hitbox.colliderect(hitbox) and enemy.hot <= 0:
                running = False
                enemies.remove(enemy)
        #update setting
        for setting in settings :
            setting.update(screen)

    #end cod
    else:
        for enemy in enemies:
            enemies.remove(enemy)
        score = 0
        hp = 3
        
        hitbox.x = game_width / 2 - size / 2
        hitbox.y = 600
        v_y = 0
        v_x = 0
        
        enemy_hitbox.x = game_width / 2 - enemy_size / 2
        enemy_hitbox.y = 450
        enemy_v_y = 0
        enemy_v_x = 0
        ray_on = True
        ray = 120

        enemy_trasher.y = game_height

    screen.blit(high_score_text, (0, 30))


    # Tell pygame to update the screen
    pygame.display.flip()
    clock.tick(speed_of_game)
    pygame.display.set_caption("MY GAME fps: " + str(clock.get_fps()))
