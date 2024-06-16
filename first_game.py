import pygame
from sys import exit

pygame.init()

width,height = 800,400
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("PYGAME")

#setting framerate
clock = pygame.time.Clock()

#creating a item to place
player_surface = pygame.image.load("graphics/android.png").convert_alpha()
player_surface = pygame.transform.scale(player_surface,(200,200))
player_rect = player_surface.get_rect(midleft = (100,250))

#text
test_font = pygame.font.Font("font/BlackRunters.otf",50)
text_surface = test_font.render("Hello World", False, 'green')

ball_surface = pygame.image.load("graphics/ball.png").convert_alpha()
ball_surface = pygame.transform.scale(ball_surface, (100, 100))
ball_rect = ball_surface.get_rect(midbottom = (600,300)) #transforming the size of the ball


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.fill("black") #prevents smearing, can remove if bg object
    screen.blit(text_surface, (300,50))

    screen.blit(player_surface, player_rect)

    ball_rect.x -= 4
    if ball_rect.right <= 0: ball_rect.left = 800
    screen.blit(ball_surface, ball_rect)

    #collision between ball and player
    if player_rect.colliderect(ball_rect):
        print("ball")

    #mouse 
    mouse_pos = pygame.mouse.get_pos()
    if player_rect.collidepoint(mouse_pos):
        print(pygame.mouse.get_pressed())

    #update everything
    pygame.display.flip()
    clock.tick(60)

#watched video until 1 15 39