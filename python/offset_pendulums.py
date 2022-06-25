import numpy as np
import pygame
import random

def main():
    pygame.init()
    running = True


    size = (1400,1000)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Offset Pendulums")

    clock = pygame.time.Clock()

    # Initial settings
    line_start = np.array([100,100])
    line_end = np.array([500,500])
    lb, ub = [-10,10]
    black = (0,0,0)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Logic
        line_start = line_start + [random.randint(lb, ub), random.randint(lb, ub)]
        line_end = line_end + [random.randint(lb, ub), random.randint(lb, ub)]
        # Draw Code
        screen.fill((255,255,255))
        pygame.draw.line(screen, black, line_start, line_end, 5)


        pygame.display.flip()
        clock.tick(60)


if __name__ == "__main__":
    main()
