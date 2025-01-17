import pygame
import pygwidgets
from Constants import *
from SceneIntro import *
from SceneGame import *
from SceneDonut import *
from SceneExcercise import *
from GameState import *
from SceneEnd import *

pygame.init()
sugarRush = pygame.display.set_mode((GAME_WINDOW_WIDTH, GAME_WINDOW_HEIGHT))


sugarRushSceneList = [SceneIntro(sugarRush), SceneGame(sugarRush, GameState), SceneDonut(sugarRush, GameState), SceneExcercise(sugarRush, GameState), SceneEnd(sugarRush)]

oSceneMgr = pyghelpers.SceneMgr(sugarRushSceneList, 30)

oSceneMgr.run()