import pygame
from pygame.constants import QUIT
from plane_sprites import *
screen_rect = pygame.Rect(0, 0, 480, 700)


class PlaneGame(object):
    def create_sprites(self):
        pass

    def __init__(self) -> None:
        super().__init__()
        print("游戏初始化")
        self.screen = pygame.display.set_mode(screen_rect.size)
        self.clock = pygame.time.Clock()
        self.create_sprites()

    def start_game(self):
        print("游戏开始...")

        while True:
            self.clock.tick(60)
            self.event_handler()
            self.check_collide()
            self.update_sprites()
            pygame.display.update()

    def event_handler(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                PlaneGame.game_over()

    def check_collide(self):
        pass

    def update_sprites(self):
        pass

    @staticmethod
    def game_over():
        print("游戏结束")
        pygame.quit()
        exit()


if __name__ == '__main__':
    game = PlaneGame()
    game.start_game()
