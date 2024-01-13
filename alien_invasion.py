import sys
import pygame
from pygame.sprite import Group

from alien import Alien
from bullet import Bullet
from setting import Setting
from ship import Ship

import game_functions as gf

def run_game():
    # 初始化游戏并创建屏幕对象
    pygame.init()
    ai_setting = Setting()
    screen = pygame.display.set_mode((
        ai_setting.screen_width, ai_setting.screen_height))
    pygame.display.set_caption('Alien Invasion')
    # 实例化飞船
    ship = Ship(ai_setting,screen)
    # 创建一个存储子弹的编组
    bullets = Group()
    # 实例化存储外星人的编组
    aliens = Group()

    #创建外星人群
    gf.create_fleet(ai_setting,screen,aliens)

    # 开始游戏主循环
    while True:
        #检查事件状态
        gf.check_events(ai_setting, screen,ship,bullets)
        ship.update()
        gf.update_bullets(bullets)
        # 更新屏幕
        gf.update_screen(ai_setting, screen, ship,bullets,aliens)


run_game()