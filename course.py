# project for coursework

import pygame    # this module we need to install to use in our project
import sys       # this module we need to install to use in our project
import random    # this module we need to install to use in our project

pygame.init()

class Snake(object):      #we call the snake with class
    def init(self):
        self.length = 1  # length of snake
        self.positions = [((WIDTH/2), (HEIGHT/2))]     # snake always starts from the middle
        self.direction = random.choice([UP, DOWN, LEFT, RIGHT])  # snake goes wherever the user runs
        self.color = green  # color of the snake


    def get_head_position(self):     # for checking where the head is
        return self.positions[0]   # every time snake starts from one fixed place

    def turn(self, point):
        if self.length > 1 and (point[0] * -1, point[1] * -1) == self.direction:  # turning when it gets against the food
            return   # turn back if it is
        else:
            self.direction = point  # then eat the food

    def move(self):  # for the movement of nake
        cur = self.get_head_position()  # to find head
        x, y = self.direction   # depending on the interaction goes right, left, up or down
        new = (((cur[0] + (x * GRID_SIZE)) % WIDTH), (cur[1] + (y * GRID_SIZE)) % HEIGHT)
        if len(self.positions) > 2 and new in self.positions[2:]:  # new parts follow the head
            self.reset()
        else:
            self.positions.insert(0, new)
            if len(self.positions) > self.length:   # if positions get bigger than length
                self.positions.pop()  # when it gets too long it cuts last part of the tail

    def reset(self):
        self.length = 1   # every time it starts from one single head when it hits itself
        self.positions = [((WIDTH / 2), (HEIGHT / 2))]  # starts from the middle of the screen
        self.direction = random.choice([UP, DOWN, LEFT, RIGHT])

    def draw(self, surface):
        for p in self.positions:
            r = pygame.Rect((p[0], p[1]), (GRID_SIZE, GRID_SIZE))  # segments of body look like
            pygame.draw.rect(surface, self.color, r)
            pygame.draw.rect(surface, black, r, 1)   # makes very skinny line

    def handle_keys(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # if the user wants to quit
                pygame.quit()   # close the game
                sys.exit()   # these codes are for when the user wants to exit
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:  # if user wants to go up
                    self.turn(UP)   # go up
                elif event.key == pygame.K_DOWN:   # if user wants go down
                    self.turn(DOWN)   # go down
                elif event.key == pygame.K_LEFT:   # if user wants to go left
                    self.turn(LEFT)    # go left
                elif event.key == pygame.K_RIGHT:   # if user wants to go right
                    self.turn(RIGHT)    # go right

class Food(object):
    def __init__(self):
        self.position = (0, 0)
        self.color = red()    # color of the food
        self.randomize_position() # it appears randomly

    def randomize_position(self):
        self.position = (random.randint(0, GRID_WIDTH - 1) * GRID_SIZE, random.randint(0, GRID_HEIGHT - 1) * GRID_SIZE) # it appears randomly inside the screen

    def draw(self, surface):
        r = pygame.Rect((self.position[0], self.position[1]), (GRID_SIZE, GRID_SIZE))   # modifying accurate food for snake
        pygame.draw.rect(surface, self.color, r)    # color is going to be the same
        pygame.draw.rect(surface, black, r, 1)   # color of the food is black
def drawGrid(surface):
    for y in range(0, int(GRID_HEIGHT)):
        for x in range(0, int(GRID_WIDTH)):
            if ((x + y) % 2) == 0:
                r = pygame.Rect((x * GRID_SIZE, y * GRID_SIZE), (GRID_SIZE, GRID_SIZE))  # location of pygame
                pygame.draw.rect(surface, gray1, r)  # Grid color
            else:
                rr = pygame.Rect((x * GRID_SIZE, y * GRID_SIZE), (GRID_SIZE, GRID_SIZE))  # location of pygame
                pygame.draw.rect(surface, gray1, rr)        # overall these codes for movement of food and snake inside the screen


# Library variables for the game
WIDTH = 500    # these are the size of the screen of pygame
HEIGHT = 500  # these are the size of the screen of pygame
GRID_SIZE = 20   # makes rectangle
GRID_WIDTH = WIDTH / GRID_SIZE    # to call with one name and give size
GRID_HEIGHT = HEIGHT / GRID_SIZE   # to call with one name and give size
gray1 = (120, 120, 120)   # color for Grid size
gray2 = (170, 170, 170)
green = (20, 200, 50)
black = (0, 0, 0)  # food's color
red = (200, 40, 40)
UP = (0, -1)   # as it -y it goes to the up because it is located in upside
DOWN = (0, 1)  # as it  y it goes to the down because it is located in downside
LEFT = (-1, 0)  # as it -x it goes to the left because it is located in left side
RIGHT = (1, 0)  # as it x it goes to the right because it is located in right side
font = pygame.font.Font('freesansbold.ttf', 30)

def main():
    pygame.init()

    clock = pygame.time.Clock()    # controls the speed of the game run
    screen = pygame.display.set_mode((WIDTH, HEIGHT), 0, 32)   # define the screen

    surface = pygame.Surface(screen.get_size())  # this gets the entire size fo screen and enable it contain multiple sizes
    surface = surface.convert()
    drawGrid(surface)    # giving this drawGrid at the beginning makes the screen work right away

    snake = Snake()   # instance of the class
    food = Food()     # instance of the class

    score = 0
    while True:
        clock.tick(10)  # speed of the snake
        snake.handle_keys()      # sub functions of food
        drawGrid(surface)
        snake.move()
        if snake.get_head_position() == food.position:
            snake.length += 1
            score += 1    # when snake consumes food it becomes larger for one step
            food.randomize_position()    # food appears wherever it wants
        snake.draw(surface)
        food.draw(surface)
        screen.blit(surface, (0, 0))
        text = font.render("Score {0}".format(score), True, black)
        screen.blit(text, (5, 10))   # when user gets one food 10 marks will be given
        pygame.display.update()  # It updates the food and the snake


main()




