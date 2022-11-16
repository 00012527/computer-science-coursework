# project for coursework

import pygame
import sys
import random   # these three modules we are going to use to complete our project

pygame.init()

class Snake(object):
    def __init__(self):
        self.length = 1  # length of snake
        self.positions = [((WIDTH/2), (HEIGHT/2))]
        self.direction = random.choice([UP, DOWN, LEFT, RIGHT])
        self.color = green


class Food(object):
    pass

def drawGrid(surface):
    for y in range(0, int(GRID_HEIGHT)):
        for x in range(0, int(GRID_WIDTH)):
            if ((x + y) % 2) == 0:
                rect = pygame.Rect((x * GRID_SIZE, y * GRID_SIZE), (GRID_SIZE, GRID_SIZE))  # location of pygame
                pygame.draw.rect(surface, gray1, rect)
            else:
                rect = pygame.Rect((x * GRID_SIZE, y * GRID_SIZE), (GRID_SIZE, GRID_SIZE))  # location of pygame
                pygame.draw.rect(surface, gray1, rect)


# Library variables for the game
WIDTH = 500
HEIGHT = 500  # these are the size of the screen of pygame
GRID_SIZE = 20
GRID_WIDTH = WIDTH / GRID_SIZE
GRID_HEIGHT = HEIGHT / GRID_SIZE
gray1 = (120, 120, 120)
gray2 = (170, 170, 170)
green = (0, 255, 0)
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

def main():
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((WIDTH, HEIGHT), 0, 32)

    surface = pygame.Surface(screen.get_size())  # this gets the entire size fo screen
    surface = surface.convert()

    drawGrid(surface)

    snake = Snake()
    food = Food()

    score = 0
    while True:
        clock.ticket(10)
        # sub functions of food
        drawGrid(surface)

        pygame.display.update()


main()



