import pyghelpers
import pygwidgets
from Constants import *
import pygame

MY_WINDOW = pygame.display.set_mode((GAME_WINDOW_WIDTH, GAME_WINDOW_HEIGHT))


TWO_HUNDRED_INTERVAL = 200


def draw_cubes(MY_WINDOW):
    for row in range(ROWS):
        for col in range(row % 2, ROWS, 2):
            pygame.draw.rect(MY_WINDOW, YELLOW, (row * SQUARE_SIZE, col * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
class SceneGame(pyghelpers.Scene):
    def __init__(self, MY_WINDOW):
        self.step = 0
        self.food = None
        self.foodButton = None
        self.MY_WINDOW = MY_WINDOW
        self.counter = 0
        self.playerScore = 0


    def fill_EvenBoard(self):
        i = 0
        j = -200
        iter = 0
        for row in range(ROWS):
            j = j + TWO_HUNDRED_INTERVAL
            if j == 800:
                j = 0
                if iter == 6:
                    break
                elif iter < 6:
                    iter = iter + 1
            for col in range(row % 2, ROWS, 2):  # start at 0, stop at 8, step 2
                self.food = pygwidgets.Image(MY_WINDOW, (i, j), 'images/' + str(i) + '.png', nickname=None)
                self.food.draw()
                i = i + TWO_HUNDRED_INTERVAL
                if i == 800:
                    i = 0
                    break

    def fill_OddBoard(self):
        m = 100  # columns
        n = -100  # Rows
        for row in range(ROWS):
            n = n + TWO_HUNDRED_INTERVAL
            for col in range(row % 2, ROWS, 2):  # start at 0, stop at 8, step 2
                self.food = pygwidgets.Image(MY_WINDOW, (m, n), 'images/' + str(m) + '.png', nickname=None)
                self.food.draw()
                if m == 700:
                    m = 100
                    break
                elif m < 700:
                    m = m + TWO_HUNDRED_INTERVAL

    def fill_OuterCols(self):
        for x in range(OUTER_COLS):
            if x > 6:
                MY_WINDOW.fill(BLACK)


    def getSceneKey(self):
        return SCENE_GAME


    def handleInputs(self, eventsList, keyPressedList):
        for event in eventsList:
            if 1==1:
                self.goToScene(SCENE_GAME)

    def draw(self):
        self.MY_WINDOW.fill(BLUE)
        draw_cubes(MY_WINDOW)
        self.fill_OddBoard()
        self.fill_EvenBoard()