import config as con

# func for click field
def field(x,y):
    if con.FIELD1[1] <= x <= con.FIELD1[1]+con.FIELD_WIDTH and con.FIELD1[2] <= y <= con.FIELD1[2]+con.FIELD_HEIGHT:
        pass