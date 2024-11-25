import pygame
import generation
import message

# Define window size
window_x = 1820
window_y = 930

# Define color constants
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)
sky = pygame.Color(160, 160, 255)

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
