import pygame
from plane_sprites import *
pygame.init()

# 编写游戏代码

# 初始化位置
# hero_rect = pygame.Rect(100,500,120,125)
# print("英雄的原点 %d %d"%(hero_rect.x,hero_rect.y))
# print("英雄的尺寸 %d %d"%(hero_rect.width,hero_rect.height))
# print("%d %d"%hero_rect.size)

# 创建游戏主窗口 480*720
screen = pygame.display.set_mode((480, 700))
# 加载图像，blit绘制图像，更新屏幕显示
background = pygame.image.load("./images/background.png")
screen.blit(background, (0, 0))
pygame.display.update()


hero = pygame.image.load("./images/me1.png")
screen.blit(hero, (200, 500))
pygame.display.update()


# 创建时钟对象
clock = pygame.time.Clock()

hero_rect = pygame.Rect(200, 500, 102, 126)


enemy = GameSprite("./images/enemy1.png", 1)
enemy1 = GameSprite("./images/enemy1.png", 2)
enemy_group = pygame.sprite.Group(enemy, enemy1)
while True:

    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("游戏退出...")
            pygame.quit()
            exit()
    # 修改飞机的位置
    hero_rect.y -= 1
    # 调用blit方法绘制图像
    if hero_rect.y <= 0:
        hero_rect.y = 700
    screen.blit(background, (0, 0))
    screen.blit(hero, hero_rect)

    enemy_group.update()
    enemy_group.draw(screen)
    pygame.display.update()


pygame.quit()
