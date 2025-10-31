import pygame

# setup
pygame.init()
screen = pygame.display.set_mode((600, 1000))
clock = pygame.time.Clock()
running = True

GRAVITY = 0.5
GROUND_Y = 950

class Court:
    def __init__(self, x, y):
        self.x = x
        self.x = y
        self.rectangle = 0

class Ball:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.radius = 50
        self.color = (255, 255, 255)
        self.vy = 0

    def update(self):
        self.vy += GRAVITY
        self.y += self.vy

        if self.y + self.radius > GROUND_Y:
            self.y = GROUND_Y - self.radius
            self.vy *= -0.7

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.radius)


ball = Ball(300, 100)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    ball.update()

    screen.fill("black")
    ball.draw(screen)
    pygame.display.flip()

    clock.tick(60)

pygame.quit()
