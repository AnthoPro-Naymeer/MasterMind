"""
MasterMind Game

A personal project to practice various programming concepts such as:
- Game logic design
- User interface (UI) implementation with Pygame
- Event handling and state management

The goal is to implement the classic MasterMind game while learning
how to structure a project and separate logic from UI.

Author: [Your Name]
"""

import pygame
import random

nb_gess = 10
nb_pawn = 4

pygame.init()
smallfont = pygame.font.SysFont(None,35)
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
running = True


import Button as button

def starting():
    print("Game start")
    running = True
    # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")
    print("init buttons")
    Bstop = button.Button("Quit",(150, 120, 100, 50), (0, 200, 100), stop)
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