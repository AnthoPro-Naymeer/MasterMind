"""
Docstring for Button
-------------

Contains the Button class for Pygame.

Each button has:
- position and size
- color
- displayed text
- action triggered on click

The class handles drawing and mouse click detection.
"""

import pygame
from config import *

class Button:

    def __init__(self, name, x, y , width, height, color, action):
        self.name = name
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.rec = pygame.Rect(self.x, self.y, self.width+font_size/2, self.height)
        self.color = color
        self.font = pygame.font.SysFont(font, font_size)
        self.action = action

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rec, border_radius = 10)

        # superimposing the text onto our button
        text = self.font.render(self.name, True, (0, 0, 0))

        center_text_x = (self.width-font_size)/3
        center_text_y = (self.height-font_size)/2


        screen.blit(text, (self.x+center_text_x, self.y+center_text_y, self.width, self.height+5))

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.action()
