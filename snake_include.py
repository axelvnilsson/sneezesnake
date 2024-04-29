# snake_include.py

import pygame
import random

def display_score(game_window, font_style, score_color, score):
    score_text = font_style.render("Score: " + str(score), True, score_color)
    game_window.blit(score_text, [0, 0])

def draw_snake(game_window, block_size, snake_color, snake_list):
    for block in snake_list:
        pygame.draw.rect(game_window, snake_color, [int(block[0]), int(block[1]), block_size, block_size])

def draw_chaser(game_window, block_size, chaser_color, chaser_x, chaser_y):
    pygame.draw.rect(game_window, chaser_color, [int(chaser_x), int(chaser_y), block_size, block_size])

def draw_food(game_window, block_size, food_color, food_x, food_y):
    pygame.draw.rect(game_window, food_color, [food_x, food_y, block_size, block_size])

def clear_screen(game_window, background_color):
    game_window.fill(background_color)  # Fill the screen with the background color

def splash_screen(game_window, font_style, width, height, score, high_score):
    while True:
        clear_screen(game_window,(0, 0, 0))  # Black background
        splash_screen_text1 = font_style.render("This is a better version of snake!", True, (255, 255, 255))
        splash_screen_text2 = font_style.render("It is called Sneeze Snake", True, (255, 255, 255))
        splash_screen_text3 = font_style.render("By Axel Nilsson", True, (255, 255, 255))
        splash_screen_text4 = font_style.render("[S] to  play!", True, (255, 255, 255))
        splash_screen_text5 = font_style.render("[Q] to  quit!", True, (255, 255, 255))
        splash_screen_text6 = font_style.render("Your highscore is: " + str(high_score), True, (255, 255, 255))
        game_window.blit(splash_screen_text1, [width / 4, height / 3])
        game_window.blit(splash_screen_text2, [width / 4, height / 3 + 50])
        game_window.blit(splash_screen_text3, [width / 4, height / 3 + 100])
        game_window.blit(splash_screen_text4, [width / 4, height / 3 + 150])
        game_window.blit(splash_screen_text5, [width / 4, height / 3 + 200])
        game_window.blit(splash_screen_text6, [width / 4, height / 3 + 250])
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    return True  # Quit the game
                elif event.key == pygame.K_s:
                    return False  # to play the game
                

def game_over_screen(game_window, font_style, width, height, score):
    while True:
        # clear_screen(game_window,(0, 0, 0))  # Black background
        game_over_text1 = font_style.render("Game Over!", True, (255, 255, 255))
        game_over_text2 = font_style.render("[Q] to Quit ", True, (255, 255, 255))
        game_over_text3 = font_style.render("[P] to Play Again", True, (255, 255, 255))
        game_window.blit(game_over_text1, [width / 4, height / 3])
        game_window.blit(game_over_text2, [width / 4, height / 3 + 50])
        game_window.blit(game_over_text3, [width / 4, height / 3 + 100])

        # Display score
        score_text = font_style.render("Score: " + str(score), True, (255, 255, 255))
        game_window.blit(score_text, [0, 0])

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    return False  # Quit the game
                elif event.key == pygame.K_p:
                    return True  # Play again

# This function handles the key events for the snake game
# It allows the snake to move in the direction of the key pressed
# It also allows the player to quit the game by closing the window
# It returns the updated x and y changes and a boolean value that indicates if the game is interrupted
# The snake_x_change and snake_y_change variables are used to update the x and y coordinates of the snake
# The block_size variable is used to determine the distance the snake moves in each step
# The player variable is used to determine which player is controlling the snake
# The player variable can be 1 or 2
# The player 1 controls the snake using the arrow keys
# The player 2 controls the snake using the WASD keys
def handle_key_events(snake_x_change, snake_y_change, block_size, player):
    game_interrupted = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_interrupted = True
        if event.type == pygame.KEYDOWN:
            if player == 1:
                if event.key == pygame.K_LEFT and snake_x_change == 0:
                    snake_x_change = -block_size
                    snake_y_change = 0
                elif event.key == pygame.K_RIGHT and snake_x_change == 0:
                    snake_x_change = block_size
                    snake_y_change = 0
                elif event.key == pygame.K_UP and snake_y_change == 0:
                    snake_y_change = -block_size
                    snake_x_change = 0
                elif event.key == pygame.K_DOWN and snake_y_change == 0:
                    snake_y_change = block_size
                    snake_x_change = 0
            elif player == 2:
                if event.key == pygame.K_a and snake_x_change == 0:
                    snake_x_change = -block_size
                    snake_y_change = 0
                elif event.key == pygame.K_d and snake_x_change == 0:
                    snake_x_change = block_size
                    snake_y_change = 0
                elif event.key == pygame.K_w and snake_y_change == 0:
                    snake_y_change = -block_size
                    snake_x_change = 0
                elif event.key == pygame.K_s and snake_y_change == 0:
                    snake_y_change = block_size
                    snake_x_change = 0
    return snake_x_change, snake_y_change, game_interrupted

def ticker_load_facts():
    # Load snake facts from file and create a single long string with all facts in random order
    with open('snake_facts.txt', 'r') as file:
        facts = file.readlines()
    random.shuffle(facts)
    ticker_tape = " ... ".join([fact.strip() for fact in facts]) + " ... "
    return ticker_tape

def ticker_setup(ticker_tape, ticker_font, ticker_color, screen_width, screen_height):
    # Initialize ticker with the long text
    text = ticker_font.render(ticker_tape, True, ticker_color)
    text_rect = text.get_rect()
    text_rect.left = screen_width  # Start off right edge of screen
    text_rect.bottom = screen_height  # Position at the bottom of the screen
    return text, text_rect

def ticker_update(text, text_rect):
    # Move text left
    text_rect.x -= 2
    return text, text_rect
