from SceneDonut import *


WINDOW_WIDTH = 600
from GameState import *


# pygame.time.Clock().tick(60)


class SceneExcercise(pyghelpers.Scene):
    def __init__(self, window, GameState):
        self.SceneDonut = SceneDonut
        self.GameState = GameState
        self.window = window
        self.counter = 1
        self.myScore = player1.getScore()
        self.titleField = pygwidgets.DisplayText(self.window, (75, 90), 'Congratulations! You had a workout.',
                                                 fontSize=50, textColor=BLACK, width=610, justified='center')
        self.updateButtonText = pygwidgets.TextButton(window, (300, 135),
                                                      'Update Glucose', fontSize=35,
                                                      overColor=RED, downColor=LIME)
        self.diceButton = pygwidgets.ImageCollection(
            self.window, (250, 250),
            {1: "images/dice.png"}, 1,
        )

        self.healthScoreCounterText = pygwidgets.DisplayText(
            self.window, (25, 25), 'Glucose:',
            fontSize=50, textColor=BLACK)

        self.score = pygwidgets.DisplayText(
            self.window, (180, 25), "<Workout decreases glucose by -10>",
            fontSize=50, textColor=BLACK)


        self.returntoBoardText = pygwidgets.TextButton(window, (275, 500),
                                                       'Return to Board', fontSize=35,
                                                       overColor=RED, downColor=LIME)

    def getSceneKey(self):
        return SCENE_EXCERCISE


    def update(self):
        pass

    def handleInputs(self, eventsList, keyPressedList):
        for event in eventsList:
            if self.updateButtonText.handleEvent(event):
                self.counter = self.counter + 1
                decreaseScore()
                self.score.setValue(player1.getScore())
                print(player1.getScore())
                # player1.save_score()
            if self.returntoBoardText.handleEvent(event):
                self.goToScene(SCENE_GAME, self.myScore)


    def draw(self):
        self.window.fill(DANDILION_YELLOW)
        self.titleField.draw()
        self.updateButtonText.draw()
        self.healthScoreCounterText.draw()
        self.score.draw()
        self.diceButton.draw()
        self.returntoBoardText.draw()
