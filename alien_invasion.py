import sys
import pygame
import game_functions as gf
from pygame.sprite import Group
from settings import Settings
from ship import Ship
from game_states import GameStates
from button import Button


def run_game():

    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    ship = Ship(ai_settings, screen)
    bullets = Group()
    aliens = Group()

    # 创建外星人群
    gf.create_fleet(ai_settings, screen, ship, aliens)
    pygame.display.set_caption("Alien Invasion")

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


run_game()
