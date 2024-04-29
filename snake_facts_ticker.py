import pygame
import random

from snake_include import ticker_load_facts, ticker_update, ticker_setup

# Initialize pygame
pygame.init()

# Set up screen
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Snake Game')

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

ticker_color = WHITE
ticker_font = pygame.font.Font(None, 32)

# Set up clock
clock = pygame.time.Clock()

ticker_tape = ticker_load_facts()
text, text_rect = ticker_setup(ticker_tape, ticker_font, ticker_color, screen_width, screen_height)

# Initial position of the apple
apple_x = random.randint(0, screen_width-20)
apple_y = random.randint(0, screen_height-20)

# Game loop
running = True
while running:
    screen.fill(BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Apple movement controls
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]:
        apple_x += 5
    if keys[pygame.K_LEFT]:
        apple_x -= 5
    if keys[pygame.K_DOWN]:
        apple_y += 5
    if keys[pygame.K_UP]:
        apple_y -= 5

    # Check boundaries for the apple
    if apple_x < 0:
        apple_x = 0
    elif apple_x > screen_width - 20:
        apple_x = screen_width - 20
    if apple_y < 0:
        apple_y = 0
    elif apple_y > screen_height - 20:
        apple_y = screen_height - 20

    # Draw the apple
    pygame.draw.rect(screen, RED, (apple_x, apple_y, 20, 20))

    # Update and draw the ticker
    text, text_rect = ticker_update(text, text_rect)
    screen.blit(text, text_rect)

    pygame.display.update()
    clock.tick(40)

pygame.quit()
