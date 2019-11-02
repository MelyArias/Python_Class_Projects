for y_offset in range(300):
    pygame.draw.rect(screen, RED, [10, 20, 10 * y_offset, 10], 1)
    for y_offset in range(50):
        pygame.draw.rect(screen, RED, [10, 20 * y_offset, 10, 10],1)