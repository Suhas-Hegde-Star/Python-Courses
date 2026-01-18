import pygame

pygame.init()

screen = pygame.display.set_mode((1000, 1000))

runnin_on_somethin = True 

while runnin_on_somethin:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            runnin_on_somethin = False

    pygame.draw.rect(screen, (67, 67, 67), (67, 67, 670, 670), 100)

    pygame.display.update()

pygame.quit()