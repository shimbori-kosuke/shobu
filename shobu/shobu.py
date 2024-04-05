import pygame
import field as fd
import button as bt
import config as con
import global_value as g
import click as cl


# pygame setup
pygame.init()
screen = pygame.display.set_mode(con.SCREEN_SIZE)
clock = pygame.time.Clock()
running = True

# setup fonts
p = pygame.font.Font(None,20)
h3 = pygame.font.Font(None,40)
h = pygame.font.Font(None,80)



# create font class
player_black = h3.render("BLACK",True,"black")
player_white = h3.render("WHITE",True,"black")

confirm_button = h.render("Next Turn",True,"black","white")
#confirm_rect = confirm_button.get_rect(center=(con.SCREEN_SIZE[0]/2, con.SCREEN_SIZE[1]/2))



# create field classes
fd1 = fd.Field(con.FIELD1[0],con.FIELD1[1],con.FIELD1[2],con.FIELD1[3],con.FIELD1[4])
fd2 = fd.Field(con.FIELD2[0],con.FIELD2[1],con.FIELD2[2],con.FIELD2[3],con.FIELD2[4])
fd5 = fd.Field(con.FIELD5[0],con.FIELD5[1],con.FIELD5[2],con.FIELD5[3],con.FIELD5[4])
fd6 = fd.Field(con.FIELD6[0],con.FIELD6[1],con.FIELD6[2],con.FIELD6[3],con.FIELD6[4])

def undo_move():
    g.passive = True
    g.select = True
    g.winner = 0
    fd1.field = g.previous_fields[0]
    fd2.field = g.previous_fields[1]
    fd5.field = g.previous_fields[2]
    fd6.field = g.previous_fields[3]
    print(fd1.field, fd2.field, fd5.field,fd6.field)

def confirm_move():
    print("confirm")
    if not g.passive and not g.select:
        g.passive = True
        g.select =True
        g.turn += 1
        g.previous_fields = [fd1.field, fd2.field, fd5.field, fd6.field]
        g.log.append([g.passive_stone, g.active_stone, g.move_direction, g.move_number])
        if g.winner != 0:
            g.gameover = True
        

# roop
while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                x,y = event.pos
                print(x,y)
                if not g.passive and not g.select:
                    if con.FIELD_LEFT < x < con.FIELD_RIGHT and con.FIELD_TOP < y < con.FIELD_BOTTOM:
                        undo_move()
                    elif 1000 < x and 620 < y:
                        confirm_move()

                else:
                    # if con.FIELD_LEFT <= x <= con.FIELD_RIGHT and con.FIELD_TOP <= y <= con.FIELD_BOTTOM:
                    #     cl.field(x,y)
                    if con.FIELD1[1] < x < con.FIELD1[1]+con.FIELD_WIDTH and con.FIELD1[2] < y < con.FIELD1[2]+con.FIELD_HEIGHT:
                        fd1.click(x,y)
                    elif con.FIELD2[1] < x < con.FIELD2[1]+con.FIELD_WIDTH and con.FIELD2[2] < y < con.FIELD2[2]+con.FIELD_HEIGHT:
                        fd2.click(x,y)
                    elif con.FIELD5[1] < x < con.FIELD5[1]+con.FIELD_WIDTH and con.FIELD5[2] < y < con.FIELD5[2]+con.FIELD_HEIGHT:
                        fd5.click(x,y)
                    elif con.FIELD6[1] < x < con.FIELD6[1]+con.FIELD_WIDTH and con.FIELD6[2] < y < con.FIELD6[2]+con.FIELD_HEIGHT:
                        fd6.click(x,y)
                    
    # fill the screen with a color to wipe away anything from last frame
    screen.fill(con.BACKGROUND_COLOR)

    # draw fields
    fd1.draw(screen)
    fd2.draw(screen)
    fd5.draw(screen)
    fd6.draw(screen)

    # draw information
    if g.turn%2:
        screen.blit(player_black,(20,20))
    else:
        screen.blit(player_white,(20,20))

    # draw confirm button
    if not g.passive and not g.select:
        screen.blit(confirm_button, (1000,620)) 

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()