from array import Array2D

class ReversiGame :
    BLANK_CELL = 0

    PLAYER1 = 1
    PLAYER2 = 2

    NEIGHBOR = [(-1, -1), (-1, 0), (-1, 1), \
               (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

    def __init__(self, numRows, numCols):
        self._grid = Array2D(numRows, numCols)
        self.configure(list())
        self._player = ReversiGame.PLAYER1

    def numRows(self):
        return self._grid.numRows()

    def numCols(self):
        return self._grid.numCols()

    def configure(self, coordList): 
        for i in range(self.numRows()):
            for j in range(self.numCols()):
                self.setCell(i, j, ReversiGame.BLANK_CELL)

        for coord in coordList:
            self.setCell(coord[0], coord[1], coord[2])

    def getChange(self, row, col, direct):
        tmp2 = list()
        
        for k in direct:
            #print "k " + str(k)
            ii, jj = ReversiGame.NEIGHBOR[k]
            i = row + ii
            j = col + jj
            find = 0
            tmp = list()
            while (i >= 0) and (i < self.numRows()) and \
                 (j >= 0) and (j < self.numCols()):
                 tmp.append((i, j))
                 #print (i, j, self._grid[i, j], self._player)
                 if self._grid[i, j] == self._player:
                     find = 1
                     break
                 i += ii
                 j += jj
            
            if find == 1:
                tmp2.extend(tmp)
            
        return tmp2 


    def setTurn(self, row, col):
        # if legal
        direct = self.numNeighbors(row, col, self.nextPlayer()) 
        if direct  == []:
            print "== illegal position =="
            return 0
        
        # change cell
        change = self.getChange(row, col, direct)
        if change == []:
            print "== illegal position =="
            return 0 

        #print change

        for i, j in change:
            self._grid[i, j] = self._player

        self._grid[row, col] = self._player
        self._player = self.nextPlayer()
        return 1

    def setCell(self, row, col, value):
        self._grid[row, col] = value


    def whoseTurn(self):
        return self._player

    def numChips(self, player):
        return

    def numOpenSquares(self):
        return

    # reture player num; 0 not finished
    def getWinner(self):
        return 0

    def isLegalMove(self, row, col):
        return 1

    def occupiedBy(self, row, col):
        return self._grid[row, col]

    def makeMove(row, col):
        return

    # eight direction 1-2-3  4- -5  6-7-8
    def numNeighbors(self, row, col, value):
        sum = list()
        k = 0
        
        for (i, j) in ReversiGame.NEIGHBOR:
            if (row+i >= 0) and (row+i < self.numRows()):
                if (col+j >= 0) and (col+j < self.numCols()):
                    if self._grid[row+i, col+j] == value:
                        sum.append(k) 
            k += 1
        #print sum
        return sum

    def nextPlayer(self):
        return [ReversiGame.PLAYER1, ReversiGame.PLAYER2] \
                    [self._player == ReversiGame.PLAYER1]

