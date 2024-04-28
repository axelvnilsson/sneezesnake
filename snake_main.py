import pygame
import random

from snake_include import splash_screen, game_over_screen, clear_screen, draw_snake, draw_food, draw_chaser, handle_key_events, display_score

# Initialize Pygame and other game settings
pygame.init()
width, height = 800, 600
game_window = pygame.display.set_mode((width, height))
pygame.display.set_caption('Snake Game')
clock = pygame.time.Clock()
font_style = pygame.font.SysFont(None, 50)
block_size = 20
high_score = 0  # Global high score

# Colors
blue = (0, 0, 255)
white = (255, 255, 255)
green = (0, 255, 0)
red = (255, 0, 0)
black = (0, 0, 0)
yellow = (255, 255, 0)

def sneeze_snake():
    global high_score  # Declare high_score as global to ensure it retains value across game sessions

    game_active = True
    while game_active:
        # Game state variables
        game_over = False
        game_start = True

        # Game settings
        update_player = 1
        setting_background_color = blue

        # Snake parameters
        snake_x = width / 2
        snake_y = height / 2
        snake_x_change = 0
        snake_y_change = 0
        snake_speed = 15
        snake_list = []
        snake_length = 1
        snake_color = green

        # Chaser parameters
        chaser_x = random.randrange(0, width - block_size, block_size)
        chaser_y = random.randrange(0, height - block_size, block_size)
        chaser_speed = 5
        chaser_color = yellow

        # Game parameters
        score = 0
        score_color = white
        last_speed_increase = 0

        # Initial position of the food
        food_x = round(random.randrange(0, width - block_size) / block_size) * block_size
        food_y = round(random.randrange(0, height - block_size) / block_size) * block_size
        food_color = red

        while not game_over:
            if game_start:
                quit_the_game = splash_screen(game_window, font_style, width, height, score, high_score)
                if quit_the_game:
                    game_active = False
                    break
                game_start = False

            snake_x_change, snake_y_change, game_interrupted = handle_key_events(snake_x_change, snake_y_change, block_size, update_player)
            if game_interrupted:
                break

            if snake_x >= width or snake_x < 0 or snake_y >= height or snake_y < 0:
                game_over = True

            snake_x += snake_x_change
            snake_y += snake_y_change

            # Chaser movement logic
            if chaser_x < snake_x:
                chaser_x += chaser_speed
            elif chaser_x > snake_x:
                chaser_x -= chaser_speed

            if chaser_y < snake_y:
                chaser_y += chaser_speed
            elif chaser_y > snake_y:
                chaser_y -= chaser_speed

            snake_head = [snake_x, snake_y]
            snake_list.append(snake_head)
            if len(snake_list) > snake_length:
                del snake_list[0]

            for block in snake_list[:-1]:
                if block == snake_head:
                    game_over = True

            if abs(snake_x - chaser_x) < block_size and abs(snake_y - chaser_y) < block_size:
                game_over = True

            if score >= 10 and score % 10 == 0 and score != last_speed_increase:
                chaser_speed += 2
                last_speed_increase = score

            if snake_x == food_x and snake_y == food_y:
                food_x = round(random.randrange(0, width - block_size) / block_size) * block_size
                food_y = round(random.randrange(0, height - block_size) / block_size) * block_size
                snake_length += 1
                score += 1

            if score > high_score:
                high_score = score

            clear_screen(game_window, setting_background_color)
            draw_food(game_window, block_size, food_color, food_x, food_y)
            draw_snake(game_window, block_size, snake_color, snake_list)
            draw_chaser(game_window, block_size, chaser_color, chaser_x, chaser_y)
            display_score(game_window, font_style, score_color, score)
            pygame.display.update()
            clock.tick(snake_speed)

        if not game_over:
            continue  # If the game is not over, continue without interruption

        restart = game_over_screen(game_window, font_style, width, height, score)
        if not restart:
            game_active = False  # Exit the loop and end the game

    pygame.quit()
    quit()

sneeze_snake()