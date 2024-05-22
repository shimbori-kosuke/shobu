import logging
import pygame
import copy

import field as fd
import config as con
import global_value as g
import text as text

# set loggger
logger = logging.getLogger("logger")
logger.setLevel(logging.DEBUG)

# pygame setup
pygame.init()
screen = pygame.display.set_mode(con.SCREEN_SIZE)
clock = pygame.time.Clock()
running = True

# text setup
turn_black = text.Text(*con.BLACK_TURN_SETTING)
turn_white = text.Text(*con.WHITE_TURN_SETTING)
black_win = text.Text(*con.BLACK_WIN_SETTING)
white_win = text.Text(*con.WHITE_WIN_SETTING)
black_win.position_center()
white_win.position_center()

# button setup
undo_button = text.Button(*con.UNDO_BUTTON_SETTING)
confirm_skelton = text.Button(*con.CONFIRM_SKELTON_SETTING) 
confirm_button = text.Button(*con.CONFIRM_BUTTON_SETTING)
reset_button = text.Button(*con.RESET_BUTTON_SETTING)

# field setup
fd1 = fd.Field(*con.FIELD1)
fd2 = fd.Field(*con.FIELD2)
fd5 = fd.Field(*con.FIELD5)
fd6 = fd.Field(*con.FIELD6)

# left click
def left_click(x,y):
    if g.gameover:
        reset_game()
    else:
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
        elif undo_button.is_clicked(x,y):
            undo_move()
        elif confirm_button.is_clicked(x,y):
            if g.active_move():
                confirm_move()
        elif reset_button.is_clicked(x,y):
            reset_game()

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

def reset_game():
    g.reset()
    fd1.field = copy.deepcopy(con.FIELD_INNITIAL)
    fd2.field = copy.deepcopy(con.FIELD_INNITIAL)
    fd5.field = copy.deepcopy(con.FIELD_INNITIAL)
    fd6.field = copy.deepcopy(con.FIELD_INNITIAL)


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
        turn_black.draw(screen)
    else:
        turn_white.draw(screen)

    # draw reset button
    reset_button.draw(screen)
    # draw undo button
    undo_button.draw(screen)
    # draw confirm button
    if g.active_move():
        confirm_button.draw(screen)
    else:
        confirm_skelton.draw(screen)

    if g.black_win():
        black_win.draw(screen) 
    elif g.white_win():
        white_win.draw(screen)   

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(con.FPS)  # limits FPS to 60

pygame.quit()