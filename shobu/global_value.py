import config as con
import copy

passive = True
select = True
passive_stone = {'id':1, 'row':0, 'col':0}
active_stone = {'id':0, 'row':0, 'col':0}
move = {'num':0, 'row':0, 'col':0} # move
available = [] # boxes stone can move to [[y1,x1],[y2,x2],...]
log = [] # [passive_stone, active_stone, move_direction, move_number]
winner = 0 # winner
gameover = False # game is over
# stuck previous field to undo
previous_fields = [copy.deepcopy(con.FIELD_INNITIAL),copy.deepcopy(con.FIELD_INNITIAL),copy.deepcopy(con.FIELD_INNITIAL),copy.deepcopy(con.FIELD_INNITIAL)]

turn = 1
# turn%2 = black:1 white:0
# turn%2 + 2 = black:3 white:2 <- same as stone

def passive_select():
    if passive and select:
        return True
    else:
        return False
    
def passive_move():
    if passive and not select:
        return True
    else:
        return False
    
def active_select():
    if not passive and select:
        return True
    else:
        return False
    
def active_move():
    if not passive and not select:
        return True
    else:
        return False