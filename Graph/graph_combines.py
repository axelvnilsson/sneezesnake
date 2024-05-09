import pygame
import matplotlib.pyplot as plt
import numpy as np
from pygame.locals import *
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH, SCREEN_HEIGHT = 900, 900
PLOT_SIZE = 800
WHITE = (255, 255, 255)
LIGHT_GRAY = (200, 200, 200)
BLACK = (0, 0, 0)
BUTTON_COLOR = (100, 200, 100)
FONT_SIZE = 36
ADJUSTMENT = 0.1

# Screen setup
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Matplotlib Integration with Pygame')

# Font setup
font = pygame.font.Font(None, FONT_SIZE)

# Button setup
button_rect = pygame.Rect(400, 880, 200, 50)  # Positioned at the bottom
button_text = font.render('Update Plot', True, BLACK)

# Matplotlib setup
fig, ax = plt.subplots(figsize=(4, 4), dpi=100)  # Corrected size to 800x800
canvas = FigureCanvas(fig)
ax.set_xlim(0, 10)
ax.set_ylim(0, 50)

# Initial coefficients
m = 4
c = 2

def plot_line(m, c):
    ax.clear()
    x = np.linspace(0, 10, 100)
    y = m * x + c
    ax.plot(x, y)
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 50)
    canvas.draw()
    renderer = canvas.get_renderer()
    raw_data = renderer.tostring_rgb()
    size = canvas.get_width_height()
    return pygame.image.fromstring(raw_data, size, "RGB")

# Initial plot
current_line = plot_line(m, c)

# Click counter
click_count = 0

def handle_input():
    global m, c, current_line, click_count, running

    keys = pygame.key.get_pressed()
    
    if keys[K_UP] or keys[K_w]:
        m += ADJUSTMENT
    if keys[K_DOWN] or keys[K_s]:
        m -= ADJUSTMENT
    if keys[K_LEFT] or keys[K_a]:
        c += ADJUSTMENT
    if keys[K_RIGHT] or keys[K_d]:
        c -= ADJUSTMENT
    
    # Update the plot with new values
    current_line = plot_line(m, c)

    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        elif event.type == MOUSEBUTTONDOWN:
            if button_rect.collidepoint(event.pos):
                click_count += 1
                if click_count == 1:
                    current_line = plot_line(2, 4)  # Update the plot on first click
                elif click_count == 2:
                    running = False  # Exit on second click

# Main loop
running = True
while running:
    handle_input()

    # Fill screen
    screen.fill(LIGHT_GRAY)
    
    # Draw title
    title_surface = font.render('Interactive Matplotlib Plot', True, BLACK)
    screen.blit(title_surface, (350, 20))  # Center the title
    
    # Draw the plot
    plot_x = (SCREEN_WIDTH - PLOT_SIZE) // 2
    plot_y = (SCREEN_HEIGHT - PLOT_SIZE) // 2
    screen.blit(current_line, (plot_x, plot_y))  # Center the plot
    
    # Draw button
    pygame.draw.rect(screen, BUTTON_COLOR, button_rect)
    screen.blit(button_text, (button_rect.x + 20, button_rect.y + 10))
    
    pygame.display.flip()

pygame.quit()
