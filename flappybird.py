import pygame
import random

pygame.init() 

# setup screen size
SCREEN_SIZE = (284, 512)
screen = pygame.display.set_mode(SCREEN_SIZE)

# coordinates
x = 400
y = 100
y_change = 10
y_ground = 370

# images
BACKGROUND_IMG = pygame.image.load('images/background.png')
BIRD_IMG = pygame.image.load('images/bird.png')
GROUND_IMG = pygame.image.load('images/ground.png')
PIPE_END = pygame.image.load('images/pipe_end.png')
PIPE_BODY = pygame.image.load('images/pipe_body.png')

# random pipe size
y_pipe = random.randrange(50, 160, 20)
PIPE_BODY = pygame.transform.scale(PIPE_BODY, (80, y_pipe))

# color
WHITE = (255,255,255)

# overlay score text
score = 0
score_font = pygame.font.SysFont("comicsansms", 20)

def score_text(score):
    value = score_font.render(f"Your Score: {score}", True, WHITE)
    screen.blit(value, [0, 0])

GAME_OVER = False

while not GAME_OVER:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            GAME_OVER = True
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                y_change = -10
        
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                y_change = 10

    y += y_change
    x -=10

    # scrolling pipe with random sizes
    if x <= -30:
        x = 500
        y_pipe = random.randrange(50, 160, 20)
        PIPE_BODY = pygame.transform.scale(PIPE_BODY, (80, y_pipe))

    # if bird collide with ground
    if y == y_ground:
        GAME_OVER = True
    
    # if bird collide with pipe
    if x == 50:
        if (y<=y_pipe) or (y>=400-y_pipe):
            GAME_OVER = True       
        else:
            score += 1
    
    # display images
    screen.blit(BACKGROUND_IMG, (0,0))
    screen.blit(GROUND_IMG, (0,400))
    screen.blit(BIRD_IMG, (50,y))

    # upper pipe
    screen.blit(PIPE_BODY, (x,0))
    screen.blit(PIPE_END, (x,0+y_pipe))

    # lower pipe
    screen.blit(PIPE_BODY, (x,400-y_pipe))
    screen.blit(PIPE_END, (x,400-y_pipe))

    # update score
    score_text(score)

    pygame.time.delay(100)
    pygame.display.update()

pygame.quit()    