import pygame

pygame.init()

screen = pygame.display.set_mode((500, 500))

pygame.display.set_caption("My First Pygame Window")

images_2 = pygame.transform.scale(pygame.image.load("C:\\Users\\madhu\\OneDrive\\Documents\\Python Courses\\Module 6\\After Class Activitiy\\Kholi.jpg").convert(), (300, 300))
images2_rect = images_2.get_rect()
images2_rect.center = (500 // 2, 500 // 2)

run = True

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    screen.fill(("grey"))
    screen.blit(images_2, images2_rect)
    pygame.display.update()

pygame.quit()