import pygame
import random
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

colorlist=[WHITE,RED,PINK,PURPLE,BLUE,YELLOW,AQUA,PINK2] #Created a list that would hold all the colors

pygame.init()

size = (700, 400)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("My picture")

done = False
clock = pygame.time.Clock()
#These are the starting position of all the wheels
circ1_x=65
circ2_x=190
circ3_x=320
circ_x_change=10

#This is the starting position of the blocks that make up the truck
rect1_x=40
rect2_x=290
rect3_x=290
rect_x_change=10
while not done:
    # --- Main event loop
    screen.fill(AQUA)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    #Color Animation
    color = random.choice(colorlist)

    # This is the sun
    pygame.draw.circle(screen, YELLOW, [650, 20], 100)

    # This is the track
    pygame.draw.line(screen, BLACK, (0, 240), (700, 240), 5)
    pygame.draw.line(screen, BLACK, (0, 270), (700, 270), 5)
    n = 1
    for i in range(30):
        pygame.draw.line(screen, BLACK, (10 + n, 230), (40 + n, 280), 5)
        n += 30

    # This is the truck
    pygame.draw.rect(screen, PURPLE,[rect1_x, 100, 250, 130])
    pygame.draw.rect(screen, PINK, [rect2_x, 160, 55, 70])
    pygame.draw.rect(screen, BLUE, [rect3_x, 100, 25, 60])

    #These are the wheels of the truck
    pygame.draw.circle(screen, color, [circ1_x, 230],27)
    pygame.draw.circle(screen, color, [circ2_x, 230], 27)
    pygame.draw.circle(screen, color, [circ3_x, 230], 30)
    pygame.draw.circle(screen, BLACK, [circ1_x, 230],27,5)
    pygame.draw.circle(screen, BLACK, [circ2_x, 230], 27,5)
    pygame.draw.circle(screen, BLACK, [circ3_x, 230], 30,5)

    #Truck Animation
    rect1_x +=rect_x_change
    rect2_x +=rect_x_change
    rect3_x +=rect_x_change

    #Animation for wheels
    circ1_x += circ_x_change
    circ2_x += circ_x_change
    circ3_x += circ_x_change
    if circ3_x > 700 or rect3_x>700 : #Only have to test if front wheel and front of truck has passed the screen
        circ1_x = 65                  #If so the truck would go back to its initial position
        circ2_x = 190
        circ3_x = 320
        rect1_x = 40
        rect2_x = 290
        rect3_x = 290

    pygame.display.flip()
    clock.tick(10)

pygame.quit()