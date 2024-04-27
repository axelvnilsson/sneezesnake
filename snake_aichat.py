import pygame
import random

pygame.init()

# Window dimensions
width = 800
height = 600

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

# Initialize window
game_window = pygame.display.set_mode((width, height))
pygame.display.set_caption('Snake Game')

# Clock for controlling speed
clock = pygame.time.Clock()

# Font settings
font_style = pygame.font.SysFont(None, 50)

def display_score(score):
    score_text = font_style.render("Score: " + str(score), True, white)
    game_window.blit(score_text, [0, 0])

def draw_snake(snake_list):
    for block in snake_list:
        pygame.draw.rect(game_window, green, [int(block[0]), int(block[1]), block_size, block_size])

def draw_chaser(chaser_x, chaser_y):
    pygame.draw.rect(game_window, yellow, [int(chaser_x), int(chaser_y), block_size, block_size])

def game_loop():
    game_over = False
    game_close = False

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

    while not game_over:

        while game_close:
            game_window.fill(black)
            game_over_text1 = font_style.render("Game Over!", True, white)
            game_over_text2 = font_style.render("[Q] to Quit ", True, white)
            game_over_text3 = font_style.render("[P] to Play Again", True, white)
            game_window.blit(game_over_text1, [width / 4, height / 3])
            game_window.blit(game_over_text2, [width / 4, height / 3 + 50])
            game_window.blit(game_over_text3, [width / 4, height / 3 + 100])
            display_score(length_of_snake - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    elif event.key == pygame.K_p:
                        game_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if (event.key == pygame.K_LEFT or event.key == pygame.K_a) and x_change == 0:
                    x_change = -block_size
                    y_change = 0
                elif (event.key == pygame.K_RIGHT or event.key == pygame.K_d) and x_change == 0:
                    x_change = block_size
                    y_change = 0
                elif (event.key == pygame.K_UP or event.key == pygame.K_w) and y_change == 0:
                    y_change = -block_size
                    x_change = 0
                elif (event.key == pygame.K_DOWN or event.key == pygame.K_s) and y_change == 0:
                    y_change = block_size
                    x_change = 0

        if x >= width or x < 0 or y >= height or y < 0:
            game_close = True

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
            game_close = True

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