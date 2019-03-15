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
    revealedBoxes = []
    for i in range(BOARDWIDTH):
        revealedBoxes.append([val]*BOARDHEIGHT)
    return revealedBoxes

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
    '''Splits a list into a list of lists, where the inner lists have the most groupSize number of items'''
    result = []
    for i in range(0, len(theList), groupSize):
        result.append(theList[i:i + groupSize])
    return result

def leftTopCoordsOfBox(boxx, boxy):
    '''Convert board coordinates to pixel coordinates'''
    left = boxx * (BOXSIZE + GAPSIZE) + XMARGIN
    top = boxy * (BOXSIZE + GAPSIZE) + YMARGIN
    return (left, top)


def getBoxAtPixel(x, y):
    ''' Get the box at the pixel with the given x,y coordinates '''
    for boxx in range(BOARDWIDTH):
        for boxy in range(BOARDHEIGHT):
            left,top = leftTopCoordsOfBox(boxx,boxy)
            boxRect = pygame.Rect(left,top,BOXSIZE,BOXSIZE)
            if boxRect.collidepoint(x,y):
                return (boxx, boxy)
    return (None, None)
    

def drawIcon(shape, color, boxx, boxy):
    '''draw the icon with the given shape, color and box coordinates'''
    pass

def getShapeAndColor(board, boxx, boxy):
    ''' shape value for x, y spot is stored in board[x][y][0] '''
    return board[boxx][boxy][0], board[boxx][boxy][1]

def drawBoxCovers(board,boxes,coverage):
    ''' Draw boxes being covered/revealed. Boxes is a list of two item lists, which have the x & y spot of the box'''
    for box in boxes:
        left, top = leftTopCoordsOfBox(box[0], box[1])
        pygame.draw.rect(DISPLAYSURF, BGCOLOR, (left, top, BOXSIZE, BOXSIZE))
        shape,color = getShapeAndColor(board, box[0], box[1])
        drawIcon(shape, color, box[0], box[1])
        if coverage > 0:  # only draw the cover if there is an coverage
            pygame.draw.rect(DISPLAYSURF, BOXCOLOR, (left,top,coverage,BOXSIZE))
        pygame.display.update()
        FPSCLOCK.tick(FPS)

def revealBoxesAnimation(board, boxesToReveal):
    ''' Do the "box reveal" animation '''
    for coverage in range(BOXSIZE, (-REVEALSPEED) - 1, -REVEALSPEED):
        drawBoxCovers(board, boxesToReveal, coverage)

def coverBoxesAnimation(board, boxesToCover):
    ''' Do the box cover animation '''
    for coverage in range(0, BOXSIZE + REVEALSPEED, REVEALSPEED):
        drawBoxCovers(board, boxesToCover, coverage)


def drawBoard(board, revealed):
    ''' draw all of the boxes in their covered or revealed state '''
    for boxx in range(BOARDWIDTH):
        for boxy in range(BOARDHEIGHT):
            left, top = leftTopCoordsOfBox(boxx, boxy)
            if not revealed[boxx][boxy]:
                # Draw a covered box.
                pygame.draw.rect(DISPLAYSURF, BOXCOLOR, (left,top,BOXSIZE,BOXSIZE))
            else:
                shape, color = getShapeAndColor(board, boxx, boxy)
                drawIcon(shape, color, boxx, boxy)


def drawHighlightBox(boxx, boxy):
    ''' draws the highlighted box '''
    left, top = leftTopCoordsOfBox(boxx, boxy)
    pygame.draw.rect(DISPLAYSURF, HIGHLIGHTCOLOR, (left - 5, top - 5, BOXSIZE + 10, BOXSIZE + 10), 4)
    
def startGameAnimation(board):
    ''' Randomly reveal the boxes 8 at a time '''
    coveredBoxes = generateRevealedBoxesData(False)
    boxes = []
    for x in range(BOARDWIDTH):
        for y in range(BOARDHEIGHT):
            boxes.append((x,y))
    random.shuffle(boxes)
    boxGroups = splitIntoGroupsOf(8, boxes)
    
    drawBoard(board, coveredBoxes)
    for boxGroup in boxGroups:
        revealBoxesAnimation(board, boxGroup)
        coverBoxesAnimation(board, boxGroup)

def gameWonAnimation(board):
    ''' flash the background color when the player has won '''
    coveredBoxes = generateRevealedBoxesData(True)
    color1 = LIGHTBGCOLOR
    color2 = BGCOLOR
    
    for i in range(13):
        color1, color2 = color2, color1 # swap colors
        DISPLAYSURF.fill(color1)
        drawBoard(board, coveredBoxes)
        pygame.display.update()
        pygame.time.wait(300)

def hasWon(revealedBoxes):
    ''' Returns True if all the boxes have been revealed, otherwise False '''
    for i in revealedBoxes:
        if False in i:
            return False
    return True

if __name__ == '__main__':
    main()