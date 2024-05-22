# unused

import config as con
import global_value as g

import copy

# func for left click
def left_click(x,y):
    # if field is clicked
    if sho.fd1.is_clicked(x,y):
        print("field1 is clicked")
        sho.fd1.click(x,y)
    elif sho.fd2.is_clicked(x,y):
        print("field2 is clicked")
        sho.fd2.click(x,y)
    elif sho.fd5.is_clicked(x,y):
        print("field5 is clicked")
        sho.fd5.click(x,y)
    elif sho.fd6.is_clicked(x,y):
        print("field6 is clicked")
        sho.fd6.click(x,y)
    elif sho.undo_button.is_clicked(x,y):
            undo_move()
    elif sho.confirm_button.is_clicked(x,y):
        if g.active_move():
            confirm_move()

def undo_move():
    g.passive = True
    g.select = True
    g.winner = 0
    sho.fd1.field = copy.deepcopy(g.previous_fields[0])
    sho.fd2.field = copy.deepcopy(g.previous_fields[1])
    sho.fd5.field = copy.deepcopy(g.previous_fields[2])
    sho.fd6.field = copy.deepcopy(g.previous_fields[3])


def confirm_move():
    if g.active_move():
        g.passive = True
        g.select =True
        g.turn += 1
        g.previous_fields = [copy.deepcopy(sho.fd1.field), copy.deepcopy(sho.fd2.field), copy.deepcopy(sho.fd5.field), copy.deepcopy(sho.fd6.field)]
        g.log.append([g.passive_stone, g.active_stone, g.move])
        if g.winner != 0:
            g.gameover = True
