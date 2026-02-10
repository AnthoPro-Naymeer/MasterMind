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

from email.policy import default
from re import L
from typing import Sequence
from click import option
import pygame
from config import *
import Button as button
import random

pygame.init()
smallfont = pygame.font.SysFont(font, font_size)
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
running = True
global menu
menu = 'start'

global sequence
sequence = []
global test_sequence
test_sequence = []

def play():
    print("Play")
    global menu
    menu = 'play'

def quit():
    global running
    running = False
    print("Quit")


def player_count_selection(player_count):
    print("Select player count")
    if player_count == 'Solo':
        print("Solo mode selected"+"\n")
        print("Generating sequense"+"\n")
        for i in range(nb_pawn):
            sequence.append(random.randint(0,possible_pawn))
            print(sequence)
    else:
        print("Duo mode selected")


Bstart = button.Button("Start", width/2-button_width/2, height/2-button_height-30 , button_width, button_height, (0, 255, 0 ), play)
Bstop = button.Button("Quit", width/2-button_width/2, height/2-button_height+30, button_width, button_height, (255, 0, 0 ), quit)
Bsolo = button.Button("Solo", width/2-button_width/2, height/2-button_height-30 , button_width, button_height, (0, 255, 0 ), lambda : player_count_selection('Solo'))
Bduo = button.Button("Duo", width/2-button_width/2, height/2-button_height+30, button_width, button_height, (0, 255, 0 ), lambda : player_count_selection('Duo'))
global test_button
test_button = []

def Bgess(nb=nb_pawn):
    """generate the button for playing, each button match a possible pawn

    nb:
        nb (int, optional): number of button. Defaults to nb_pawn.
    """
    for i in range(1, nb):
        test_button[i] = button.Button(i, width/nb_pawn+2-button_width/2+width*i/nb_pawn+2, height/2-button_height, button_width, button_height, (0, 0, 0 ), lambda : )


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        Bstart.handle_event(event)
        Bstop.handle_event(event)
        Bsolo.handle_event(event)
        Bduo.handle_event(event)

    screen.fill("purple")
    match menu:
        case 'start':
            Bstart.draw(screen)
            Bstart.Is_active()
            Bstop.draw(screen)
            Bstop.Is_active()
        case 'play':
            Bsolo.draw(screen)
            Bsolo.Is_active()
            Bduo.draw(screen)
            Bduo.Is_active()

        case 'solo':


        case _:
            pygame.display.flip()
    
            


    pygame.display.flip()
    clock.tick(60)

pygame.quit()