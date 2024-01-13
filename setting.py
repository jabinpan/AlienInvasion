
class Setting():
    def __init__(self):
        # 初始化游戏设置
        self.screen_width = 1080
        self.screen_height = 540
        self.bg_color = (230,235,105)

        # 移动速度
        self.ship_speed_factor = 1.5

        #子弹配置
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60,60,60)
        self.bullets_allowed = 3 #将未消失的子弹数量限制为3