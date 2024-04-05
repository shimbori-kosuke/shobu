import pygame

class Button:
    def __init__(self, pos, size, pad, color, txtcolor, action=None, text="Button"):
        self.x = pos[0]
        self.y = pos[1]
        self.pad = pad
        self.color = color
        self.font = pygame.font.SysFont(None, size)
        self.text = self.font.render(text, True, txtcolor)
        self.action = action
        self.button = pygame.Rect(pos, (self.text.get_width() + pad, self.text.get_height() + pad))
        self.button_bottom = pygame.Rect(pos, (self.button.width, self.button.height + 5))

    def update(self):
        self.button.top = self.y

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.button.collidepoint(event.pos):
                    self.action()

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.button)
        screen.blit(self.text, (self.x + self.pad / 2, self.y + self.pad / 2))