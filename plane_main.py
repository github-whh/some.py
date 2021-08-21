import pygame
import os
from pygame.constants import QUIT
from plane_sprites import *
pygame.init()
screen_rect = pygame.Rect(0, 0, 480, 700)
CREATE_ENEMY_EVENT = pygame.USEREVENT
HERO_FIRE_EVENT = pygame.USEREVENT + 1


class PlaneGame(object):
    def create_sprites(self):
        background1 = Background()
        background2 = Background(True)
        self.back_group = pygame.sprite.Group(background1, background2)
        self.enemy_group = pygame.sprite.Group()
        self.hero = Hero()
        self.hero_group = pygame.sprite.Group(self.hero)

    def __init__(self) -> None:
        super().__init__()
        print("游戏初始化")
        self.screen = pygame.display.set_mode(screen_rect.size)
        self.clock = pygame.time.Clock()
        self.create_sprites()
        self.score = 0
        pygame.time.set_timer(CREATE_ENEMY_EVENT, 1000)
        pygame.time.set_timer(HERO_FIRE_EVENT, 500)

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
            elif event.type == CREATE_ENEMY_EVENT:
                print("敌机出厂")
                # 创建敌机精灵，并添加到精灵组中
                enemy = Enemy()
                self.enemy_group.add(enemy)
            elif event.type == HERO_FIRE_EVENT:
                self.hero.fire()

            # elif event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
            #     print("向右移动")
            # elif event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
            #     print("向左移动")
        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_RIGHT]:
            self.hero.speed1 = 2
            self.hero.speed2 = 0
        elif keys_pressed[pygame.K_LEFT]:
            self.hero.speed1 = -2
            self.hero.speed2 = 0
        elif keys_pressed[pygame.K_UP]:
            self.hero.speed2 = -2
            self.hero.speed1 = 0
        elif keys_pressed[pygame.K_DOWN]:
            self.hero.speed2 = 2
            self.hero.speed1 = 0
        else:
            self.hero.speed1 = 0
            self.hero.speed2 = 0

    def check_collide(self):
        flag = pygame.sprite.groupcollide(
            self.hero.bullets, self.enemy_group, True, True)
        if len(flag) > 0:
            self.score += 1
        enemies = pygame.sprite.spritecollide(
            self.hero, self.enemy_group, True)
        if len(enemies) > 0:
            self.game_over()

    def update_sprites(self):
        self.back_group.update()
        self.back_group.draw(self.screen)
        self.enemy_group.update()
        self.enemy_group.draw(self.screen)
        self.hero_group.update()
        self.hero_group.draw(self.screen)
        self.hero.bullets.update()
        self.hero.bullets.draw(self.screen)

    def game_over(self):

        os.system("cls")
        print("游戏结束")
        print("你一共摧毁了", self.score, "架飞机")
        pygame.quit()
        exit()


if __name__ == '__main__':
    game = PlaneGame()
    game.start_game()
