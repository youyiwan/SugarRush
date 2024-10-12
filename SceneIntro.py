import pygwidgets
from Constants import *
import pyghelpers


class SceneIntro(pyghelpers.Scene):
    def __init__(self, MY_WINDOW):
        self.MY_WINDOW = MY_WINDOW

    def getSceneKey(self):
        return SCENE_INTRO


    def handleInputs(self, eventsList, keyPressedList):
        for event in eventsList:
            if 1==1:
                print('TEST')

    def draw(self):
        self.MY_WINDOW.fill(BLUE)

