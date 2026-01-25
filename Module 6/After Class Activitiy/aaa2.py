import pygame

pygame.init()

screen = pygame.display.set_mode((1000, 1000))
background_color = (0, 0, 0)
screen.fill(background_color)

runnin_on_somethin = True 

while runnin_on_somethin:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            runnin_on_somethin = False

    pygame.draw.rect(screen, (67, 67, 67), (67, 67, 670, 670), 100)
    font = pygame.font.SysFont("Times New Roman", 72)
    text = font.render("Hello, Pygame!", True, (255, 255, 255))
    screen.blit(text, (300, 450))

    pygame.display.update()

pygame.quit()