import pygame

pygame.init()

height = 500
widthh = 500

display_surface = pygame.display.set_mode((widthh, height))

pygame.display.set_caption("Virat Kholi with his Lamborghini")

background = pygame.transform.scale(pygame.image.load("C:\\Users\\madhu\\OneDrive\\Documents\\Python Courses\\Module 6\\Lesson 1\\Kholi.jpg").convert(), (widthh, height))

images2 = pygame.transform.scale(pygame.image.load("C:\\Users\\madhu\\OneDrive\\Documents\\Python Courses\\Module 6\\Lesson 1\\Lamborghini.jpg").convert(), (275, 183))

images2_rect = images2.get_rect()
images2_rect.center = (widthh // 2, height // 2)

text = pygame.font.Font(None, 32).render("Virat Kholi with his Lamborghini", True, (1, 0, 0))
text_rect = text.get_rect(center=(widthh // 2, 30))

clock = pygame.time.Clock()

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    display_surface.blit(background, (0, 0))
    display_surface.blit(images2, images2_rect)
    display_surface.blit(text, text_rect)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()