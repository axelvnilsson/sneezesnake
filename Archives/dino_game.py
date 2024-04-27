import pygame
import random

pygame.init()

WIDTH, HEIGHT = 800, 600
FPS = 30

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Offline Dino Game")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)

# Dino variables
dino_width = 50
dino_height = 50
dino_pos = [50, HEIGHT - dino_height - 50]
dino_jump = False
dino_jump_height = 150

# Cactus variables
cactus_width = 50
cactus_height = 50
cactus_speed = 10
cacti = []

# Score
score = 0
font = pygame.font.SysFont(None, 30)

def draw_dino():
    pygame.draw.rect(screen, WHITE, (dino_pos[0], dino_pos[1], dino_width, dino_height))

def draw_cacti():
    for cactus in cacti:
        pygame.draw.rect(screen, GREEN, (cactus[0], cactus[1], cactus_width, cactus_height))

def move_cacti():
    for cactus in cacti:
        cactus[0] -= cactus_speed
        if cactus[0] < 0:
            cacti.remove(cactus)
            global score
            score += 1

def collision_detection():
    for cactus in cacti:
        if dino_pos[0] < cactus[0] + cactus_width and dino_pos[0] + dino_width > cactus[0] and dino_pos[1] < cactus[1] + cactus_height:
            return True
    return False

clock = pygame.time.Clock()

running = True
while running:
    screen.fill(BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and not dino_jump:
                dino_jump = True

    if dino_jump:
        dino_pos[1] -= 5
        dino_jump_height -= 5
        if dino_jump_height <= 0:
            dino_jump = False
            dino_jump_height = 150
    
    if not dino_jump and dino_pos[1] < HEIGHT - dino_height - 50:
        dino_pos[1] += 5

    if random.randint(0, 100) < 2:
        cacti.append([WIDTH, HEIGHT - cactus_height - 50])

    move_cacti()

    if collision_detection():
        running = False

    draw_dino()
    draw_cacti()

    text = font.render("Score: " + str(score), True, WHITE)
    screen.blit(text, (10, 10))

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
