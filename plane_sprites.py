import pygame
import random
from plane_main import screen_rect

# 创建定时器常量


class GameSprite(pygame.sprite.Sprite):

    def __init__(self, image_name, speed=1):
        super().__init__()
        self.image = pygame.image.load(image_name)
        self.rect = self.image.get_rect()
        self.speed = speed

    def update(self):
        self.rect.y += self.speed


class Background(GameSprite):
    """
    游戏背景精灵
    """

    def __init__(self, is_alt=False):
        super().__init__(image_name="./images/background.png")
        if is_alt:
            self.rect.y = -self.rect.height

    def update(self):
        super().update()
        if self.rect.y >= screen_rect.height:
            self.rect.y = -self.rect.height


class Enemy(GameSprite):

    def __init__(self):
        super().__init__("./images/enemy1.png")
        self.speed = random.randint(1, 5)
        self.rect.bottom = 0
        self.rect.x = random.randint(0, (screen_rect.width-self.rect.width))

    def update(self):
        super().update()
        if self.rect.y >= screen_rect.height:
            # print("飞出屏幕，需要从精灵组中删除...")
            self.kill()

    def __del__(self):
        # print("敌机挂了 %s" % self.rect)
        pass


class Hero(GameSprite):
    """
    英雄精灵
    """

    def __init__(self):
        super().__init__("./images/me1.png", 0)
        self.speed1 = 0
        self.speed2 = 0
        self.rect.centerx = screen_rect.centerx
        self.rect.bottom = screen_rect.bottom - 120
        self.bullets = pygame.sprite.Group()

    def update(self):
        if self.rect.right <= screen_rect.right and self.rect.x >= 0:
            self.rect.x += self.speed1
        elif self.rect.x < 0:
            self.rect.x = 0
        else:
            self.rect.right = screen_rect.right

        if self.rect.bottom <= screen_rect.bottom and self.rect.y >= 0:
            self.rect.y += self.speed2
        elif self.rect.y < 0:
            self.rect.y = 0
        else:
            self.rect.bottom = screen_rect.bottom

    def fire(self):
        print("发射子弹...")
        for i in (0, 1, 2):
            bullet = Bullet()
            bullet.rect.bottom = self.rect.y - i * 20
            bullet.rect.centerx = self.rect.centerx
            self.bullets.add(bullet)


class Bullet(GameSprite):
    def __init__(self):
        super().__init__("./images/bullet1.png", -2)

    def update(self):
        super().update()
        if self.rect.bottom < 0:
            self.kill()

    def __del__(self):
        # print("子弹被销毁")
        pass
