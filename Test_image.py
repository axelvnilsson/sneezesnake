import pygame
import sys

def init_pygame():
    pygame.init()
    size = width, height = 600, 600  # Set the size of the window
    screen = pygame.display.set_mode(size)
    return screen

def load_and_slice_image(filepath):
    image = pygame.image.load(filepath)
    image_width, image_height = image.get_size()
    tile_width = image_width // 3
    tile_height = image_height // 3
    tiles = []
    for i in range(3):  # row index
        for j in range(3):  # column index
            rect = pygame.Rect(j * tile_width, i * tile_height, tile_width, tile_height)
            tile = image.subsurface(rect)
            tiles.append(tile)
    return tiles

def main():
    screen = init_pygame()
    tiles = load_and_slice_image('Images/snake.png')  # Load and slice the image
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key in range(pygame.K_1, pygame.K_9 + 1):
                    index = event.key - pygame.K_1
                    screen.fill((0, 0, 0))  # Clear the screen with black
                    screen.blit(tiles[index], (0, 0))  # Draw the selected tile
                    pygame.display.flip()  # Update the display
        pygame.time.wait(100)  # Wait a little before the next frame

    pygame.quit()
    sys.exit()

if __name__ == '__main__':
    main()
