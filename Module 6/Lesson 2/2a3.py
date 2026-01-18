import pygame

pygame.init()
screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Circle in a Circle in a Circle")
runnin_on_somethin = True
clo = pygame.time.Clock()


clorares = {
    "red": (250, 0, 0),
    "green": (0, 250, 0),
    "blue": (0, 0, 250),
    "yellow": (250, 250, 0),
    "white" : (250, 250, 250)
}

currebt_clorares = "white"

x, y = 10, 10
widt = 100
heig = 100
speed = 5

while runnin_on_somethin:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            runnin_on_somethin = False

    pre = pygame.key.get_pressed()

    if pre[pygame.K_RIGHT]: x += speed
    if pre[pygame.K_LEFT]:  x -= speed
    if pre[pygame.K_UP]:    y -= speed
    if pre[pygame.K_DOWN]:  y += speed

    x = min(max(x, 0), 500 - widt)
    y = min(max(y, 0), 500 - heig)

    if x == 0:            currebt_clorares = "red"
    elif x == 500 - widt: currebt_clorares = "green"
    elif y == 0:          currebt_clorares = "blue"
    elif y == 500 - heig: currebt_clorares = "yellow"
    else:                 currebt_clorares = "white"

    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, currebt_clorares, (x, y, widt, heig))
    pygame.display.flip()
    clo.tick(60)

pygame.quit()