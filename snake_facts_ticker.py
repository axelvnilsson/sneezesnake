import pygame
import random

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

# Set up clock
clock = pygame.time.Clock()

# Load snake facts from file
with open('snake_facts.txt', 'r') as file:
    facts = file.readlines()

# Function to get a random fact
def get_random_fact():
    return random.choice(facts).strip()

# Initial ticker setup
font = pygame.font.Font(None, 32)
text = font.render(get_random_fact(), True, WHITE)
text_rect = text.get_rect()
text_rect.right = screen_width  # Start off right edge of screen
text_rect.bottom = screen_height  # Position at the bottom of the screen

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

    # Move the apple
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

    # Update text position for the ticker
    text_rect.x -= 2  # Move text left
    if text_rect.right < 0:  # If text has moved past the left side
        text = font.render(get_random_fact(), True, WHITE)  # Get new fact
        text_rect = text.get_rect()
        text_rect.left = screen_width  # Start from the right again
        text_rect.bottom = screen_height  # Keep it at the bottom

    # Draw the text
    screen.blit(text, text_rect)

    pygame.display.update()
    clock.tick(40)

pygame.quit()
