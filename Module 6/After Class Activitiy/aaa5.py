import pygame, random, sys
pygame.init()

WIDTH, HEIGHT, clock, font, WHITE, BLUE, RED, score, TIME_LIMIT, start_ticks = 800, 600, pygame.time.Clock(), pygame.font.SysFont(None, 36), (255, 255, 255), (0, 0, 255), (255, 0, 0), 0, 60, pygame.time.get_ticks()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Player and Enemies Collision")

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((40, 40))
        self.image.fill(BLUE)
        self.rect = self.image.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        self.speed = 5

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:  self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]: self.rect.x += self.speed
        if keys[pygame.K_UP]:    self.rect.y -= self.speed
        if keys[pygame.K_DOWN]:  self.rect.y += self.speed
        if keys[pygame.K_t]:     TIME_LIMIT  += 10
        self.rect.clamp_ip(screen.get_rect())

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((30, 30))
        self.image.fill(RED)
        self.rect = self.image.get_rect(center=(random.randint(20, WIDTH - 20), random.randint(20, HEIGHT - 20)))
        self.speed = random.randint(1, 3)

all_sprites = pygame.sprite.Group()
enemies = pygame.sprite.Group()
player = Player()
all_sprites.add(player)

for hehehe in range(7):
    e = Enemy()
    enemies.add(e)
    all_sprites.add(e)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    all_sprites.update()

    collided_enemies = pygame.sprite.spritecollide(player, enemies, dokill=True)
    if collided_enemies:
        score += len(collided_enemies)
        for _ in range(len(collided_enemies)):
            e = Enemy()
            enemies.add(e)
            all_sprites.add(e)

    elapsed_ms = pygame.time.get_ticks() - start_ticks
    remaining_seconds = max(0, TIME_LIMIT - (elapsed_ms // 1000))

    screen.fill(WHITE)
    all_sprites.draw(screen)
    score_text = font.render(f"Score: {score}", True, (0, 0, 0))
    screen.blit(score_text, (10, 10))

    timer_text = font.render(f"Time: {remaining_seconds//60}:{remaining_seconds%60:02d}", True, (0, 0, 0))
    screen.blit(timer_text, (WIDTH - 160, 10))

    pygame.display.flip()

    if remaining_seconds == 0:
        end_text = font.render(f"Time's up! Final Score: {score}", True, (0, 0, 0))
        screen.fill(WHITE)
        screen.blit(end_text, (WIDTH//2 - end_text.get_width()//2, HEIGHT//2 - end_text.get_height()//2))
        pygame.display.flip()
        pygame.time.delay(3000)
        break

    clock.tick(60)

pygame.quit()