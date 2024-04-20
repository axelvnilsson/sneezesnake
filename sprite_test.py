import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up some constants
WIDTH, HEIGHT = 640, 480
SPEED = 2

# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Load the snake sprite
snake_image = pygame.image.load('snake.png')
snake_rect = snake_image.get_rect(center=(WIDTH / 2, HEIGHT / 2))

# Set up the initial direction
direction = (0, -1)  # Up

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                direction = (0, -1)  # Up
            elif event.key == pygame.K_a:
                direction = (-1, 0)  # Left
            elif event.key == pygame.K_s:
                direction = (0, 1)  # Down
            elif event.key == pygame.K_d:
                direction = (1, 0)  # Right

    # Move the snake
    snake_rect = snake_rect.move(direction[0] * SPEED, direction[1] * SPEED)

    # Keep the snake inside the window
    if snake_rect.left < 0:
        snake_rect.left = 0
    elif snake_rect.right > WIDTH:
        snake_rect.right = WIDTH
    if snake_rect.top < 0:
        snake_rect.top = 0
    elif snake_rect.bottom > HEIGHT:
        snake_rect.bottom = HEIGHT

    # Draw everything
    screen.fill((0, 0, 0))
    screen.blit(snake_image, snake_rect)
    pygame.display.flip()