from reversigame import ReversiGame

GRID_WIDTH = 8
GRID_HEIGHT = 8

INIT_CONFIG = [ (GRID_WIDTH/2-1, GRID_HEIGHT/2-1, ReversiGame.PLAYER1), \
                (GRID_WIDTH/2-1, GRID_HEIGHT/2, ReversiGame.PLAYER2), \
                (GRID_WIDTH/2, GRID_HEIGHT/2-1, ReversiGame.PLAYER2), \
                (GRID_WIDTH/2, GRID_HEIGHT/2, ReversiGame.PLAYER1), ]
P1 = "#"
P2 = "O"

def main():
    
    grid = ReversiGame(GRID_WIDTH, GRID_HEIGHT)
    grid.configure(INIT_CONFIG)

    draw(grid)
    while not grid.getWinner():
        row, col =  input(grid)
        if (grid.isLegalMove(row, col)):
            grid.setTurn(row, col)
            draw(grid) 

def draw(grid):
    print ""
    print " ",
    for i in range(grid.numRows()) :
        print i, 
    print ""

    for i in range(grid.numRows()) :
        print i,
        for j in range( grid.numCols() ) :
            print [".", P1, P2][grid.occupiedBy(i, j)],
        print ""
    print ""

def input(grid):
    prompt = "%s's turn row: " % [P2, P1] \
            [grid.whoseTurn()==ReversiGame.PLAYER1]
    row = int(raw_input(prompt))
    prompt = "%s's turn col: " % [P2, P1] \
            [grid.whoseTurn()==ReversiGame.PLAYER1]
    col = int(raw_input(prompt))

    return (row, col)

main()
