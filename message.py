import pygame

def display_message(game_window):
    """Displays a small message box with block selection instructions."""
    running = True
    font = pygame.font.SysFont("Arial", 20)
    small_font = pygame.font.SysFont("Arial", 16)

    # Message dimensions and positioning
    box_width = 400
    box_height = 200
    box_x = (game_window.get_width() - box_width) // 2
    box_y = (game_window.get_height() - box_height) // 2

    # Button dimensions
    button_width = 100
    button_height = 30
    button_x = box_x + (box_width - button_width) // 2
    button_y = box_y + box_height - 50

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left mouse button
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    if button_x <= mouse_x <= button_x + button_width and button_y <= mouse_y <= button_y + button_height:
                        running = False

        # Draw the message box
        pygame.draw.rect(game_window, (255, 255, 255), (box_x, box_y, box_width, box_height))
        pygame.draw.rect(game_window, (0, 0, 0), (box_x, box_y, box_width, box_height), 2)

        # Render the text
        title = font.render("Block Selection Guide", True, (0, 0, 0))
        instructions = [
            "1: Grass Block",
            "2: Dirt Block",
            "3: Stone Block"
        ]
        title_rect = title.get_rect(center=(box_x + box_width // 2, box_y + 30))
        game_window.blit(title, title_rect)

        for i, text in enumerate(instructions):
            line = small_font.render(text, True, (0, 0, 0))
            game_window.blit(line, (box_x + 20, box_y + 60 + i * 20))

        # Draw the close button
        pygame.draw.rect(game_window, (200, 200, 200), (button_x, button_y, button_width, button_height))
        button_text = font.render("Close", True, (0, 0, 0))
        button_text_rect = button_text.get_rect(center=(button_x + button_width // 2, button_y + button_height // 2))
        game_window.blit(button_text, button_text_rect)

        # Update the display
        pygame.display.flip()
