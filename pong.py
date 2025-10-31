import pygame

# setup
pygame.init()
screen = pygame.display.set_mode((600, 1000))
clock = pygame.time.Clock()
running = True

gravity = 1
GROUND_Y = screen.get_height()

class Player:
    def __init__(self, left, top):
        x = 100
        self.left = left - x/2
        self.top = top
        self.x = 100
        self.y = 50
        self.rectangle = (self.left, self.top, self.x, self.y)
        self.color = (255, 255, 255)
    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rectangle, 0, 10)

class Court:
    def __init__(self, left, top, x, y, padding, color):
        self.left = left
        self.top = top
        self.x = x - padding
        self.y = y - padding
        self.rectangle = (self.left, self.top, self.x, self.y)
        self.color = color
    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rectangle)

class Ball:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.radius = 20
        self.color = (255, 255, 255)
        self.vy = 0

    def update(self):
        self.vy += gravity
        self.y += self.vy

        if self.y + self.radius > GROUND_Y:
            self.y = GROUND_Y - self.radius
            self.vy *= -1

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.radius)


ball = Ball(screen.get_width()/2, 0)
court = Court(10, 10, screen.get_width(), screen.get_height(), 20,(255, 255, 255))
blackcourt = Court(20 , 20, screen.get_width(), screen.get_height(), 40,(0, 0, 0))
playerone = Player(screen.get_width()/2, 10)


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    ball.update()

    screen.fill("black")
    court.draw(screen)
    blackcourt.draw(screen)
    ball.draw(screen)
    playerone.draw(screen)
    pygame.display.flip()

    clock.tick(60)

pygame.quit()
