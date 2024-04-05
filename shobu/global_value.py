passive = True
select = True
passive_stone = [0,0,0] # if selected -> [id,y,x]
active_stone = [0,0,0] # if selected -> [id,y,x]
move_direction = [0,0] # y,x
move_number = 0
available = [] # boxes stone can move to [[y1,x1],[y2,x2],...]
log = [] # [passive_stone, active_stone, move_direction, move_number]
winner = 0
gameover = False
previous_fields = [[[2,2,2,2],[0,0,0,0],[0,0,0,0],[3,3,3,3]],
                   [[2,2,2,2],[0,0,0,0],[0,0,0,0],[3,3,3,3]],
                   [[2,2,2,2],[0,0,0,0],[0,0,0,0],[3,3,3,3]],
                   [[2,2,2,2],[0,0,0,0],[0,0,0,0],[3,3,3,3]]] # stuck previous field to undo

turn = 1
# turn%2 = black:1 white:0
# turn%2 + 2 = black:3 white:2 <- same as stone