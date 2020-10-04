import pygame
from pygame.locals import *
import sys
from utils.game import Game

RES = 500


def main():

    pygame.init()

    win = pygame.display.set_mode((RES, RES))
    surface = pygame.Surface((RES, RES))
    surface = surface.convert()
    clock = pygame.time.Clock()
    game = Game()

    while True:
        clock.tick(120)
        if game.update_canvas() == "QUIT":
            pygame.quit()
            sys.exit()
        handle_events(game)
        drawgrid(surface, game)
        win.blit(surface, (0, 0))
        pygame.display.update()


def handle_events(game):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                game.snake.update_direction("UP")
            if event.key == pygame.K_a:
                game.snake.update_direction("LEFT")
            if event.key == pygame.K_s:
                game.snake.update_direction("DOWN")
            if event.key == pygame.K_d:
                game.snake.update_direction("RIGHT")


def drawgrid(surface, game):
    bg = pygame.Rect((0, 0), (RES, RES))
    pygame.draw.rect(surface, (0, 0, 0), bg)
    for i, x in enumerate(game.game_canvas):
        for j, y in enumerate(x):
            r = pygame.Rect((i*int(RES/game.WIN_WIDTH), j*int(RES/game.WIN_HEIGHT)),
                            (int(RES/game.WIN_WIDTH), int(RES/game.WIN_HEIGHT)))
            pygame.draw.rect(surface, (y[0], y[1], y[2]), r)


main()
