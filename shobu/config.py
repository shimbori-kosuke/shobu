#size

SCREEN_SIZE = (1280, 720) # width,height
#field
FIELD_LEFT = 310
FIELD_TOP = 20
FIELD_RIGHT = 970
FIELD_BOTTOM = 700
FIELD_CENTER_VERTICAL_MARGIN = 20
FIELD_CENTER_HORIZONTAL_MARGIN = 40

FIELD_WIDTH = (FIELD_RIGHT - FIELD_LEFT - FIELD_CENTER_VERTICAL_MARGIN)/2 # 320
FIELD_HEIGHT = (FIELD_BOTTOM - FIELD_TOP - FIELD_CENTER_HORIZONTAL_MARGIN)/2 # 320

FIELD1 = (1,FIELD_LEFT, FIELD_BOTTOM - FIELD_HEIGHT, FIELD_WIDTH, FIELD_WIDTH) # id,left,top,width,height
FIELD2 = (2,FIELD_LEFT, FIELD_TOP, FIELD_WIDTH, FIELD_HEIGHT) # id,left,top,width,height
FIELD5 = (5,FIELD_RIGHT - FIELD_WIDTH, FIELD_BOTTOM - FIELD_HEIGHT, FIELD_WIDTH, FIELD_HEIGHT) # id,left,top,width,height
FIELD6 = (6,FIELD_RIGHT - FIELD_WIDTH, FIELD_TOP, FIELD_WIDTH, FIELD_HEIGHT) # id,left,top,width,height

AVAILABLE_CIRCLE_RADIUS = 20
STONE_RADIUS = 35

# color
BACKGROUND_COLOR = "green"
FIELD_BACKGROUND_COLOR = "brown"
FIELD_LINES_COLOR = "black"
SELECTED_COLOR = "orange"
AVAILABLE_CIRCLE_COLOR = "gray"
WHITE_STONE_COLOR = "white"
BLACK_STONE_COLOR = "black"
