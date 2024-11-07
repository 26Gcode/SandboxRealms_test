import pygame
import generation

# Define window size
window_x = 1920
window_y = 1030

# Define color constants
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)

# Initialize pygame
pygame.init()

# Set up the game window
pygame.display.set_caption('MineRealm Pre-Alpha 1.0')
game_window = pygame.display.set_mode((window_x, window_y))

# Fill the window with blue color
game_window.fill(blue)
pygame.display.flip()

# Start the generation process
generation.generation(game_window)
