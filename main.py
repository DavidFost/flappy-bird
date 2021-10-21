import pygame
import random


pygame.init()

SCREEN = pygame.display.set_mode((500,750))
BACKGROUND_IMAGE = pygame.image.load('background.jpg')

model_image = pygame.image.load('flappy.png')
model_x = 50
model_y = 300
model_y_change = 0

obstacle_width = 70
obstacle_height = (random.randint(150,450))
obstacle_color = (211,253,117)
obstacle_x_change = -4
obstacle_x = 500

score = 0
font = pygame.font.Font('arcade.ttf',32)

def display_score(score):
    display = font.render("Score: "+ str(score), True, (255,255,255))
    SCREEN.blit(display, (10,10))

def detect_collision(obstacle_x, obstacle_height, model_y, bottom_obstacle_height,char_y):
    if obstacle_x >= 50 and obstacle_x <= 50+64:
        if model_y <= obstacle_height or model_y >= (bottom_obstacle_height-64):
            return True
    if char_y <= 0:
        return True
    if char_y >= 574:
        return True
    return False

def display_obstacle(height):
    pygame.draw.rect(SCREEN, obstacle_color,(obstacle_x, 0, obstacle_width, height))
    bottom_y = height+200
    bottom_height = 635 - bottom_y
    pygame.draw.rect(SCREEN, obstacle_color,(obstacle_x, bottom_y, obstacle_width, bottom_height))

def display_model(x,y):
    SCREEN.blit(model_image, (x,y))

playing = True

while playing:
    SCREEN.fill((0,0,0))
    SCREEN.blit(BACKGROUND_IMAGE,(0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            playing = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                model_y_change = -6
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                model_y_change = 3
    model_y += model_y_change
    if model_y <= 0:
        model_y = 0
    if model_y >= 574:
        model_y = 574

    obstacle_x += obstacle_x_change
    if obstacle_x <= -10:
        obstacle_x = 500
        obstacle_height = random.randint(200,400)
        score  += 1
    display_obstacle(obstacle_height)

    collided = detect_collision(obstacle_x,obstacle_height,model_y,obstacle_height+200, model_y)
    if collided:
        pygame.quit()

    display_model(model_x, model_y)
    display_score(score)
    pygame.display.update()


pygame.QUIT()

