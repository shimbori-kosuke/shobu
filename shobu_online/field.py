import pygame
import config as con
import global_value as g

import copy

class Field():
    def __init__(self,id,left,top):
        self.id = id
        self.left = left
        self.top = top
        self.field_rect = pygame.Rect(left,top,con.FIELD_WIDTH,con.FIELD_HEIGHT)
        self.field = copy.deepcopy(con.FIELD_INNITIAL)

    # draw fields
    def draw(self,surface):
        # draw square for background
        pygame.draw.rect(surface, con.FIELD_BACKGROUND_COLOR, self.field_rect)

        # draw horizontal lines of field
        for i in range(con.FIELD_ROW+1):
            # start and end position for line
            start_pos = (self.left, self.top + con.BOX_HEIGHT * i)
            end_pos = (self.left + con.FIELD_WIDTH, self.top + con.BOX_HEIGHT * i)
            # draw lines
            pygame.draw.line(surface, con.FIELD_LINES_COLOR, start_pos, end_pos)
        
        # draw vertical lines of field
        for i in range(con.FIELD_COL+1):
            # start and end position for line
            start_pos = (self.left + con.BOX_WIDTH * i, self.top)
            end_pos = (self.left + con.BOX_WIDTH * i, self.top + con.FIELD_HEIGHT)
            # draw lines
            pygame.draw.line(surface, con.FIELD_LINES_COLOR, start_pos, end_pos)

        # paint box of selected stone and draw circle in available boxes
        if g.passive_move() and g.passive_stone['id'] == self.id:
            x = g.passive_stone['col']
            y = g.passive_stone['row']
            
            rect_left = self.left + con.BOX_WIDTH * x
            rect_top = self.top + con.BOX_HEIGHT * y
            rect = pygame.Rect(rect_left,rect_top,con.BOX_WIDTH,con.BOX_HEIGHT)

            # paint box of selected stone for passive move
            pygame.draw.rect(surface, con.SELECTED_COLOR, rect)

            # draw circle in available boxes
            color = con.AVAILABLE_CIRCLE_COLOR
            radius = con.AVAILABLE_CIRCLE_RADIUS
            for box in g.available:
                x = box[1]
                y = box[0]

                center_x = self.left + con.BOX_WIDTH/2 + x*con.BOX_WIDTH
                center_y = self.top + con.BOX_HEIGHT/2 + y*con.BOX_HEIGHT
                center = (center_x,center_y)
                pygame.draw.circle(surface, color, center, radius)
        
        elif g.active_move() and g.active_stone['id'] == self.id:
            x = g.active_stone['col']
            y = g.active_stone['row']
            
            rect_left = self.left + con.BOX_WIDTH * x
            rect_top = self.top + con.BOX_HEIGHT * y
            rect = pygame.Rect(rect_left,rect_top,con.BOX_WIDTH,con.BOX_HEIGHT)

            # paint box of selected stone for active move
            pygame.draw.rect(surface, con.SELECTED_COLOR, rect)

        # draw stones
        for y,row in enumerate(self.field):
            for x,box in enumerate(row):
                if box == 2:
                    center_x = self.left + con.BOX_WIDTH/2 + x*con.BOX_WIDTH
                    center_y = self.top + con.BOX_HEIGHT/2 + y*con.BOX_HEIGHT
                    center = (center_x,center_y)
                    pygame.draw.circle(surface, con.WHITE_STONE_COLOR, center, con.STONE_RADIUS)
                elif box == 3:
                    center_x = self.left + con.BOX_WIDTH/2 + x*con.BOX_WIDTH
                    center_y = self.top + con.BOX_HEIGHT/2 + y*con.BOX_HEIGHT
                    center = (center_x,center_y)
                    pygame.draw.circle(surface, con.BLACK_STONE_COLOR, center, con.STONE_RADIUS)

    def is_clicked(self,x,y):
        if self.left < x < self.left+con.FIELD_WIDTH and self.top < y < self.top+con.FIELD_HEIGHT:
            return True
        else:
            return False
    
    # click the field
    def click(self,x,y):
        print(self.id)
        if g.passive_select():
            self.passive_stone_select(x,y)
            print(g.passive_stone)
        elif g.passive_move():
            self.passive_move_select(x,y)
            print(g.move)
        elif g.active_select():
            self.active_stone_select(x,y)
            print(g.active_stone)
    
    # select stone for passive move
    def passive_stone_select(self,x,y):
        # check which box is clicked
        field_x = x - self.left
        field_y = y - self.top
        row = int(field_y / con.BOX_HEIGHT)
        col = int(field_x / con.BOX_WIDTH)
        # if turn player's field and stone
        if self.id % 2 == g.turn%2 and self.field[row][col] == g.turn%2+2:
            # check available box
            g.available = []
            availabale_check = [[-1,0],[-1,1],[0,1],[1,1],[1,0],[1,-1],[0,-1],[-1,-1]]

            for r,c in availabale_check:
                check_row = row+r
                check_col = col+c
                if 0 <= check_row <= 3 and 0 <= check_col <= 3:
                    if self.field[check_row][check_col] == 0:
                        g.available.append([check_row, check_col])
                        check_row += r
                        check_col += c
                    if 0 <= check_row <= 3 and 0 <= check_col <= 3:
                        if self.field[check_row][check_col] == 0:
                            g.available.append([check_row, check_col])
            g.passive_stone['id'] = self.id
            g.passive_stone['row'] = row
            g.passive_stone['col'] = col
            g.select = False

    # select move
    def passive_move_select(self,x,y):
        field_x = x - self.left
        field_y = y - self.top
        row = int(field_y / con.BOX_HEIGHT)
        col = int(field_x / con.BOX_WIDTH)
        if self.id == g.passive_stone['id'] and [row, col] in g.available:
            row_move = row - g.passive_stone['row']
            col_move = col - g.passive_stone['col']
            g.move['num'] = max(abs(row_move),abs(col_move))
            g.move['row'] = int((row_move)/max(1,abs(row_move)))
            g.move['col'] = int((col_move)/max(1,abs(col_move)))
            self.field[g.passive_stone['row']][g.passive_stone['col']] = 0
            self.field[row][col] = g.turn%2+2
            g.passive = False
        g.select = True
        g.available = []

    # select stone for active move
    def active_stone_select(self,x,y):
        field_x = x - self.left
        field_y = y - self.top
        row = int(field_y / con.BOX_HEIGHT)
        col = int(field_x / con.BOX_WIDTH)
        # if active move's field and turn player's stone
        if abs(self.id - g.passive_stone['id']) > 2 and self.field[row][col] == g.turn%2+2:
            # check if selected stone can move
            can_move = True
            check_row = row
            check_col = col
            field_cp = copy.deepcopy(self.field) # stuck of field

            for i in range(g.move['num']):
                move_row = check_row + g.move['row']
                move_col = check_col + g.move['col']

                # if move_box is out of the field : can't move
                if move_row < 0 or 3 < move_row or move_col < 0 or 3 < move_col:
                    can_move = False
                    break
                else:
                    move_box = field_cp[move_row][move_col]
                    # if turn player's stone is in move_box : can't move
                    if move_box == g.turn%2+2:
                        can_move = False
                        break
                    # if opponent's stone is in move_box
                    elif move_box == (g.turn+1)%2+2:
                        next_row = move_row + g.move['row']
                        next_col = move_col + g.move['col']
                        # if next_box exists
                        if 0 <= next_row <= 3 and 0 <= next_col <= 3:
                            next_box = field_cp[next_row][next_col]
                            # if any stone is in the next_box : can't move
                            if next_box != 0:
                                can_move = False
                                break
                            # if next_box is free : can move
                            else:
                                field_cp[check_row][check_col] = 0
                                field_cp[move_row][move_col] = (g.turn)%2+2
                                field_cp[next_row][next_col] = (g.turn+1)%2+2
                                check_row = move_row
                                check_col = move_col
                        # if next_box is out of field : can move
                        else:
                            field_cp[check_row][check_col] = 0
                            field_cp[move_row][move_col] = (g.turn)%2+2
                            check_row = move_row
                            check_col = move_col
                    # if move_box is free : can move
                    else:
                        field_cp[check_row][check_col] = 0
                        field_cp[move_row][move_col] = (g.turn)%2+2
                        check_row = move_row
                        check_col = move_col
            # if stone can move
            if can_move:
                g.select = False
                g.active_stone['id'] = self.id
                g.active_stone['row'] = row
                g.active_stone['col'] = col
                self.field = copy.deepcopy(field_cp)
                game_over = True
                for row in self.field:
                    if (g.turn+1)%2+2 in row:
                        game_over = False
                if game_over:
                    g.winner = g.turn%2+2
