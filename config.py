"""
Docstring for config
-------------

Contains global constants and parameters for the MasterMind game.

Main variables:
- nb_gess : maximum number of guesses
- nb_pawn : number of pawns per row
- width : window width
- height : window height
- button_width : default button width
- button_height : default button height
- font : default font (to be initialized after pygame.init())
- font_size : default font size
"""

import pygame

nb_gess = 10
nb_pawn = 4
width = 800
height = 600
button_width = 75
button_height = 50
font = 'Helvetica'
font_size = 35