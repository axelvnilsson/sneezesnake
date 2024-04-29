import pygame
import random

from snake_include import ticker_load_facts, ticker_setup, draw_ticker

# Initialize pygame
pygame.init()

# Set up screen
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Snake Game')
clock = pygame.time.Clock()

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Initial position of the food
food_x = random.randint(0, screen_width-20)
food_y = random.randint(0, screen_height-20)

# ticker settings
ticker_font = pygame.font.Font(None, 32)
ticker_color = WHITE
ticker_tape = ticker_load_facts()
text, text_rect = ticker_setup(ticker_tape, ticker_font, ticker_color, screen_width, screen_height)

# Game loop
running = True
while running:
    screen.fill(BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # food movement controls
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]:
        food_x += 5
    if keys[pygame.K_LEFT]:
        food_x -= 5
    if keys[pygame.K_DOWN]:
        food_y += 5
    if keys[pygame.K_UP]:
        food_y -= 5

    # Check boundaries for the food
    if food_x < 0:
        food_x = 0
    elif food_x > screen_width - 20:
        food_x = screen_width - 20
    if food_y < 0:
        food_y = 0
    elif food_y > screen_height - 20:
        food_y = screen_height - 20

    # Draw the food
    pygame.draw.rect(screen, RED, (food_x, food_y, 20, 20))

    # Update and draw the ticker
    text, text_rect = draw_ticker(screen, text, text_rect) # Update the ticker

    pygame.display.update()
    clock.tick(40)

pygame.quit()
