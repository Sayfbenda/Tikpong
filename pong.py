import pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((600, 1000))
clock = pygame.time.Clock()
running = True

class Ball:
    size = 50
    color = "white"
    velocity = 1

def drawnBall():
    pygame.draw.circle(screen, (255, 255, 255), (pygame.Surface.get_width(screen)/2, pygame.Surface.get_height(screen)/2), Ball.size)


while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")

    # RENDER YOUR GAME HERE
    drawnBall()
    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60


pygame.quit()