import sys
import pygame
import game_functions as gf
from pygame.sprite import Group
from settings import Settings
from ship import Ship
<<<<<<< HEAD
from game_states import GameStates
from button import Button
=======
>>>>>>> 7cdb07eeeb31e9d7b836e95c3712dad19af3ad28



def run_game():

    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    ship = Ship(ai_settings, screen)
    bullets = Group()
    aliens = Group()

<<<<<<< HEAD

=======
>>>>>>> 7cdb07eeeb31e9d7b836e95c3712dad19af3ad28
    # 创建外星人群
    gf.create_fleet(ai_settings, screen, ship, aliens)
    pygame.display.set_caption("Alien Invasion")

<<<<<<< HEAD
    # 创建一个用于存储游戏统计信息实例
    stats = GameStates(ai_settings)
    # 创建Play按钮
    play_button = Button(ai_settings, screen, "Play")

    while True:
        gf.check_events(ai_settings, screen, stats,
                            play_button, ship, bullets)

        if stats.game_active:
            gf.update_bullets(ai_settings, screen, ship, aliens, bullets)
            gf.update_alien(ai_settings, stats, screen, ship, aliens, bullets)
            gf.check_events(ai_settings, screen, stats, play_button, ship, bullets)
        gf.update_screen(ai_settings, screen, stats, ship,
                         aliens, bullets, play_button)


=======
    while True:

        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        gf.update_bullets(ai_settings,screen,ship,aliens,bullets)
        gf.update_alien(ai_settings, ship,aliens)
        gf.update_screen(ai_settings, screen, ship, aliens, bullets)

        
>>>>>>> 7cdb07eeeb31e9d7b836e95c3712dad19af3ad28
run_game()
