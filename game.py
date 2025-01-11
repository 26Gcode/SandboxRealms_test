import pygame
from generation import Generation
import message
from constants import window_x, window_y, sky, blue, green, red, white, black


class Game():
  
    # Initialize pygame
    def __init__(self):
        pygame.init()
        
        # Set up the game window 
        self.screen = pygame.display.set_caption('SandboxRealms Pre-Alpha 1.0.0')
        game_window = pygame.display.set_mode((window_x, window_y))
        self.clock = pygame.time.Clock()
        self.running = True
        self.generation = Generation()
        self.current_block = "sky"

        # Show the block selection message at the start
        message.display_message(game_window)

        # Start the generation process
        Generation.generation(game_window)

    def update(self):
        pass

    def draw(self):
        # Fill the window with blue color
        self.screen.fill(sky)
        pygame.display.flip()


    
