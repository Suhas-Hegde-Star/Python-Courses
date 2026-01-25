import pygame
import random

pygame.init()

Widths, Height, Speeds, Font_s = 1000, 1000, 5, 72
background, font = pygame.transform.scale(pygame.image.load("C:\\Users\\madhu\\OneDrive\\Documents\\Python Courses\\Module 6\\Lesson 4\\image.png"), (Widths, Height)), pygame.font.SysFont("Times New Roman", Font_s)

class Sproite(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        pygame.draw.rect(self.image, color, [0, 0, width, height])
        self.rect = self.image.get_rect()

    def move_it_move_it(self, x_change, y_change):
        self.rect.x = max(min(self.rect.x + x_change, Widths - self.rect.width ), 0)
        self.rect.y = max(min(self.rect.y + y_change, Height - self.rect.height), 0)

screen = pygame.display.set_mode((Widths, Height))
pygame.display.set_caption("Sprites Are Ambulances")
all_sprites_list = pygame.sprite.Group()

sprite1 = Sproite(pygame.Color("black"), 20, 30)
sprite1.rect.x = random.randint(0, Widths - sprite1.rect.width)
sprite1.rect.y = random.randint(0, Height - sprite1.rect.height)
all_sprites_list.add(sprite1)

sprite2 = Sproite(pygame.Color("Red"), 20, 30)
sprite2.rect.x = random.randint(0, Widths - sprite2.rect.width)
sprite2.rect.y = random.randint(0, Height - sprite2.rect.height)
all_sprites_list.add(sprite2)
clock, running = pygame.time.Clock(), True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_x):
            running = False

    keys = pygame.key.get_pressed()
    x1_change = (keys[pygame.K_d]     - keys[pygame.K_a   ]) * Speeds
    y1_change = (keys[pygame.K_s]     - keys[pygame.K_w   ]) * Speeds
    sprite1.move_it_move_it(x1_change, y1_change)
        

    screen.blit(background, (0, 0))
    all_sprites_list.draw(screen)
    pygame.display.flip()
    clock.tick(80)
pygame.quit()