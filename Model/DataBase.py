import pygame
from pygame.locals import *
from Class.Interfase.ISolid import Solide


class DataBase(metaclass=Solide):
    def __init__(self):
        self.WINDOW_WIDTH = 1024
        self.WINDOW_HEIGHT = 600
        self.DISPLAY_HEIGHT = 300
        self.WHITE = (255, 255, 255)
        self.BLACK = (0, 0, 0)
        self.BUR = (0, 255, 255)
        self.RED = (255, 0, 0)
        self.is_playing = False
        self.__position_left_paddle = (45, 400)
        self.hud_energy = [0, 0]
        self.__position_right_paddle = (self.WINDOW_WIDTH - 55, 400)
        self.__position_ball = ()
        self.border_position = ((0, 0), (0, self.WINDOW_HEIGHT - 5), (0, 0), (self.WINDOW_WIDTH - 5, 0))
        self.border_size = ([self.WINDOW_WIDTH, 5], [self.WINDOW_WIDTH, 5],
                            [5, self.WINDOW_HEIGHT], [5, self.WINDOW_HEIGHT])

        self.energy_position = ((45, 100), (45, 500), (self.WINDOW_WIDTH - 60, 100), (self.WINDOW_WIDTH - 60, 500))
        self.energy_size = ([10, 10], [10, 10], [10, 10], [10, 10])

        self.score = [0, 0]

        self.restart = USEREVENT + 100
        self.restart_event = pygame.event.Event(self.restart)
        self.game_over = USEREVENT + 101
        self.game_over_event = pygame.event.Event(self.game_over)

        self.move_paddle = USEREVENT + 102
        self.move_paddle_event = pygame.event.Event(self.move_paddle)
        self.move_ball = USEREVENT + 103
        self.move_ball_event = pygame.event.Event(self.move_ball)
        self.energy_map = USEREVENT + 104
        self.energy_map_event = pygame.event.Event(self.energy_map)

        self.side = None

    def set_position_paddles(self, position_left, position_right):
        self.__position_left_paddle = position_left
        self.__position_right_paddle = position_right

    def get_position_paddles(self):
        return self.__position_left_paddle, self.__position_right_paddle

    def set_position_ball(self, position_ball):
        self.__position_ball = position_ball

    def get_position_ball(self):
        return self.__position_ball

    def set_score(self, i, score):
        self.score[i] += score
        if 10 == self.score[i]:
            self.game_over_event.message = i
            pygame.event.post(self.game_over_event)



