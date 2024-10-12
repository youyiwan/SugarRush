import pygame
import pygwidgets
from Constants import *
from SceneIntro import *

pygame.init()
sugarRush = pygame.display.set_mode((GAME_WINDOW_WIDTH, GAME_WINDOW_HEIGHT))


sugarRushSceneList = [SceneIntro(sugarRush)]

oSceneMgr = pyghelpers.SceneMgr(sugarRushSceneList, 30)

oSceneMgr.run()