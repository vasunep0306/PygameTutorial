import random, pygame, sys
from pygame.locals import *

FPS = 30  # frames per second, the general speed of the program
WINDOWWIDTH = 640 # size of the window's width in pixels
WINDOWHEIGHT = 480 # size of the window's height in pixels
REVEALSPEED = 8 # speed boxes' sliding reveals and covers
BOXSIZE = 40 # size of box height & width in pixels
GAPSIZE = 10 # size of gap between boxes in pixels
BOARDWIDTH = 10 # number of columns of icons
BOARDHEIGHT = 7 # number of rows of icons
TITLE = "Memory Game"
assert (BOARDWIDTH * BOARDHEIGHT) % 2 == 0, 'Board needs to have an even number of boxes for pairs and matches.'
XMARGIN = int((WINDOWWIDTH - (BOARDWIDTH * (BOXSIZE + GAPSIZE))) / 2)
YMARGIN = int((WINDOWHEIGHT - (BOARDHEIGHT * (BOXSIZE + GAPSIZE))) / 2)
# R G B
colors = 
{
    'GRAY':(100,100,100),
    'NAVYBLUE':(60,60,100),
    'WHITE':(255,255,255),
    'RED':(255,0,0),
    'GREEN':(0,255,0),
    'BLUE':(0,0,255),
    'YELLOW':(255,255,0),
    'ORANGE':(255,128,0),
    'PURPLE':(255,0,255),
    'CYAN':(0,255,255)
}

BGCOLOR = colors['NAVYBLUE']
LIGHTBGCOLOR = colors['GRAY']
BOXCOLOR = colors['WHITE']
HIGHLIGHTCOLOR = colors['BLUE']

shapes = 
{
    'DONUT':'donut',
    'SQUARE':'square',
    'DIAMOND':'diamond',
    'LINES':'lines',
    'OVAL' = 'oval'
}


ALLCOLORS = (colors['RED'], colors['GREEN'],colors['BLUE'],colors['YELLOW'],colors['ORANGE'],colors['PURPLE'],colors['CYAN'])

ALLSHAPES = (shapes['DONUT'],shapes['SQUARE'],shapes['DIAMOND'],shapes['LINES'],shapes['OVAL'])

assert len(ALLCOLORS) * len(ALLSHAPES) * 2 >= BOARDWIDTH * BOARDHEIGHT, "Board is too big for the number of shapes/colors defined."

def main():
    '''Main function'''
    global FPSCLOCK, DISPlAYSURF
    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
    
    mousex, mousey = 0,0
    pygame.display.set_caption(TITLE)
    
    mainBoard = getRandomizedBoard()
    revealedBoxes = generateRevealedBoxesData(False)

def generateRevealedBoxesData(val):
    '''Generate the revealed boxes data'''
    pass

def getRandomizedBoard():
    ''' Get a list of every possible shape in every possible color'''
    icons = []
    for colors in ALLCOLORS:
        for shape in ALLSHAPES:
            icons.append((shape,color))
            
    random.shuffle(icons) # randomize the order of the icons list
    numIconsUsed = int(BOARDWIDTH * BOARDHEIGHT / 2)  #calculate how many icons are needed
    icons = icons[:numIconsUsed] * 2 # make two of each 
    print("Line 78: ", icons)
    random.shuffle(icons)
    
    # Create the board data structure, with randomly placed icons.
    board = []
    for x in range(BOARDWIDTH):
        column = []
        for y in range(BOARDHEIGHT):
            column.append(icons[0])
            del icons[0]
        board.append(column)
    return board


def splitIntoGroupsOf(groupSize, theList):
    '''Splits a list into a list of lists, where the inner lists have the mosst groupSize number of items'''
    pass

def leftTopCoordsOfBox(boxx, boxy):
    '''Convert board coordinates to pixel coordinates'''
    pass


def getBoxAtPixel(x, y):
    ''' Get the box at the pixel with the given x,y coordinates '''
    pass

def drawIcon(shape, color, boxx, boxy):
    '''draw the icon with the given shape, color and box coordinates'''
    pass

def getShapeAndColor(board, boxx, boxy):
    ''' shape value for x, y spot is stored in board[x][y][0] '''
    pass

def drawBoxCovers(board,boxes,coverage):
    ''' Draw boxes being covered/revealed. Boxes is a list of two item lists, which have the x & y spot of the box'''
    pass

def revealBoxesAnimation(board, boxesToReveal):
    ''' Do the "box reveal" animation '''
    pass

def coverBoxesAnimation(board, boxesToCover):
    ''' Do the box cover animation '''
    pass


def drawBoard(board, revealed):
    ''' draw all of the boxes in their covered or revealed state '''
    pass


def drawHighlightBox(boxx, boxy):
    ''' draws the highlighted box '''
    pass
    
def startGameAnimation(board):
    ''' Randomly reveal the boxes 8 at a time '''
    pass

def gameWonAnimation(board):
    ''' flash the background color when the player has won '''
    pass

def hasWon(revealedBoxes):
    ''' Returns True if all the boxes have been revealed, otherwise False '''
    pass

if __name__ == '__main__':
    main()