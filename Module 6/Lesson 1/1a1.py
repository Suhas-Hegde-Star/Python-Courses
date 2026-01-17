import pygame

pygame.init()

screen = pygame.display.set_mode((400, 500))

runnin_on_somethin = True

while runnin_on_somethin:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            runnin_on_somethin = False
    pygame.display.update()

pygame.quit()