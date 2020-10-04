import random
from .snake import Snake
from .fruit import Fruit


class Game:
    WIN_WIDTH = WIN_HEIGHT = 50

    def __init__(self):
        self.game_canvas = [[0, 0, 0]
                            for _ in range(WIN_WIDTH) for _ in range(WIN_HEIGHT)]
        self.snake = Snake(self.WIN_WIDTH/2, self.WIN_HEIGHT/2, self)
        self.fruit = Fruit(random.randint(1, WIN_WIDTH),
                           random.randint(1, WIN_HEIGHT))

    def update_canvas(self):

        for pos in self.snake.pos:
            self.game_canvas[pos[0]][pos[1]] = [255, 255, 255]

        self.game_canvas[self.fruit.posx][self.fruit.posy] = [255, 0, 0]

    def endgame(self):
        return "QUIT"

    def new_fruit(self):
        del self.fruit
        self.fruit = Fruit(random.randint(1, WIN_WIDTH),
                           random.randint(1, WIN_HEIGHT))
