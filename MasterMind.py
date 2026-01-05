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

def starting():
    print("Game start")
    running = True
    # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")
    print("init buttons")
    Bstop = button.Button("Quit", width/2-button_width/2, height/2-button_height/2 , button_width, button_height, (255, 0, 0 ), stop)
    Bstop.draw(screen)


def stop():
    running=False
    print("Game stop")
    pygame.quit()

starting()
while running:
    for event in pygame.event.get():
        match event.type:
            case pygame.QUIT:
                running = False
                break;

            case pygame.MOUSEBUTTONDOWN:
                exit


    # RENDER YOUR GAME HERE

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)