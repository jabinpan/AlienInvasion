import pygame.image
from pygame.sprite import Sprite
class Alien(Sprite):
    def __init__(self,screen,ai_settings):
        super(Alien,self).__init__()

        self.screen = screen
        self.ai_settings = ai_settings

        #加载外星人图像
        self.image = pygame.image.load('alien.png')
        self.rect = self.image.get_rect()

        # 每个外星人最初都在左上角处出现（）但预留了一个外星人宽度的边距
        self.rect.x = self.rect.width/2
        self.rect.y = self.rect.height/2
        # 存储外星人的准确位置
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)


    def blitme(self):
        #在指定位置显示外星人
        self.screen.blit(self.image,self.rect)