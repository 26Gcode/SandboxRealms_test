import pygame
import generation
import message
from constants import window_x, window_y, sky, blue, green, red, white, black


def Game():
  
    # Initialize pygame
    pygame.init()

    # Set up the game window
    pygame.display.set_caption('SandboxRealms Pre-Alpha 1.0.0')
    game_window = pygame.display.set_mode((window_x, window_y))

    # Fill the window with blue color
    game_window.fill(sky)
    pygame.display.flip()

    # Show the block selection message at the start
    message.display_message(game_window)

    # Start the generation process
    generation.generation(game_window)
