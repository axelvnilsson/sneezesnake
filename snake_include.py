# snake_include.py

import pygame

def handle_game_over(game_window, font_style, width, height, score):
    while True:
        game_window.fill((0, 0, 0))  # Black background
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

def handle_key_events(x_change, y_change, block_size):
    game_interrupted = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_interrupted = True
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
    return x_change, y_change, game_interrupted