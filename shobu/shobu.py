import logging
import pygame
import copy

import field as fd
import config as con
import global_value as g

# set loggger
logger = logging.getLogger("logger")
logger.setLevel(logging.DEBUG)

# pygame setup
pygame.init()
screen = pygame.display.set_mode(con.SCREEN_SIZE)
clock = pygame.time.Clock()
running = True

# setup fonts
p = pygame.font.Font(None,con.P_FONT_SIZE)
h1 = pygame.font.Font(None,con.H1_FONT_SIZE)
h2 = pygame.font.Font(None,con.H2_FONT_SIZE)
h3 = pygame.font.Font(None,con.H3_FONT_SIZE)

# create font class
player_black = h3.render("BLACK",True,"black")
player_white = h3.render("WHITE",True,"black")
undo_button = h2.render("Undo Move",True,"black","white")
confirm_skelton = h2.render("Next  Turn  ",True,"dark grey","light grey") 
confirm_button = h2.render("Next  Turn  ",True,"black","white")

# sizes of buttons (width, height)
undo_button_size = undo_button.get_size()
confirm_button_size = confirm_button.get_size()

def undo_button_is_clicked(x,y):
    if con.UNDO_BUTTON_POS[0] < x < con.UNDO_BUTTON_POS[0]+undo_button_size[0] and con.UNDO_BUTTON_POS[1] < y < con.UNDO_BUTTON_POS[1]+undo_button_size[1]:    
        return True
    else:
        return False

def confirm_button_is_clicked(x,y):
    if con.CONFIRM_BUTTON_POS[0] < x < con.CONFIRM_BUTTON_POS[0]+confirm_button_size[0] and con.CONFIRM_BUTTON_POS[1] < y < con.CONFIRM_BUTTON_POS[1]+confirm_button_size[1]:
        return True
    else:
        return False

# func for left click
def left_click(x,y):
    # if field is clicked
    if fd1.is_clicked(x,y):
        print("field1 is clicked")
        fd1.click(x,y)
    elif fd2.is_clicked(x,y):
        print("field2 is clicked")
        fd2.click(x,y)
    elif fd5.is_clicked(x,y):
        print("field5 is clicked")
        fd5.click(x,y)
    elif fd6.is_clicked(x,y):
        print("field6 is clicked")
        fd6.click(x,y)
    elif undo_button_is_clicked(x,y):
            undo_move()
    elif confirm_button_is_clicked(x,y):
        if g.active_move():
            confirm_move()

def undo_move():
    g.passive = True
    g.select = True
    g.winner = 0
    fd1.field = copy.deepcopy(g.previous_fields[0])
    fd2.field = copy.deepcopy(g.previous_fields[1])
    fd5.field = copy.deepcopy(g.previous_fields[2])
    fd6.field = copy.deepcopy(g.previous_fields[3])


def confirm_move():
    if g.active_move():
        g.passive = True
        g.select =True
        g.turn += 1
        g.previous_fields = [copy.deepcopy(fd1.field), copy.deepcopy(fd2.field), copy.deepcopy(fd5.field), copy.deepcopy(fd6.field)]
        g.log.append([g.passive_stone, g.active_stone, g.move])
        if g.winner != 0:
            g.gameover = True


# create field classes
fd1 = fd.Field(*con.FIELD1)
fd2 = fd.Field(*con.FIELD2)
fd5 = fd.Field(*con.FIELD5)
fd6 = fd.Field(*con.FIELD6)
        

# roop
while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                x,y = event.pos
                left_click(x,y)
                
                    
    # fill the screen with a color to wipe away anything from last frame
    screen.fill(con.BACKGROUND_COLOR)

    # draw fields
    fd1.draw(screen)
    fd2.draw(screen)
    fd5.draw(screen)
    fd6.draw(screen)

    # draw turn information
    if g.turn%2:
        screen.blit(player_black,con.TURN_PLAYER_POS)
    else:
        screen.blit(player_white,con.TURN_PLAYER_POS)


    # draw undo button
    screen.blit(undo_button, con.UNDO_BUTTON_POS)
    # draw confirm button
    if g.active_move():
        screen.blit(confirm_button, con.CONFIRM_BUTTON_POS) 
    else:
        screen.blit(confirm_skelton, con.CONFIRM_BUTTON_POS) 

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(con.FPS)  # limits FPS to 60

pygame.quit()