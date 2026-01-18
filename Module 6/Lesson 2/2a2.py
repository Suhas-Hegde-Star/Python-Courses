import pygame

pygame.init()

screen = pygame.display.set_mode((400, 500))

pygame.display.set_caption("Circle in a Circle in a Circle")

runnin_on_somethin = True

while runnin_on_somethin:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            runnin_on_somethin = False

    pygame.draw.circle(screen, (250, 0, 0), (100, 100), 25)
    pygame.draw.circle(screen, (0, 250, 0), (100, 100), 50, 5)
    pygame.draw.circle(screen, (0, 0, 250), (100, 100), 75, 10)

    pygame.display.flip()

pygame.quit()