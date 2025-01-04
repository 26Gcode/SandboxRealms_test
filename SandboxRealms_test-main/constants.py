import pygame
import os

# Define window size
window_x = 1820
window_y = 928

# Define color constants
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)
sky = pygame.Color(160, 160, 255)

# Define constants for block types
BLOCK_TYPES = ["grass", "dirt", "stone"]


# Texture loading function with error handling
def load_texture(file_path, scale_factor=0.2):
    """Loads and scales a texture."""
    try:
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"Texture file not found: {file_path}")
        
        texture = pygame.image.load(file_path)
        texture = pygame.transform.scale(texture, (
            int(texture.get_width() * scale_factor),
            int(texture.get_height() * scale_factor)
        ))
        return texture
    except Exception as e:
        print(f"Error loading texture: {e}")
        return None

# Load textures for each block type
dirt_texture = load_texture('textures/dirt_block.png')
grass_texture = load_texture('textures/grass_block.png')
stone_texture = load_texture('textures/stone_block.png')
air_texture = load_texture('textures/air_block.png')