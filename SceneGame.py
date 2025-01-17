import pyghelpers
import pygwidgets
from Constants import *
import pygame
import random

MY_WINDOW = pygame.display.set_mode((GAME_WINDOW_WIDTH, GAME_WINDOW_HEIGHT))


TWO_HUNDRED_INTERVAL = 200


def draw_cubes(MY_WINDOW):
    for row in range(ROWS):
        for col in range(row % 2, ROWS, 2):
            pygame.draw.rect(MY_WINDOW, PINK, (row * SQUARE_SIZE, col * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
class SceneGame(pyghelpers.Scene):
    def __init__(self, MY_WINDOW):
        self.step = 0
        self.food = None
        self.foodButton = None
        self.MY_WINDOW = MY_WINDOW
        self.counter = 0
        self.playerScore = 0

        self.playerbutton = pygwidgets.CustomButton(self.MY_WINDOW, (0, 700),
                                                    up='images/player.png',
                                                    down='images/player.png',
                                                    over='images/player.png')

        self.donut_1Button = pygwidgets.CustomButton(self.MY_WINDOW, (100, 700),
                                                    up='images/donut_1.png',
                                                    down='images/donut_1.png',
                                                    over='images/donut_1.png')

        self.donut_2Button = pygwidgets.CustomButton(self.MY_WINDOW, (300, 700),
                                                    up='images/donut_2.png',
                                                    down='images/donut_2.png',
                                                    over='images/donut_2.png')

        self.donut_3Button = pygwidgets.CustomButton(self.MY_WINDOW, (200, 600),
                                                    up='images/donut_3.png',
                                                    down='images/donut_3.png',
                                                    over='images/donut_3.png')

        self.donut_4Button = pygwidgets.CustomButton(self.MY_WINDOW, (100, 500),
                                                    up='images/donut_4.png',
                                                    down='images/donut_4.png',
                                                    over='images/donut_4.png')

        self.donut_5Button = pygwidgets.CustomButton(self.MY_WINDOW, (600, 400),
                                                    up='images/donut_5.png',
                                                    down='images/donut_5.png',
                                                    over='images/donut_5.png')

        self.donut_6Button = pygwidgets.CustomButton(self.MY_WINDOW, (100, 300),
                                                    up='images/donut_6.png',
                                                    down='images/donut_6.png',
                                                    over='images/donut_6.png')

        self.donut_7Button = pygwidgets.CustomButton(self.MY_WINDOW, (500, 300),
                                                    up='images/donut_7.png',
                                                    down='images/donut_7.png',
                                                    over='images/donut_7.png')

        self.donut_8Button = pygwidgets.CustomButton(self.MY_WINDOW, (400, 200),
                                                    up='images/donut_8.png',
                                                    down='images/donut_8.png',
                                                    over='images/donut_8.png')

        self.donut_9Button = pygwidgets.CustomButton(self.MY_WINDOW, (200, 400),
                                                    up='images/donut_9.png',
                                                    down='images/donut_9.png',
                                                    over='images/donut_9.png')

        self.donut_10Button = pygwidgets.CustomButton(self.MY_WINDOW, (700, 300),
                                                    up='images/donut_10.png',
                                                    down='images/donut_10.png',
                                                    over='images/donut_10.png')

        self.donut_11Button = pygwidgets.CustomButton(self.MY_WINDOW, (200, 200),
                                                    up='images/donut_11.png',
                                                    down='images/donut_11.png',
                                                    over='images/donut_11.png')

        self.finishButton = pygwidgets.CustomButton(self.MY_WINDOW, (0, 0),
                                                    up='images/finish.png',
                                                    down='images/finish.png',
                                                    over='images/finish.png')

        self.workout1Button = pygwidgets.CustomButton(self.MY_WINDOW, (500, 100),
                                                    up='images/workout_2.png',
                                                    down='images/workout_2.png',
                                                    over='images/workout_2.png')

        self.workout2Button = pygwidgets.CustomButton(self.MY_WINDOW, (100, 100),
                                                    up='images/workout_2.png',
                                                    down='images/workout_2.png',
                                                    over='images/workout_2.png')

        self.workout3Button = pygwidgets.CustomButton(self.MY_WINDOW, (300, 300),
                                                    up='images/workout_3.png',
                                                    down='images/workout_3.png',
                                                    over='images/workout_3.png')

        self.workout4Button = pygwidgets.CustomButton(self.MY_WINDOW, (400, 400),
                                                    up='images/workout_4.png',
                                                    down='images/workout_4.png',
                                                    over='images/workout_4.png')
        self.workout5Button = pygwidgets.CustomButton(self.MY_WINDOW, (500, 500),
                                                    up='images/workout_5.png',
                                                    down='images/workout_5.png',
                                                    over='images/workout_5.png')
        self.workout6Button = pygwidgets.CustomButton(self.MY_WINDOW, (600, 600),
                                                    up='images/workout_6.png',
                                                    down='images/workout_6.png',
                                                    over='images/workout_6.png')
        self.workout7Button = pygwidgets.CustomButton(self.MY_WINDOW, (700, 700),
                                                    up='images/workout_7.png',
                                                    down='images/workout_7.png',
                                                    over='images/workout_7.png')
        self.workout8Button = pygwidgets.CustomButton(self.MY_WINDOW, (0, 200),
                                                    up='images/workout_8.png',
                                                    down='images/workout_8.png',
                                                    over='images/workout_8.png')
        self.workout9Button = pygwidgets.CustomButton(self.MY_WINDOW, (0, 400),
                                                    up='images/workout_9.png',
                                                    down='images/workout_9.png',
                                                    over='images/workout_9.png')
        self.workout10Button = pygwidgets.CustomButton(self.MY_WINDOW, (0, 600),
                                                    up='images/workout_10.png',
                                                    down='images/workout_10.png',
                                                    over='images/workout_10.png')

    # def fill_EvenBoard(self):
    #     i = 0
    #     j = -200
    #     iter = 0
    #     for row in range(ROWS):
    #         j = j + TWO_HUNDRED_INTERVAL
    #         if j == 800:
    #             j = 0
    #             if iter == 6:
    #                 break
    #             elif iter < 6:
    #                 iter = iter + 1
    #         for col in range(row % 2, ROWS, 2):  # start at 0, stop at 8, step 2
    #             self.food = pygwidgets.Image(MY_WINDOW, (i, j), 'images/' + str(i) + '.png', nickname=None)
    #             self.food.draw()
    #             i = i + TWO_HUNDRED_INTERVAL
    #             if i == 800:
    #                 i = 0
    #                 break

    # def fill_OddBoard(self):
    #     m = 100  # columns
    #     n = -100  # Rows
    #     for row in range(ROWS):
    #         n = n + TWO_HUNDRED_INTERVAL
    #         for col in range(row % 2, ROWS, 2):  # start at 0, stop at 8, step 2
    #             self.food = pygwidgets.Image(MY_WINDOW, (m, n), 'images/' + str(m) + '.png', nickname=None)
    #             self.food.draw()
    #             if m == 700:
    #                 m = 100
    #                 break
    #             elif m < 700:
    #                 m = m + TWO_HUNDRED_INTERVAL

    def fill_OuterCols(self):
        for x in range(OUTER_COLS):
            if x > 6:
                MY_WINDOW.fill(BLACK)


    def getSceneKey(self):
        return SCENE_GAME


    def handleInputs(self, eventsList, keyPressedList):
        for event in eventsList:
            if self.playerbutton.handleEvent(event):
                jump = random.randint(1, 6)
                print('The dice roll is ')
                print(jump)
                for i in range(jump):
                    if 0 <= self.counter < 7 or 15 < self.counter < 23 or 31 < self.counter < 39 or 48 <= self.counter < 55:
                        self.playerbutton.moveX(100)
                        print(self.playerbutton.getLoc())
                        self.counter = self.counter + 1
                        print(self.counter)
                    elif 8 <= self.counter <= 14 or 23 < self.counter < 31 or 39 < self.counter < 47 or 55 < self.counter < 63:
                        self.playerbutton.moveX(-100)
                        self.counter = self.counter + 1
                        print(self.playerbutton.getLoc())
                        print(self.counter)
                    elif self.counter == 7 or self.counter == 15 or self.counter == 23 or self.counter == 31 or self.counter == 39 or self.counter == 47 or self.counter == 55:
                        self.playerbutton.moveY(-100)
                        self.counter = self.counter + 1
                        print(self.playerbutton.getLoc())
                        print(self.counter)
                    elif self.counter >= 63:
                        print(self.playerbutton.getLoc())

    def draw(self):
        self.MY_WINDOW.fill(BLUE)
        draw_cubes(MY_WINDOW)
        # self.fill_OddBoard()
        # self.fill_EvenBoard()
        self.playerbutton.draw()
        self.donut_1Button.draw()
        self.donut_2Button.draw()
        self.donut_3Button.draw()
        self.donut_4Button.draw()
        self.donut_5Button.draw()
        self.donut_6Button.draw()
        self.donut_7Button.draw()
        self.donut_8Button.draw()
        self.donut_9Button.draw()
        self.donut_10Button.draw()
        self.donut_11Button.draw()
        self.workout1Button.draw()
        self.workout2Button.draw()
        self.workout3Button.draw()
        self.workout4Button.draw()
        self.workout5Button.draw()
        self.workout6Button.draw()
        self.workout7Button.draw()
        self.workout8Button.draw()
        self.workout9Button.draw()
        self.workout10Button.draw()
        self.finishButton.draw()
