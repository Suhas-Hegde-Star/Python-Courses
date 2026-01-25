import pygame
import random

pygame.init()

Sprite_Color_Change_Event = pygame.USEREVENT + 1
Backgr_Color_Change_Event = pygame.USEREVENT + 2

Blues = pygame.Color("blue")      #     
lblue = pygame.Color("lightblue") #     Background Colors
dblue = pygame.Color("darkblue")  #

Yellow = pygame.Color("yellow")   #
Magent = pygame.Color("magenta")  #     
Orange = pygame.Color("orange")   #     Sprite Colors
Whites = pygame.Color("white")    #
Blacks = pygame.Color("black")    #

class TheCoolSprite(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.velocity = [random.choice([-5, 5]), random.choice([-5, 5])]

    def update(self):
        self.rect.move_ip(self.velocity)
        boundary_hit = False
        if self.rect.left < 0 or self.rect.right > 500:
            self.velocity[0] = -self.velocity[0] 
            boundary_hit = True
        if self.rect.top < 0 or self.rect.bottom > 500:
            self.velocity[1] = -self.velocity[1]
            boundary_hit = True

        if boundary_hit:
            pygame.event.post(pygame.event.Event(Sprite_Color_Change_Event))
            pygame.event.post(pygame.event.Event(Backgr_Color_Change_Event))

    def change_color(self):
        self.image.fill(random.choice([Yellow, Magent, Orange, Whites, Blacks]))

def change_background_color():
    global Backgr_Color
    Backgr_Color = random.choice([Blues, lblue, dblue])

all_sprites_list = pygame.sprite.Group()
Sprites_number_1 = TheCoolSprite(random.choice([Yellow, Magent, Orange, Whites, Blacks]), 20, 20)
Sprites_number_1.rect.x = random.randint(0, 500)
Sprites_number_1.rect.y = random.randint(0, 500)
all_sprites_list.add(Sprites_number_1)

screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Cool Boundary Color Color Changer Sprite")
Backgr_Color = Blues
screen.fill(Backgr_Color)
runnin_on_somethin = True
clock = pygame.time.Clock()

while runnin_on_somethin:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            runnin_on_somethin = False
        elif event.type == Sprite_Color_Change_Event:
            Sprites_number_1.change_color()
        elif event.type == Backgr_Color_Change_Event:
            change_background_color()

    all_sprites_list.update()
    screen.fill(Backgr_Color)
    all_sprites_list.draw(screen)
    pygame.display.flip()
    clock.tick(100)

pygame.quit()