import pygwidgets
from Constants import *
import pyghelpers


class SceneIntro(pyghelpers.Scene):
    def __init__(self, MY_WINDOW):
        self.MY_WINDOW = MY_WINDOW

        self.startButtonText = pygwidgets.TextButton(MY_WINDOW, (325, 0),
                                                     'Start Game', fontSize=35,
                                                     overColor=RED, downColor=LIME)
        self.introImage = pygwidgets.Image(MY_WINDOW, (0, 0), 'images/intro.png')


    def getSceneKey(self):
        return SCENE_INTRO


    def handleInputs(self, eventsList, keyPressedList):
        for event in eventsList:
            if self.startButtonText.handleEvent(event):
                self.goToScene(SCENE_GAME)

    def draw(self):
        self.MY_WINDOW.fill(BLUE)
        self.introImage.draw()
        self.startButtonText.draw()
