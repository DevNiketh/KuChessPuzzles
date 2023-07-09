import pygame
import os

from Chess.data.classes.Board import Board

pygame.init()

WINDOW_SIZE = (600, 600)
screen = pygame.display.set_mode(WINDOW_SIZE)

board = Board(WINDOW_SIZE[0], WINDOW_SIZE[1])

# Define colors
WHITE = (255, 255, 255)
BACKGROUND_COLOR = (0, 0, 0)
TEXT_COLOR = (255, 255, 255)
OPAQUE_ALPHA = 128

# Define the path to your custom font file
font_path = os.path.join("data/font/fon.ttf")

# Load the custom font
font_size = 69
font = pygame.font.Font(font_path, font_size)

def draw(display):
    display.fill(WHITE)
    board.draw(display)

    if board.is_in_checkmate('black'):  # If black is in checkmate
        text = font.render('White wins!', True, TEXT_COLOR)
    elif board.is_in_checkmate('white'):  # If white is in checkmate
        text = font.render('Black wins!', True, TEXT_COLOR)
    else:
        text = None

    if text:
        # Create a slightly opaque background surface
        background_surface = pygame.Surface((WINDOW_SIZE[0], WINDOW_SIZE[1]))
        background_surface.fill(BACKGROUND_COLOR)
        background_surface.set_alpha(OPAQUE_ALPHA)

        # Calculate the position to center the text
        text_x = (WINDOW_SIZE[0] - text.get_width()) // 2
        text_y = (WINDOW_SIZE[1] - text.get_height()) // 2

        # Blit the background surface and the text onto the display
        display.blit(background_surface, (0, 0))
        display.blit(text, (text_x, text_y))

        # Render "Play again" text
        play_again_text = font.render("Play again", True, (252, 252, 96))  # Yellow color
        play_again_text = pygame.transform.scale(play_again_text, (
        int(play_again_text.get_width() * 0.5), int(play_again_text.get_height() * 0.5)))  # Scale down the text
        play_again_x = (WINDOW_SIZE[0] - play_again_text.get_width()) // 2
        play_again_y = text_y + text.get_height() + 20
        display.blit(play_again_text, (play_again_x, play_again_y))

        # Get the rectangle of "Play again" text for mouse click detection
        play_again_rect = play_again_text.get_rect(topleft=(play_again_x, play_again_y))

        # Check for mouse click on "Play again" text
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1 and play_again_rect.collidepoint(event.pos):
                    board.reset()

    pygame.display.update()


if __name__ == '__main__':
    running = True
    while running:
        mx, my = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    board.handle_click(mx, my)

        draw(screen)
