import pygame
from constants import *

def main():
    pygame.init()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return
    print(f"Starting Asteroids! \nScreen width: {SCREEN_WIDTH} \nScreen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    while True: 
        screen.fill((0, 0, 0))
        pygame.display.flip()

if __name__ == "__main__":
    main()
