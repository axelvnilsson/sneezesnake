import pygame
import sys

# Constants
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
PADDLE_WIDTH, PADDLE_HEIGHT = 15, 90
BALL_SIZE = 20
WHITE = (255, 255, 255)
FPS = 60

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Pong')
clock = pygame.time.Clock()

class Paddle:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, PADDLE_WIDTH, PADDLE_HEIGHT)

    def move(self, y):
        self.rect.y += y
        # Prevent the paddle from moving out of the screen
        self.rect.y = max(self.rect.y, 0)
        self.rect.y = min(self.rect.y, SCREEN_HEIGHT - PADDLE_HEIGHT)

    def draw(self):
        pygame.draw.rect(screen, WHITE, self.rect)

class Ball:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, BALL_SIZE, BALL_SIZE)
        self.dx = 5  # Horizontal movement
        self.dy = 5  # Vertical movement

    def move(self, paddles):
        self.rect.x += self.dx
        self.rect.y += self.dy
        # Bounce off the top and bottom of the screen
        if self.rect.top <= 0 or self.rect.bottom >= SCREEN_HEIGHT:
            self.dy = -self.dy
        # Check for collisions with the paddles
        for paddle in paddles:
            if self.rect.colliderect(paddle.rect):
                self.dx = -self.dx
                break

    def reset(self):
        self.rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
        self.dx = -self.dx  # Change direction to make the game fairer

    def draw(self):
        pygame.draw.ellipse(screen, WHITE, self.rect)

def main():
    paddle1 = Paddle(30, SCREEN_HEIGHT // 2 - PADDLE_HEIGHT // 2)
    paddle2 = Paddle(SCREEN_WIDTH - 30 - PADDLE_WIDTH, SCREEN_HEIGHT // 2 - PADDLE_HEIGHT // 2)
    ball = Ball(SCREEN_WIDTH // 2 - BALL_SIZE // 2, SCREEN_HEIGHT // 2 - BALL_SIZE // 2)
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            paddle1.move(-5)
        if keys[pygame.K_s]:
            paddle1.move(5)
        if keys[pygame.K_UP]:
            paddle2.move(-5)
        if keys[pygame.K_DOWN]:
            paddle2.move(5)
        if keys[pygame.K_SPACE]:
            ball.reset()

        ball.move([paddle1, paddle2])

        screen.fill(0)
        paddle1.draw()
        paddle2.draw()
        ball.draw()

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
