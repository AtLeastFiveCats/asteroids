import pygame
from constants import *
from player import *

def main():
    pygame.init() 
    
    #Creating a group for the player class
    updatable = pygame.sprite.Group() 
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)

    #Sets the game clock
    game_time = pygame.time.Clock()
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    
    #Used for delta time
    dt = 0
    print(f"Starting Asteroids! \nScreen width: {SCREEN_WIDTH} \nScreen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            #moves our character position
        updatable.update(dt)
            #creates the black screen
        screen.fill((0, 0, 0))
            #draw our sprite
        for sprites in drawable:
            sprites.draw(screen)
            #dt will use the ingame clock to set speeds rather than relying on our computer clock
        dt = game_time.tick(60) / 1000
            #updates the screen
        pygame.display.flip()


if __name__ == "__main__":
    main()
