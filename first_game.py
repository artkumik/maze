import pygame
from sys import exit

pygame.init()

width,height = 800,400
screen = pygame.display.set_mode((width,height),)
pygame.display.set_caption("PYGAME")

#setting framerate
clock = pygame.time.Clock()

#creating a item to place
player_surface = pygame.image.load("graphics/android.png")

#text
test_font = pygame.font.Font("font/BlackRunters.otf",50)
text_surface = test_font.render("Hello World", False, 'green')

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.blit(player_surface, (200,100))
    screen.blit(text_surface, (300,50))

    #update everything
    pygame.display.update()
    clock.tick(60)

#watched video until 42.37