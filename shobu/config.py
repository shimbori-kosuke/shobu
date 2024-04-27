# screen size
SCREEN_SIZE = (1280, 720) # width,height
SCREEN_CENTER = (SCREEN_SIZE[0]/2, SCREEN_SIZE[1]/2)

# field settings
FIELD_ROW = 4
FIELD_COL = 4
FIELD_LEFT = 310
FIELD_TOP = 20
FIELD_RIGHT = 970
FIELD_BOTTOM = 700
FIELD_CENTER_VERTICAL_MARGIN = 20
FIELD_CENTER_HORIZONTAL_MARGIN = 40

FIELD_WIDTH = (FIELD_RIGHT - FIELD_LEFT - FIELD_CENTER_VERTICAL_MARGIN)/2 # 320
FIELD_HEIGHT = (FIELD_BOTTOM - FIELD_TOP - FIELD_CENTER_HORIZONTAL_MARGIN)/2 # 320
BOX_WIDTH = FIELD_WIDTH/FIELD_COL
BOX_HEIGHT = FIELD_HEIGHT/FIELD_ROW
# initial field
FIELD_INNITIAL = [[2 if j==0 else 3 if j==FIELD_ROW-1 else 0 for i in range(FIELD_COL)] for j in range(FIELD_ROW)]

FIELD1 = (1,FIELD_LEFT, FIELD_BOTTOM - FIELD_HEIGHT)
FIELD2 = (2,FIELD_LEFT, FIELD_TOP)
FIELD5 = (5,FIELD_RIGHT - FIELD_WIDTH, FIELD_BOTTOM - FIELD_HEIGHT)
FIELD6 = (6,FIELD_RIGHT - FIELD_WIDTH, FIELD_TOP)

# stone size
STONE_RADIUS_PER_BOX = 0.45
STONE_RADIUS = (FIELD_WIDTH/max(FIELD_ROW,FIELD_COL)) * STONE_RADIUS_PER_BOX
#available circle size
AVAILABLE_CIRCLE_RADIUS_PER_STONE = 0.8
AVAILABLE_CIRCLE_RADIUS = STONE_RADIUS * AVAILABLE_CIRCLE_RADIUS_PER_STONE

# color
BACKGROUND_COLOR = "green"
FIELD_BACKGROUND_COLOR = "brown"
FIELD_LINES_COLOR = "black"
SELECTED_COLOR = "orange"
AVAILABLE_CIRCLE_COLOR = "gray"
WHITE_STONE_COLOR = "white"
BLACK_STONE_COLOR = "black"

# text settings
# font size
P_FONT_SIZE = 20
H3_FONT_SIZE = 40
H2_FONT_SIZE = 60
H1_FONT_SIZE = 80

# position
TURN_PLAYER_POS = (20,50)
UNDO_BUTTON_POS = (1000,550)
CONFIRM_BUTTON_POS = (1000,620)
RESET_BUTTON_POS = (1000,50)

# texts
BLACK_TURN_TEXT = "Black"
WHITE_TURN_TEXT = "White"
BLACK_WIN_TEXT = "Black Win!"
WHITE_WIN_TEXT = "White Win!"
UNDO_BUTTON_TEXT = "Undo Move "
CONFIRM_BUTTON_TEXT = "Next  Turn   "
RESET_BUTTON_TEXT = "Reset game"

# (position,text,antialias,color,background=None,font='p')
BLACK_TURN_SETTING = (TURN_PLAYER_POS,BLACK_TURN_TEXT,True,"black",None,'h3')
WHITE_TURN_SETTING = (TURN_PLAYER_POS,WHITE_TURN_TEXT,True,"black",None,'h3')
BLACK_WIN_SETTING = ((0,0),BLACK_WIN_TEXT,True,"white","black",'h1')
WHITE_WIN_SETTING = ((0,0),WHITE_WIN_TEXT,True,"black","white",'h1')
UNDO_BUTTON_SETTING = (UNDO_BUTTON_POS,UNDO_BUTTON_TEXT,True,"black","white",'h2')
CONFIRM_SKELTON_SETTING = (CONFIRM_BUTTON_POS,CONFIRM_BUTTON_TEXT,True,"dark grey","light grey",'h2') 
CONFIRM_BUTTON_SETTING = (CONFIRM_BUTTON_POS,CONFIRM_BUTTON_TEXT,True,"black","white",'h2')
RESET_BUTTON_SETTING = (RESET_BUTTON_POS,RESET_BUTTON_TEXT,True,"black","white",'h2')

FPS = 60