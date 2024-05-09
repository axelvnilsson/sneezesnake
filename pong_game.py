import pygame
import sys
import os

# Constants
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
PADDLE_WIDTH, PADDLE_HEIGHT = 15, 90
BALL_SIZE = 20
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
FPS = 60
NET_WIDTH = 4
NET_HEIGHT = 20
NET_COLOR = WHITE
NET_POSITION_X = SCREEN_WIDTH // 2 - NET_WIDTH // 2  # Center of the screen

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

    def move(self, paddles, score1, score2):
        self.rect.x += self.dx
        self.rect.y += self.dy
        # Bounce off the top and bottom of the screen
        if self.rect.top <= 0 or self.rect.bottom >= SCREEN_HEIGHT:
            self.dy = -self.dy
        # Check for collisions with the paddles
        for paddle in paddles:
            if self.rect.colliderect(paddle.rect):
                self.dx = -self.dx
                sound_file = "Sounds/Bounce.mp3"
                os.system(f"afplay {sound_file}&")
                break
        # Reset the ball if it goes off the screen
        # Reset the ball if it goes off the screen
        if self.rect.left <= 0 or self.rect.right >= SCREEN_WIDTH:
            self.reset()

    def reset(self):
        self.rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
        self.dx = -self.dx  # Change direction to make the game fairer

    def draw(self):
        pygame.draw.ellipse(screen, WHITE, self.rect)

def draw_score(screen, color, score1, score2):
    font = pygame.font.SysFont(None, 36)
    # Calculate the position to center the text at 1/4 the screen width
    one_quarter_x = SCREEN_WIDTH // 4
    three_quarter_x = SCREEN_WIDTH // 4 * 3

    # Render the text for score1
    score1_text = font.render(f"Player One: {score1}", True, color, BLACK)
    text_width, text_height = font.size(f"Player one: {score1}")
    # Adjust the position to center the text at one_quarter_x
    score1_position_x = one_quarter_x - (text_width // 2)
    screen.blit(score1_text, (score1_position_x, 10))

    # Render the text for score2
    score2_text = font.render(f"Player Two: {score2}", True, color, BLACK)
    text_width, text_height = font.size(f"Player Two: {score2}")
    # Adjust the position to center the text at one_quarter_x
    score2_position_x = three_quarter_x - (text_width // 2)
    screen.blit(score2_text, (score2_position_x, 10))

def draw_net():
    # Draw the net
    for y in range(0, SCREEN_HEIGHT, NET_HEIGHT * 2):
        pygame.draw.rect(screen, NET_COLOR, (NET_POSITION_X, y, NET_WIDTH, NET_HEIGHT))

def main():
    paddle1 = Paddle(30, SCREEN_HEIGHT // 2 - PADDLE_HEIGHT // 2)
    paddle2 = Paddle(SCREEN_WIDTH - 30 - PADDLE_WIDTH, SCREEN_HEIGHT // 2 - PADDLE_HEIGHT // 2)
    ball = Ball(SCREEN_WIDTH // 2 - BALL_SIZE // 2, SCREEN_HEIGHT // 2 - BALL_SIZE // 2)
    running = True
    score1 = 0
    score2 = 0

    while running:
        for event in pygame.event.get():
            if event.type is pygame.QUIT:
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

        ball.move([paddle1, paddle2], score1, score2)
        # score1 = score1 +1 
        # score2 = score2 +1
        if ball.rect.left == 10:
            score2 += 1
        if ball.rect.right == SCREEN_WIDTH - 10:
            score1 += 1

        screen.fill(BLACK)
        draw_net()  # Draw the net on the screen
        paddle1.draw()
        paddle2.draw()
        ball.draw()
        draw_score(screen, WHITE, score1, score2)

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
