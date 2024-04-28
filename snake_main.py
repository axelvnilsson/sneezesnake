import pygame
import random

from snake_include import handle_game_over, handle_key_events  # Import the game over and all other functions

# Initialize Pygame and other game settings
pygame.init()
width, height = 800, 600
game_window = pygame.display.set_mode((width, height))
pygame.display.set_caption('Snake Game')
clock = pygame.time.Clock()
font_style = pygame.font.SysFont(None, 50)

# Colors
blue = (0, 0, 255)
white = (255, 255, 255)
green = (0, 255, 0)
red = (255, 0, 0)
black = (0, 0, 0)
yellow = (255, 255, 0)  # Color for the chaser

# Snake attributes
block_size = 20
snake_speed = 15


def display_score(score):
    score_text = font_style.render("Score: " + str(score), True, white)
    game_window.blit(score_text, [0, 0])

def draw_snake(snake_list):
    for block in snake_list:
        pygame.draw.rect(game_window, green, [int(block[0]), int(block[1]), block_size, block_size])

def draw_chaser(chaser_x, chaser_y):
    pygame.draw.rect(game_window, yellow, [int(chaser_x), int(chaser_y), block_size, block_size])

def game_loop():
    game_active = True
    game_over = False

    # Snake parameters
    x = width / 2
    y = height / 2
    x_change = 0
    y_change = 0

    snake_list = []
    length_of_snake = 1
    last_speed_increase = 0  # Initialize the last_speed_increase variable

    # Initial position of the food
    food_x = round(random.randrange(0, width - block_size) / block_size) * block_size
    food_y = round(random.randrange(0, height - block_size) / block_size) * block_size

    # Chaser parameters
    chaser_x = random.randrange(0, width - block_size, block_size)
    chaser_y = random.randrange(0, height - block_size, block_size)
    chaser_speed = 5  # Initial chaser speed

    while game_active:

        while game_over:
            # Handle game over scenario
            restart_from_beginning = handle_game_over(game_window, font_style, width, height, length_of_snake - 1)
            if restart_from_beginning == True:
                game_loop()  # Restart the game from the beginning
            else:
                game_over = False # Don't go back and show the game over screen again
                game_active = False # Don't quit out of the game

        # Handle key events - this returns the change in x and y coordinates depending on which key is pressed
        # The keys used to move the snake are the arrow keys and the WASD keys or the arrow keys
        x_change, y_change, game_interrupted = handle_key_events(x_change, y_change, block_size)
        if game_interrupted:
            break

        if x >= width or x < 0 or y >= height or y < 0:
            game_over = True

        x += x_change
        y += y_change

        # Chaser movement logic
        if chaser_x < x:
            chaser_x += chaser_speed
        elif chaser_x > x:
            chaser_x -= chaser_speed

        if chaser_y < y:
            chaser_y += chaser_speed
        elif chaser_y > y:
            chaser_y -= chaser_speed

        game_window.fill(blue)
        pygame.draw.rect(game_window, red, [food_x, food_y, block_size, block_size])

        snake_head = [x, y]
        snake_list.append(snake_head)
        if len(snake_list) > length_of_snake:
            del snake_list[0]

        for block in snake_list[:-1]:
            if block == snake_head:
                game_close = True

        draw_snake(snake_list)
        draw_chaser(chaser_x, chaser_y)

        # Check for collision with chaser
        if abs(x - chaser_x) < block_size and abs(y - chaser_y) < block_size:
            game_over = True

        display_score(length_of_snake - 1)

        # Increment chaser speed gradually
        if length_of_snake > 10 and (length_of_snake - 1) % 10 == 0 and (length_of_snake - 1) != last_speed_increase:
            chaser_speed += 2
            last_speed_increase = length_of_snake - 1

        pygame.display.update()

        if x == food_x and y == food_y:
            food_x = round(random.randrange(0, width - block_size) / block_size) * block_size
            food_y = round(random.randrange(0, height - block_size) / block_size) * block_size
            length_of_snake += 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()

game_loop() 