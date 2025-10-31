import pygame

# setup
pygame.init()
screen = pygame.display.set_mode((600, 1000))
clock = pygame.time.Clock()
running = True

GROUND_Y = screen.get_height()

class Player:
    def __init__(self, left, top, x, y):
        self.x = x
        self.y = y
        self.left = left - self.x/2
        self.top = top
        self.color = (255, 255, 255)
        self.v = 10
    def update(self):
        self.left += self.v
        if self.left > screen.get_width()-self.x:
            self.v *= -1
        if self.left < 0:
            self.v *= -1

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.left, self.top, self.x, self.y), 0, 10)


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
        self.v = 10

    def update(self):
        self.y += self.v

        if self.y + self.radius > screen.get_height()-blackcourt.top:
            self.v *= -1
        elif self.y + self.radius < 60:
            self.v *= -1

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.radius)


ball = Ball(screen.get_width()/2, 100)
court = Court(10, 10, screen.get_width(), screen.get_height(), 20,(255, 255, 255))
blackcourt = Court(20 , 20, screen.get_width(), screen.get_height(), 40,(0, 0, 0))
playerone = Player(screen.get_width()/2, 10, 100, 50)


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    ball.update()
    playerone.update()

    screen.fill("black")
    court.draw(screen)
    blackcourt.draw(screen)
    ball.draw(screen)
    playerone.draw(screen)
    pygame.display.flip()

    clock.tick(60)

pygame.quit()
