import pygame
import random

from snake_include import ticker_load_facts, ticker_setup, ticker_update

# Initialize pygame
pygame.init()

# Set up screen
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Snake Game')
font_style = pygame.font.Font(None, 32)

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GRAY = (128, 128, 128)

# Set up clock
clock = pygame.time.Clock()

# Load facts
facts = ticker_load_facts()
ticker_color = GRAY

# Setup initial texts
current_text, current_text_rect = ticker_setup(facts, ticker_color, font_style, screen_width, screen_height)
next_text, next_text_rect = None, None

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

    # Draw ticker
    current_text, current_text_rect, next_text, next_text_rect = ticker_update(font_style, current_text, current_text_rect, next_text, next_text_rect, facts, ticker_color, screen_width, screen_height)
    screen.blit(current_text, current_text_rect)
    if next_text:
        screen.blit(next_text, next_text_rect)

    pygame.display.update()
    clock.tick(40)

pygame.quit()
