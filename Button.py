import pygame
smallfont = pygame.font.SysFont(None,35)

class Button:

    def __init__(self, name, rect, color, action):
        self.name = name
        self.rect = pygame.Rect(rect)
        self.color = color
        self.action = action

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect, border_radius=5)
        # superimposing the text onto our button
        text = smallfont.render(self.name , True , (0,0,0))

        screen.blit(text, self.rect)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.action()