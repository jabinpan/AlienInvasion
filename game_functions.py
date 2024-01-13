import sys
import pygame

from alien import Alien
from bullet import Bullet


def check_events(ai_settings, screen,ship,bullets):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event,ai_settings, screen,ship,bullets)
            check_keydown_events(event,ai_settings, screen,ship,bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(ship,event)

def check_keydown_events(event,ai_settings, screen,ship,bullets):
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            ship.moving_left = True
        elif event.key == pygame.K_RIGHT:
            ship.moving_right = True
        elif event.key == pygame.K_SPACE :
            fire_bullets(bullets,ai_settings,screen, ship)
        elif event.key == pygame.K_ESCAPE:
            sys.exit()
def check_keyup_events(ship,event):
    if event.type == pygame.KEYUP:
        if event.key == pygame.K_RIGHT:
            ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            ship.moving_left = False
def update_screen(ai_settings, screen,ship,bullets,aliens):
    '''更新屏幕上的图像，并切换到新屏幕'''
    #每次循环都时都重绘屏幕
    screen.fill(ai_settings.bg_color)
    ship.blitme()
    # 在飞船和外星人后面重绘所有子弹
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    aliens.draw(screen)

    #让最新绘制的屏幕可见
    pygame.display.flip()

def update_bullets(bullets):
    '''更新子弹位置，并删除消失的子弹'''
    bullets.update()
    # 删除消失的子弹
    for bullet in bullets.copy():  # 在for循环中不应该从列表或编组中删除条目，因此必须遍历编组的副本
        if bullet.rect.bottom < 0:
            bullets.remove(bullet)

def fire_bullets(bullets,ai_settings,screen, ship):
    if len(bullets) <= ai_settings.bullets_allowed:
        newBullet = Bullet(ai_settings, screen, ship)
        bullets.add(newBullet)

def create_fleet(ai_setting,screen,aliens):
    '''创建一个外星人群'''
    # 计算一行最大能生成的外星人数量
    number_aliens_x = get_number_aliens(ai_setting,screen)
    # 创建第一行外星人
    for alien_number in range(number_aliens_x):
        create_alien(ai_setting,screen,aliens,alien_number)

def get_number_aliens(ai_setting,screen):
    '''计算一行最大能生成的外星人数量'''
    newAlien = Alien(ai_setting, screen)
    alien_width = newAlien.rect.width
    available_space_x = ai_setting.screen_width - (2 * newAlien.rect.width)
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x

def create_alien(ai_setting,screen,aliens,alien_number):
    newAlien = Alien(ai_setting, screen)
    newAlien.x = newAlien.rect.width / 2 + 2 * newAlien.rect.width * alien_number
    newAlien.rect.x = newAlien.x
    aliens.add(newAlien)