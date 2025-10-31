import pygame

# setup
pygame.init()
screen = pygame.display.set_mode((600, 800))
clock = pygame.time.Clock()
running = True

GROUND_Y = screen.get_height()

class Player:
    def __init__(self, left, top, x, y):
        self.x = x
        self.y = y
        self.left = left - self.x / 2
        self.top = top
        self.color = (255, 255, 255)
        self.v = 8

    def update(self):
        self.left += self.v
        if self.left > blackcourt.x - self.x:
            self.v *= -1
        elif self.left < blackcourt.left:
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
        pygame.draw.rect(screen, self.color, self.rectangle, width=2)


class Ball:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.radius = 15
        self.color = (255, 255, 255)
        self.vx = 6
        self.vy = 6

    def update(self):
        self.x += self.vx
        self.y += self.vy

        if self.x - self.radius < blackcourt.left or self.x + self.radius > blackcourt.x:
            self.vx *= -1

        if self.y - self.radius < blackcourt.top or self.y + self.radius > blackcourt.y:
            self.vy *= -1

        self.check_collision(playerone)
        self.check_collision(playertwo)

    def check_collision(self, player):
        ball_rect = pygame.Rect(self.x - self.radius, self.y - self.radius, self.radius * 2, self.radius * 2)

        player_rect = pygame.Rect(player.left, player.top, player.x, player.y)

        if ball_rect.colliderect(player_rect):
            self.vy *= -1

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.radius)



court = Court(10, 10, screen.get_width(), screen.get_height(), 20, (255, 255, 255))
blackcourt = Court(20, 20, screen.get_width(), screen.get_height(), 40, (0, 0, 0))

playerone = Player(screen.get_width() / 2, 40, 100, 20)
playertwo = Player(screen.get_width() / 2, screen.get_height() - 60, 100, 20)

ball = Ball(screen.get_width() / 2, screen.get_height() / 2)


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    ball.update()
    playerone.update()
    playertwo.update()


    screen.fill("black")
    court.draw(screen)
    blackcourt.draw(screen)
    ball.draw(screen)
    playerone.draw(screen)
    playertwo.draw(screen)

    pygame.draw.line(screen, (255, 255, 255), (blackcourt.left, screen.get_height() / 2),
                     (screen.get_width() - blackcourt.left, screen.get_height() / 2), 5)
    pygame.draw.circle(screen, (255, 255, 255), (screen.get_width() / 2, screen.get_height() / 2), 10)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
