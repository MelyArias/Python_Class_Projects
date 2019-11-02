#Mely Arias
#6.1 Part 1
n=10 #this is setting the starting number to be 10
for rows in range(10):
    for columns in range(rows):
        print(n," ",end="") #This is printing the number and then a space next to it for the number of rows
        n+=1
    print()

#Part 2
n=int(input("ENTER NUMBER"))
for rows in range(n+2): #This is going to print 'o' vertically for the number the user entered plus 2
    print("o", end="")
print()
for rows in range(n-2):
    print("o",end="")
    for columns in range(n):
        print(" ", end="") #This is going to handle the spaces next to every number
    print("o", end="")
    print()
for columns in range(n+2):
    print("o", end="")

#Part 4
import pygame
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

pygame.init()

size = (700, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Pygame Grid")

done = False
clock = pygame.time.Clock()

while not done:
    # --- Main event loop
    screen.fill(BLACK)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    y_offset=0
    x_offset=0
    for y_offset in range(1,50,2): #This is going to iterate the code below for odd numbers from 1 to 49
        for x_offset in range(100):
            pygame.draw.rect(screen, RED, [20*x_offset, 10 * y_offset, 10, 10]) #I multiplied the x axis and y axis of the starting coordinates so we can have many squares at different positions
    pygame.display.flip()
    clock.tick(60)

pygame.quit()