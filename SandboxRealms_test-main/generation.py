import pygame
import random
import os
from block_interaction import handle_block_interaction  # Use functions from block_interaction
from constants import dirt_texture, grass_texture, stone_texture, air_texture
texture_map = {}





def generate_world(width, height):
    """Generates the initial grid of the world."""
    world = []
    for x in range(width):
        BLOCK_TYPES2 = ["grass", "grass", "air"]
        col = []
        for i in range(0, 4):
            col.append("air")
        for y in range(height // 6):  # Adjust block height scaling
            block_type = random.choice(BLOCK_TYPES2)
            if block_type == "grass":
                BLOCK_TYPES2 = ["dirt"]
            col.append(block_type)
        for i in range(0, 20):
            col.append("stone")
        world.append(col)
    return world


def draw_world(game_window, world, block_size, textures):
    """Draws the world (grid of blocks) on the screen."""
    for x, col in enumerate(world):
        for y, block_type in enumerate(col):
            block_texture = textures.get(block_type)
            if block_texture:
                game_window.blit(block_texture, (x * block_size, y * block_size))
                if block_texture == "dirt":
                    texture_map[0].append(x*block_size, y*block_size)
                elif block_texture == "grass":
                    texture_map[1].append(x*block_size, y*block_size)
                elif block_texture == "stone":
                    texture_map[2].append(x*block_size, y*block_size)
                elif block_texture == "air":
                    texture_map[3].append(x*block_size, y*block_size)


def generation(game_window):
    """Handles the generation of game content."""
    

    # Store textures in a dictionary for easy access
    block_textures = {
        "dirt": dirt_texture,
        "grass": grass_texture,
        "stone": stone_texture,
        "air": air_texture
    }

    # Define world size and block size
    world_width = 100  # Number of blocks horizontally
    world_height = 40  # Number of blocks vertically
    block_size = 32  # Size of each block in pixels

    # Generate the world (a grid of blocks)
    world = generate_world(world_width, world_height)
    
    # Main game loop
    running = True
    while running:
        # Fill screen with blue background
        game_window.fill((135, 206, 235))  # Sky blue background

        # Handle block interaction
        handle_block_interaction(game_window, world, block_size)

        # Draw the generated world
        draw_world(game_window, world, block_size, block_textures)

        # Event handling for quitting the game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Update the display
        pygame.display.flip()

    # Quit pygame when the loop ends
    pygame.quit()
