import copy
import pygame
from sys import exit


# display function
def print_m(M):
    for i in range(len(M)):
        for j in range(len(M[0])):
            surface_background_rect.y = 30 * i
            surface_background_rect.x = 30 * j
            screen.blit(surface_background, surface_background_rect)
            if M[i][j] == 1:
                surface_alive_rect.y = 30 * i
                surface_alive_rect.x = 30 * j
                screen.blit(surface_alive, surface_alive_rect)


# iterator function
def update_m(M):
    M_1 = copy.deepcopy(M)
    for i in range(len(M_1)):
        for j in range(len(M_1[0])):
            num_of_nei = -M[i][j]
            for k in range(max(0, i - 1), min(len(M_1), i + 2)):
                for l in range(max(0, j - 1), min(len(M_1[0]), j + 2)):
                    num_of_nei += M_1[k][l]
            if num_of_nei < 2 or num_of_nei > 3:
                M[i][j] = 0
            if num_of_nei == 3:
                M[i][j] = 1
    return M


pygame.init()
size = [20, 20] # size of the board
field = [[0 for j in range(size[1])] for i in range(size[0])] # generating matrix to save board states
screen = pygame.display.set_mode((30 * size[0], 30 * size[1]))
pygame.display.set_caption("Game of life")
Font = pygame.font.Font("Assets/Pixeltype.ttf", 30)
game_active = False
setup = True
ani_speed = 0
clock = pygame.time.Clock()

surface_background = pygame.image.load("Assets/Background.png").convert_alpha()
surface_background_rect = surface_background.get_rect()
surface_alive = pygame.image.load("Assets/Alive.png").convert_alpha()
surface_alive_rect = surface_alive.get_rect()

# starting screen
screen.fill("black")
start_message = Font.render("Choose your starting fields, press space to continue ", False, (200, 200, 200))
start_message_rect = start_message.get_rect(center = (16 * size[0], 16 * size[1]))
screen.blit(start_message, start_message_rect)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # exit window
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            game_active = True
        if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN and game_active:
            setup = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            position = event.pos
            field[position[1] // 30][position[0] // 30] += 1       # finding field in Matrix corresponding to mouse
            field[position[1] // 30][position[0] // 30] %= 2       # click location. Works even while the game runs :)

    if game_active:
        if setup:
            print_m(field)
            start_message = Font.render("Enter to start the Game", False, "Red")
            start_message_rect = start_message.get_rect(center = ((15 * size[0], 20)))
            screen.blit(start_message, start_message_rect)
        else:
            print_m(field)
            ani_speed += 1
            ani_speed = ani_speed % 10              # speed of generation change
            if ani_speed == 0:
                field = update_m(field)
    else:
        pass
    pygame.display.update()
    clock.tick(60)
