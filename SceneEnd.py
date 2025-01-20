# The Play scene
# The player chooses among rock, paper, or scissors

import pygwidgets
import pyghelpers
import sys
import pygame
from pygame import event, font
# from pygame.examples.go_over_there import screen

WINDOW_WIDTH = 600
from GameState import *


# pygame.time.Clock().tick(60)


class SceneEnd(pyghelpers.Scene):
    def __init__(self, window):
        self.GameState = GameState
        self.window = window
        self.counter = 1
        self.myScore = player1.getScore()
        self.titleField = pygwidgets.DisplayText(self.window, (75, 90), 'The End.',
                                                 fontSize=50, textColor=BLACK, width=610, justified='center')
        self.updateButtonText = pygwidgets.TextButton(window, (300, 135),
                                                      'Update Glucose', fontSize=35,
                                                      overColor=RED, downColor=LIME)


        self.healthScoreCounterText = pygwidgets.DisplayText(
            self.window, (25, 25), 'Glucose:',
            fontSize=50, textColor=BLACK)

        self.score = pygwidgets.DisplayText(
            self.window, (180, 25), "",
            fontSize=50, textColor=BLACK)

        self.updateButtonText = pygwidgets.TextButton(window, (300, 135),
                                                      'Get Final Score', fontSize=35,
                                                      overColor=RED, downColor=LIME)

        self.returntoBoardText = pygwidgets.TextButton(window, (275, 500),
                                                       'Return to Board', fontSize=35,
                                                       overColor=RED, downColor=LIME)

    def getSceneKey(self):
        return SCENE_END


    def update(self):
        pass

    def handleInputs(self, eventsList, keyPressedList):
        for event in eventsList:
            if self.updateButtonText.handleEvent(event):
                # self.counter = self.counter + 1
                # increaseScore()
                self.score.setValue(player1.getScore())
                print(player1.getScore())
                # player1.save_score()
            if self.returntoBoardText.handleEvent(event):
                self.goToScene(SCENE_GAME)

    # No need to include update method, defaults to inherited one which does nothing

    def draw(self):
        self.window.fill(DANDILION_YELLOW)
        self.titleField.draw()
        self.updateButtonText.draw()
        self.healthScoreCounterText.draw()
        self.score.draw()
        # self.diceButton.draw()
        self.returntoBoardText.draw()
