import pygame
import config as con
import global_value as g

import copy

class Field():
    def __init__(self,id,left,top,width,height):
        self.id = id
        self.left = left
        self.top = top
        self.width = width
        self.height = height
        self.box_width = width/4
        self.box_height = height/4
        self.field_rect = pygame.Rect(left,top,width,height)
        self.field = [[2,2,2,2],[0,0,0,0],[0,0,0,0],[3,3,3,3]]

    # draw fields
    def draw(self,surface):
        # draw square for background
        pygame.draw.rect(surface, con.FIELD_BACKGROUND_COLOR, self.field_rect)

        # draw lines of field
        for i in range(5):
            # start and end position for line
            horizontal_start_pos = (self.left, self.top + self.height/4 * i)
            horizontal_end_pos = (self.left + self.width, self.top + self.height/4 * i)
            vertical_start_pos = (self.left + self.width/4 * i, self.top)
            vertical_end_pos = (self.left + self.width/4 * i, self.top + self.height)
            #draw lines
            pygame.draw.line(surface, con.FIELD_LINES_COLOR, horizontal_start_pos, horizontal_end_pos)
            pygame.draw.line(surface, con.FIELD_LINES_COLOR, vertical_start_pos, vertical_end_pos)

        # paint box of selected stone and draw circle in available boxes
        if g.passive and not g.select and g.passive_stone[0] == self.id:
            x = g.passive_stone[2]
            y = g.passive_stone[1]
            
            rect_left = self.left + self.box_width * x
            rect_top = self.top + self.box_height * y
            rect = pygame.Rect(rect_left,rect_top,self.box_width,self.box_height)

            # paint box of selected stone for passive move
            pygame.draw.rect(surface, con.SELECTED_COLOR, rect)

            # draw circle in available boxes
            color = con.AVAILABLE_CIRCLE_COLOR
            radius = con.AVAILABLE_CIRCLE_RADIUS
            for box in g.available:
                x = box[1]
                y = box[0]

                center_x = self.left + self.box_width/2 + x*self.box_width
                center_y = self.top + self.box_height/2 + y*self.box_height
                center = (center_x,center_y)
                pygame.draw.circle(surface, color, center, radius)
        
        elif not g.passive and not g.select and g.active_stone[0] == self.id:
            x = g.active_stone[2]
            y = g.active_stone[1]
            
            rect_left = self.left + self.box_width * x
            rect_top = self.top + self.box_height * y
            rect = pygame.Rect(rect_left,rect_top,self.box_width,self.box_height)

            # paint box of selected stone for active move
            pygame.draw.rect(surface, con.SELECTED_COLOR, rect)

        # draw stones
        for y,row in enumerate(self.field):
            for x,box in enumerate(row):
                if box == 2:
                    center_x = self.left + self.box_width/2 + x*self.box_width
                    center_y = self.top + self.box_height/2 + y*self.box_height
                    center = (center_x,center_y)
                    pygame.draw.circle(surface, con.WHITE_STONE_COLOR, center, con.STONE_RADIUS)
                elif box == 3:
                    center_x = self.left + self.box_width/2 + x*self.box_width
                    center_y = self.top + self.box_height/2 + y*self.box_height
                    center = (center_x,center_y)
                    pygame.draw.circle(surface, con.BLACK_STONE_COLOR, center, con.STONE_RADIUS)
    
    # click the field
    def click(self,x,y):
        if g.passive and g.select:
            self.passive_stone_select(x,y)
        elif g.passive and not g.select:
            self.passive_move_select(x,y)
        elif not g.passive and g.select:
            self.active_stone_select(x,y)
        # else:
        #     self.reset_move(x,y)
    
    # select stone for passive move
    def passive_stone_select(self,x,y):
        field_x = x - self.left
        field_y = y - self.top
        row = int(field_y / self.box_height)
        col = int(field_x / self.box_width)
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
                        check_row = row+2*r
                        check_col = col+2*c
                    if 0 <= check_row <= 3 and 0 <= check_col <= 3:
                        if self.field[check_row][check_col] == 0:
                            g.available.append([check_row, check_col])
                                       

            g.passive_stone = [self.id, row, col]
            g.select = False

    # select move
    def passive_move_select(self,x,y):
        field_x = x - self.left
        field_y = y - self.top
        row = int(field_y / self.box_height)
        col = int(field_x / self.box_width)
        if self.id == g.passive_stone[0] and [row, col] in g.available:
            g.move_number = max(abs(row - g.passive_stone[1]),abs(col - g.passive_stone[2]))
            g.move_direction = [int((row - g.passive_stone[1])/max(1,abs(row - g.passive_stone[1]))), int((col - g.passive_stone[2])/max(1,abs(col - g.passive_stone[2])))]
            self.field[g.passive_stone[1]][g.passive_stone[2]] = 0
            self.field[row][col] = g.turn%2+2
            g.passive = False
        g.select = True
        g.available = []

    # select stone for active move
    def active_stone_select(self,x,y):
        field_x = x - self.left
        field_y = y - self.top
        row = int(field_y / self.box_height)
        col = int(field_x / self.box_width)
        # if active move's field and turn player's stone
        if abs(self.id - g.passive_stone[0]) > 2 and self.field[row][col] == g.turn%2+2:
            # check if selected stone can move
            can_move = True
            check_row = row
            check_col = col
            field_cp = copy.deepcopy(self.field) # stuck of field
            for i in range(g.move_number):
                move_row = check_row + g.move_direction[0]
                move_col = check_col + g.move_direction[1]

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
                        next_row = move_row + g.move_direction[0]
                        next_col = move_col + g.move_direction[1]
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
                g.active_stone = [self.id, row, col]
                self.field = copy.deepcopy(field_cp)
                game_over = True
                for row in self.field:
                    if (g.turn+1)%2+2 in row:
                        game_over = False
                if game_over:
                    g.winner = g.turn%2+2

    # # confirm move, go on next turn
    # def reset_move(self,x,y):
    #     g.passive = True
    #     g.select = True
    #     g.winner = 0