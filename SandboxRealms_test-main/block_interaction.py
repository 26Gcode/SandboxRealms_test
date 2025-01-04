import pygame
from constants import BLOCK_TYPES

# Initialize selected block index (starts with the first block)
selected_block_index = 0


def get_block_coords(mouse_pos, block_size):
    """Convert pixel coordinates to block coordinates."""
    x, y = mouse_pos
    return x // block_size, y // block_size


def handle_block_interaction(game_window, world, block_size):
    """Handle block placement, removal, and block selection."""
    global selected_block_index
    mouse_pos = pygame.mouse.get_pos()
    block_coords = get_block_coords(mouse_pos, block_size)
    mouse_pressed = pygame.mouse.get_pressed()

    if any(mouse_pressed):  # Check if any mouse button is pressed
        x, y = block_coords
        if 0 <= y < len(world[0]) and 0 <= x < len(world):  # Ensure within bounds
            if mouse_pressed[2]:
                world[x][y] = BLOCK_TYPES[selected_block_index]
            elif mouse_pressed[0]: 
                world[x][y] = "air"

    # Handle block selection using number keys
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if pygame.K_1 <= event.key <= pygame.K_1 + len(BLOCK_TYPES) - 1:
                selected_block_index = event.key - pygame.K_1

    # Display the selected block on the screen
    font = pygame.font.SysFont("Arial", 24)
    text = font.render(
        f"Selected Block: {BLOCK_TYPES[selected_block_index]}", True, (255, 255, 255)
    )
    game_window.blit(text, (10, 10))
