import numpy as np
import pygame
import random
import math
from pendulums import Pendulum


def draw_pend(screen, time, pendulum, center, zoom):
    angle = pendulum.update_angle(time)

    # Drawing the line
    pend_offset_x = zoom * pendulum.length * math.sin(angle) #* flip
    pend_offset_y = zoom * pendulum.length * math.cos(angle)

    final_x = center[0] + pend_offset_x
    final_y = center[1] + pend_offset_y

    pygame.draw.line(screen, (0,0,0), center, [final_x, final_y], 5)
    pygame.draw.circle(screen, (0,127,127), [final_x, final_y], 30)

def main():
    pygame.init()
    running = True


    size = (1400,1000)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Offset Pendulums")

    clock = pygame.time.Clock()

    # Initial settings
    center = np.array([700,100])
    black = (0,0,0)

    pend1 = Pendulum(1, math.pi/4)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Draw Code
        screen.fill((255,255,255))
        pygame.draw.circle(screen, black, center, 10)
        draw_pend(screen, (pygame.time.get_ticks()/1000), pend1, center, 400)


        pygame.display.flip()
        clock.tick(60)


if __name__ == "__main__":
    main()
