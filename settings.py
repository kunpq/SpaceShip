class Settings():
    """存储游戏中所有设置的类"""

    def __init__(self):
        """初始化游戏的设置"""
        # 屏幕设置
        self.screen_width = 1300
        self.screen_height = 700
        self.bg_color = (230, 230, 230)
<<<<<<< HEAD

        #飞船设置
        self.ship_limit=3
=======
>>>>>>> 7cdb07eeeb31e9d7b836e95c3712dad19af3ad28
        self.ship_speed_factor = 1.5

        # 子弹设置
        self.bullet_speed_factor = 3
<<<<<<< HEAD
        self.bullet_width = 30
=======
        self.bullet_width = 300
>>>>>>> 7cdb07eeeb31e9d7b836e95c3712dad19af3ad28
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 3
        
        # 外星人设置
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 100
        #fleet_direction:1向右,-1向左
        self.fleet_direction = 1
        
<<<<<<< HEAD
        
=======
>>>>>>> 7cdb07eeeb31e9d7b836e95c3712dad19af3ad28
        