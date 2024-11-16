# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from pygame.pypm import Initialize

# import constants
from constants import *

def main():
    print("Starting asteroids!")
    print("Screen width:", SCREEN_WIDTH)
    print("Screen height:", SCREEN_HEIGHT)
    # Initialize pygame
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    # Create a game loop
    while True:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        # Update the game state
        # Draw the screen
        # Fill the screen with black
        screen.fill((0, 0, 0))
        pygame.display.flip()

if __name__ == "__main__":
    main()
