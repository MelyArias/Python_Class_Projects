import pygame
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
PINK=(255,26,198)
PURPLE=(204,0,255)
BLUE=(0,153,255)
YELLOW=(255,255,0)
AQUA=(0,255,255)
PINK2=(255,0,102)

pygame.init()

size = (700, 400)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("My picture")

done = False
clock = pygame.time.Clock()

while not done:
    # --- Main event loop
    screen.fill(AQUA)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # This is the sun
    pygame.draw.circle(screen, YELLOW, [650, 20], 100)

    # This is the track
    pygame.draw.line(screen, BLACK, (0, 240), (650, 240), 5)
    pygame.draw.line(screen, BLACK, (0, 270), (650, 270), 5)
    n = 1
    for i in range(20):
        pygame.draw.line(screen, BLACK, (10 + n, 230), (40 + n, 280), 5)
        n += 30

    # This is the truck
    pygame.draw.rect(screen, PURPLE, [150, 100, 250, 130])
    pygame.draw.rect(screen, PINK, [400, 160, 75, 70])
    pygame.draw.rect(screen, BLUE, [400, 100, 45, 60])

    #These are the wheels of the truck
    pygame.draw.circle(screen, GREEN, [175, 230],27)
    pygame.draw.circle(screen, GREEN, [300, 230], 27)
    pygame.draw.circle(screen, GREEN, [430, 230], 30)
    pygame.draw.circle(screen, PINK2, [175, 230],27,5)
    pygame.draw.circle(screen, PINK2, [300, 230], 27,5)
    pygame.draw.circle(screen, PINK2, [430, 230], 30,5)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()