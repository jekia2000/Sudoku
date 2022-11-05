from Board import Board
class Game:
    def __init__(self):
        self.board=Board()
        self.setResetList()
################################################################

    def setResetList(self):
        self.resetList=[0]*9
        for i in range(9):
            self.resetList[i]=[0]*9
            for j in range(9):
                self.resetList[i][j]=self.board.matrix[i][j]

###################################################################

    def reset(self, indicator,row,col):
        if indicator==False:
            self.board.matrix[row][col]=0
        for i in range (9):
            for j in range (9):
                value=self.board.matrix[i][j]
                if value!=self.resetList[i][j]:
                    self.board.unfill(i,j,value)
                self.board.matrix[i][j]=self.resetList[i][j]

####################################################################

    def checkWin(self):
        return self.board.filledBoard()

################################################################

    def addNumber(self,i,j,value,indicator):
        if self.board.matrix[i][j] > 0:
            if indicator:
                self.board.unfill(i,j,self.board.matrix[i][j])
            else:
                self.board.matrix[i][j]=0
            
        if value==0:
            return True
      
        intersect=self.board.row[i] | self.board.column[j] | self.board.square[i//3*3+j//3]
        
       

        if (intersect & 1<<(value-1))==0:
           
            self.board.fill(i,j,value)
            return True

       
        self.board.matrix[i][j]=value
        return False
############################################################################

    def isOriginalEmpty(self,row,col):
        if self.resetList[row][col]==0:
            return True
        return False

####################################################################
    def computerSolution(self,indicator,row,col):
        self.reset(indicator,row,col)
        for i in range(9):
            for j in range(9):
                self.board.matrix[i][j]=self.board.solution[i][j]

################################################################

    def startNewGame(self):
        self.board=Board()
        self.setResetList()

#################################################################
    def getBoardValue(self,i,j):
        return self.board.matrix[i][j]

#############################################################
    def getResetListValue(self,i,j):
        return self.resetList[i][j]

  

