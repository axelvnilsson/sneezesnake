import pygame
import random
from snake_include import ticker_load_facts, ticker_setup, draw_ticker

def init_game():
    pygame.init()
    game_width, game_height = 800, 600
    screen = pygame.display.set_mode((game_width, game_height))
    pygame.display.set_caption('Snake Game')
    colors = {
        "black": (0, 0, 0),
        "white": (255, 255, 255),
        "red": (255, 0, 0)
    }
    return screen, game_width, game_height, colors

def load_game_assets(game_width, game_height):
    food_x = random.randint(0, game_width - 20)
    food_y = random.randint(0, game_height - 20)
    ticker_font = pygame.font.Font(None, 32)
    ticker_tape = ticker_load_facts()
    ticker_color = (255,255,255)
    text, text_rect = ticker_setup(ticker_tape, ticker_font, ticker_color, game_width, game_height)
    return food_x, food_y, ticker_font, text, text_rect

def handle_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
    return True

def move_food(keys, food_x, food_y):
    if keys[pygame.K_RIGHT]:
        food_x += 5
    if keys[pygame.K_LEFT]:
        food_x -= 5
    if keys[pygame.K_DOWN]:
        food_y += 5
    if keys[pygame.K_UP]:
        food_y -= 5
    return food_x, food_y

def check_boundaries(food_x, food_y, game_width, game_height):
    food_x = max(0, min(game_width - 20, food_x))
    food_y = max(0, min(game_height - 20, food_y))
    return food_x, food_y

def draw_elements(screen, colors, food_x, food_y, text, text_rect):
    screen.fill(colors["black"])
    pygame.draw.rect(screen, colors["red"], (food_x, food_y, 20, 20))
    text, text_rect = draw_ticker(screen, text, text_rect)
    return text, text_rect

def main():
    screen, game_width, game_height, colors = init_game()
    food_x, food_y, ticker_font, text, text_rect = load_game_assets(game_width, game_height)
    clock = pygame.time.Clock()
    running = True

    while running:
        running = handle_events()
        keys = pygame.key.get_pressed()
        food_x, food_y = move_food(keys, food_x, food_y)
        food_x, food_y = check_boundaries(food_x, food_y, game_width, game_height)
        text, text_rect = draw_elements(screen, colors, food_x, food_y, text, text_rect)
        pygame.display.update()
        clock.tick(40)

    pygame.quit()

if __name__ == "__main__":
    main()
