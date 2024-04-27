import pygame
import config as con
import global_value as g

# initialize font module
pygame.font.init()

# setup fonts
p = pygame.font.Font(None,con.P_FONT_SIZE)
h1 = pygame.font.Font(None,con.H1_FONT_SIZE)
h2 = pygame.font.Font(None,con.H2_FONT_SIZE)
h3 = pygame.font.Font(None,con.H3_FONT_SIZE)

class Text():
    def __init__(self,position,text,antialias,color,background=None,font='p'):
        self.position_x, self.position_y = position
        self.text = text
        self.antialias = antialias
        self.color = color
        self.background = background
        self.font = font
        if self.font == 'h1':
            self.surface = h1.render(self.text,self.antialias,self.color,self.background)
        elif self.font == 'h2':
            self.surface = h2.render(self.text,self.antialias,self.color,self.background)
        elif self.font == 'h3':
            self.surface = h3.render(self.text,self.antialias,self.color,self.background)
        else:
            self.surface = p.render(self.text,self.antialias,self.color,self.background)
        self.width, self.height = self.surface.get_size()
    
    def position_center(self):
        self.position_x = con.SCREEN_CENTER[0]-self.width/2
        self.position_y = con.SCREEN_CENTER[1]-self.height/2

    def draw(self,screen):
        screen.blit(self.surface,(self.position_x,self.position_y))
    
class Button(Text):
    def __init__(self,position,text,antialias,color,background=None,font='p'):
        super().__init__(position,text,antialias,color,background,font)
    
    def is_clicked(self,x,y):
        if self.position_x < x < self.position_x+self.width and self.position_y < y < self.position_y+self.height:
            return True
        else:
            return False