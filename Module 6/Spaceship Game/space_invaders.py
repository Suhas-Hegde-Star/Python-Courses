from turtle import distance
import pygame
import random
import math

# Set the Variables
Height = 600
Width = 800
Player_Start_X = 370
Player_Start_Y = 380
Enemy_Start_Y_Min = 50
Enemy_Start_Y_Max = 150
Enemy_Speed_X = 1
Enemy_Speed_Y = 1
Bullet_Speed_Y = 10
Collision_Threshold = 27
TIME_LIMIT = 676

# Initialize Pygame
pygame.init()

# Create the Screen
screen = pygame.display.set_mode((Width, Height))

# Background
background = pygame.image.load('C:\\Users\\madhu\\OneDrive\\Documents\\Python Courses\\Module 6\\Spaceship Game\\image.png')

# Caption and Icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('C:\\Users\\madhu\\OneDrive\\Documents\\Python Courses\\Module 6\\Spaceship Game\\ufo.png')
pygame.display.set_icon(icon)

# Player
PayerImg = pygame.image.load('C:\\Users\\madhu\\OneDrive\\Documents\\Python Courses\\Module 6\\Spaceship Game\\player.png')
PlayerX = Player_Start_X
PlayerY = Player_Start_Y
PlayerX_change = 0

# Enemy
EnemyImg = []
EnemyX = []
EnemyY = []
EnemyX_change = []
EnemyY_change = []
num_of_enemies = 6

for i in range(num_of_enemies):
    EnemyImg.append(pygame.image.load('C:\\Users\\madhu\\OneDrive\\Documents\\Python Courses\\Module 6\\Spaceship Game\\enemy.png'))
    EnemyX.append(random.randint(0, Width - 64))
    EnemyY.append(random.randint(Enemy_Start_Y_Min, Enemy_Start_Y_Max))
    EnemyX_change.append(Enemy_Speed_X)
    EnemyY_change.append(Enemy_Speed_Y)

# Bullet
BulletImg = pygame.transform.scale(pygame.image.load('C:\\Users\\madhu\\OneDrive\\Documents\\Python Courses\\Module 6\\Spaceship Game\\bull.png'), (32, 32))
BulletX = 0
BulletY = PlayerY 
BullerX_change = 0
BulletY_change = Bullet_Speed_Y
Bullet_state = "ready"

# Score
score_value = 0
font = pygame.font.Font('freesansbold.ttf', 32)
textX = 10
textY = 10

# Game Over
over_font = pygame.font.Font('freesansbold.ttf', 64)
timer_font = pygame.font.Font('freesansbold.ttf', 32)

# Timer
start_ticks = pygame.time.get_ticks()

def show_score(x, y):
    score = font.render("Score : " + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))

def show_timer(x, y):
    elapsed_time = (pygame.time.get_ticks() - start_ticks) // 1000
    remaining_time = max(0, TIME_LIMIT - elapsed_time)
    minutes = remaining_time // 60
    seconds = remaining_time % 60
    timer_text = timer_font.render(f"Time: {minutes}:{seconds:02d}", True, (255, 255, 255))
    screen.blit(timer_text, (x, y))

def game_over_text():
    over_text = over_font.render("GAME OVER", True, (255, 255, 255))
    screen.blit(over_text, (200, 250))

def player(x, y):
    screen.blit(PayerImg, (x, y))

def enemy(x, y, i):
    screen.blit(EnemyImg[i], (x, y))

def _fire_bullet(x, y):
    global Bullet_state
    Bullet_state = "fire"
    screen.blit(BulletImg, (x + 16, y + 10))

def is_collision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt((math.pow(enemyX - bulletX, 2)) + (math.pow(enemyY - bulletY, 2)))
    return distance < Collision_Threshold

running = True
Clock = pygame.time.Clock()
game_over = False

while running:
    screen.fill((0, 0, 0))
    screen.blit(background, (0, 0))
    
    elapsed_time = (pygame.time.get_ticks() - start_ticks) // 1000

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                PlayerX_change = -5
            if event.key == pygame.K_RIGHT:
                PlayerX_change = 5
            if event.key == pygame.K_SPACE:
                if Bullet_state == "ready" and not game_over:
                    BulletX = PlayerX
                    _fire_bullet(BulletX, BulletY)
            if event.key == pygame.K_t:
                TIME_LIMIT += 3
            if event.key == pygame.K_r:
                TIME_LIMIT -= 60
            if event.key == pygame.K_p:
                score_value += 20
            if event.key == pygame.K_e:
                BulletImg = pygame.transform.scale(pygame.image.load('C:\\Users\\madhu\\OneDrive\\Documents\\Python Courses\\Module 6\\Spaceship Game\\bullet.png'), (32, 32))
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                PlayerX_change = 0
    
    if not game_over:
        if elapsed_time >= TIME_LIMIT:
            game_over = True
            
        PlayerX += PlayerX_change
        PlayerX = max(0, min(PlayerX, Width - 64))

        for i in range(num_of_enemies):
            if EnemyY[i] > 340:
                for j in range(num_of_enemies):
                    EnemyY[j] = 2000
                game_over_text()
                game_over = True
                break

            EnemyX[i] += EnemyX_change[i]
            if EnemyX[i] <= 0 or EnemyX[i] >= Width - 64:
                EnemyX_change[i] = -EnemyX_change[i]
                EnemyY[i] += EnemyY_change[i]

            if is_collision(EnemyX[i], EnemyY[i], BulletX, BulletY):
                BulletY = PlayerY
                Bullet_state = "ready"
                score_value += 1
                EnemyX[i] = random.randint(0, Width - 64)
                EnemyY[i] = random.randint(Enemy_Start_Y_Min, Enemy_Start_Y_Max)

            enemy(EnemyX[i], EnemyY[i], i)

        if BulletY <= 0:
            BulletY = PlayerY
            Bullet_state = "ready"

        if Bullet_state == "fire":
            _fire_bullet(BulletX, BulletY)
            BulletY -= BulletY_change

        player(PlayerX, PlayerY)
    
    if game_over:
        game_over_text()

    show_score(textX, textY)
    show_timer(620, textY)
    pygame.display.update()
    Clock.tick(60)

pygame.quit()