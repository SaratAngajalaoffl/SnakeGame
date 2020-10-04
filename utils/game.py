from .snake import Snake
from .fruit import Fruit


class Game:
    WIN_WIDTH = WIN_HEIGHT = 600

    def __init__(self):
        self.game_canvas = [[0, 0, 0]
                            for _ in range(WIN_WIDTH) for _ in range(WIN_HEIGHT)]
        self.snake = Snake(self.WIN_WIDTH/2, self.WIN_HEIGHT/2)
        