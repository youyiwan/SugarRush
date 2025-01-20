import pygame
from Constants import *
import json

def decreaseScore():
    player1.score = player1.score - 10

def increaseScore():
    player1.score = player1.score + 15

def decreaseScoreOverDose():
    player1.score = player1.score - 30


class GameState:
    def __init__(self):
        self.score = 100

    def getScore(self):
        return self.score

    # def increase(self, points):
    #     """Increase score by a given number of points."""
    #     self.score += points

    def reset(self, score):
        """Reset the score to 0."""
        score = 0

    def load_score(self):
        try:
            with open('score.json', 'r') as file:
                rawData = json.load(file)
                data = rawData['score']
                # print(data)
                # valueScore = data.values()
                # player1.score = data.get('score', 0)  # Default to 0 if no score is found
        except FileNotFoundError:
            player1.score = 0  # If the file doesn't exist, start with score 0
        return data

    def save_score(self):
        with open('score.json', 'w') as file:
            json.dump({'score': player1.score}, file)


player1 = GameState()
