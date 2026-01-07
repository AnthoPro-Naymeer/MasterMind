"""
MasterMind Game

A personal project to practice various programming concepts such as:
- Game logic design
- User interface (UI) implementation with Pygame
- Event handling and state management

The goal is to implement the classic MasterMind game while learning
how to structure a project and separate logic from UI.

Author: Naymeer
"""

import pygame
from config import *
import Button as button
import random

pygame.init()
smallfont = pygame.font.SysFont(font, font_size)
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
running = True


def play():
    print("Play")
    Bsolo.draw(screen)
    Bduo.draw(screen)

def quit():
    global running
    running = False
    print("Quit")


def player_count_selection(player_count):
    print("Select player count")
    if player_count == 'Solo':
        print("Solo mode selected")
    else:
        print("Duo mode selected")


Bstart = button.Button("Start", width/2-button_width/2, height/2-button_height-30 , button_width, button_height, (0, 255, 0 ), play)
Bstop = button.Button("Quit", width/2-button_width/2, height/2-button_height+30, button_width, button_height, (255, 0, 0 ), quit)
Bsolo = button.Button("Solo", width/2-button_width/2, height/2-button_height-30 , button_width, button_height, (0, 255, 0 ), player_count_selection('Solo'))
Bduo = button.Button("Duo", width/2-button_width/2, height/2-button_height+30, button_width, button_height, (0, 255, 0 ), player_count_selection('Duo'))

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        Bstart.handle_event(event)
        Bstop.handle_event(event)
        Bsolo.handle_event(event)
        Bduo.handle_event(event)

    screen.fill("purple")

    Bstart.draw(screen)
    Bstop.draw(screen)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()