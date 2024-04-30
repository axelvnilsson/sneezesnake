import pygame
import random

def init_game():
    pygame.init()
    game_width, game_height = 800, 600
    screen = pygame.display.set_mode((game_width, game_height))
    pygame.display.set_caption('Snake Game')
    colors = {
        "black": (0, 0, 0),
        "white": (255, 255, 255),
        "red": (255, 0, 0),
        "green": (0, 255, 0)
    }
    return screen, game_width, game_height, colors

def load_game_assets(game_width, game_height):
    food_x = random.randint(0, game_width - 20)
    food_y = random.randint(0, game_height - 20)
    return food_x, food_y

def create_random_snake(game_width, game_height, block_size=20, num_blocks=15):
    directions = [(0, -block_size), (block_size, 0), (0, block_size), (-block_size, 0)]
    snake_positions = []
    x = random.randint(0, (game_width - block_size) // block_size) * block_size
    y = random.randint(0, (game_height - block_size) // block_size) * block_size
    snake_positions.append((x, y))
    
    for _ in range(num_blocks - 1):
        valid_directions = directions.copy()
        while valid_directions:
            dx, dy = random.choice(valid_directions)
            nx, ny = snake_positions[-1][0] + dx, snake_positions[-1][1] + dy
            if (0 <= nx < game_width) and (0 <= ny < game_height) and ((nx, ny) not in snake_positions):
                snake_positions.append((nx, ny))
                break
            valid_directions.remove((dx, dy))
        if not valid_directions:
            break  # If no valid directions, stop adding segments

    return snake_positions


def handle_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
    return True

def move_food(keys, food_x, food_y):
    if keys[pygame.K_RIGHT]:
        food_x += 20
    if keys[pygame.K_LEFT]:
        food_x -= 20
    if keys[pygame.K_DOWN]:
        food_y += 20
    if keys[pygame.K_UP]:
        food_y -= 20
    return food_x, food_y

def check_boundaries(food_x, food_y, game_width, game_height):
    food_x = max(0, min(game_width - 20, food_x))
    food_y = max(0, min(game_height - 20, food_y))
    return food_x, food_y

def draw_elements(screen, colors, food_x, food_y, snake_positions):
    screen.fill(colors["black"])
    pygame.draw.rect(screen, colors["red"], (food_x, food_y, 20, 20))
    for x, y in snake_positions:
        pygame.draw.rect(screen, colors["green"], (x, y, 20, 20))

def main():
    screen, game_width, game_height, colors = init_game()
    food_x, food_y = load_game_assets(game_width, game_height)
    snake_positions = create_random_snake(game_width, game_height)
    clock = pygame.time.Clock()
    snake_timer = 0
    running = True

    while running:
        running = handle_events()
        keys = pygame.key.get_pressed()
        food_x, food_y = move_food(keys, food_x, food_y)
        food_x, food_y = check_boundaries(food_x, food_y, game_width, game_height)
        snake_timer += clock.get_time()
        if snake_timer > 1000:  # Every 1000 milliseconds, reset the timer and create a new snake
            snake_positions = create_random_snake(game_width, game_height)
            snake_timer = 0
        draw_elements(screen, colors, food_x, food_y, snake_positions)
        pygame.display.update()
        clock.tick(40)

    pygame.quit()

if __name__ == "__main__":
    main()
