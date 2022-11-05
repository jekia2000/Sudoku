import random
from Exceptions import *

class Board:
    def __init__(self):
        #It will store the current state of Sudoku
        self.matrix=[0]*9

        #It will store the solution to Sudoku
        self.solution=[0]*9

        #helper lists
        self.row=[0]*9
        self.column=[0]*9
        self.square=[0]*9

        for i in range (9):
            self.matrix[i]=[0]*9
            self.solution[i]=[0]*9
            self.row[i]= 0
            self.column[i]=0
            self.square[i]=0

        #Choose to either generate the Sudoku via file input or the random generator
        self.randomGenerator()
        #self.fileGenerator("./fileSudoku.txt")
        
        #If you choose to generate Sudoku via the fileGenerator() make sure Sudoku is a 9x9 puzzle
        #with valid input ( digits 0-9, where 0 is means an empty tile). Morever, you should not fill the whole board with digits 
        #greater than 0, as there is no point in playing then. Finally, the digits you provide must yield a solvable Sudoku. If any of
        # this conditions is not satisfied, the Programme will raise an exception and terminate printing an appropriate message.
        
###############################################################################################
    def fill(self,i,j,value):
        self.matrix[i][j]=value
        value-=1
        self.row[i]=self.row[i] | (1<<value)
        self.column[j]=self.column[j] | (1<<value)
        self.square[i//3 * 3 + j // 3]=self.square[i//3 * 3 + j // 3] | (1<<value)
####################################################################################
    def unfill(self,i,j,value):
        self.matrix[i][j]=0
        value-=1
        self.row[i]^=(1<<value)
        self.column[j]^=(1<<value)
        self.square[i //3 *3+j // 3]^=(1<<value)
#################################################################################
    def isEmpty(self,i,j):
        return self.matrix[i][j]==0

####################################################################################
    def backtrack(self,numberOfCases):
        positions=[]
        for row in range (9):
            for column in range (9):
                if self.isEmpty(row,column):
                    positions.append(9*row+column)
        k=0
        value=1
        lastValue=0
        while numberOfCases>0:
            while k < len(positions):
                lastPosition=positions[k]
                i=lastPosition // 9
                j=lastPosition % 9
                isWritten=False
                intersect=self.row[i] | self.column[j] | self.square[i//3*3+j//3]
                for m in range(value, 10):
                    if (intersect & 1<<(m-1))==0:
                        self.fill(i,j,m)
                        isWritten=True
                        break
                if not isWritten:
                    if k==0:
                        return False

                    lastPosition=positions[k-1]
                    i=lastPosition // 9
                    j=lastPosition % 9
                    value=self.matrix[i][j]
                    self.unfill(i,j,value)
                    value=value+1
                    k=k-1

                else:
                    k=k+1
                    value=1
            numberOfCases-=1
            k=k-1
            lastValue=self.matrix[8][8]
            value=lastValue+1
            self.unfill(8,8,self.matrix[8][8])
        self.fill(8,8,lastValue)
        return True

##########################################################################################

    def filledBoard(self):
        filled=(1<<9)-1 #this is 511(10)=111111111(2)
        for i in range (9):
            if self.row[i]^filled!=0:
                return False
        return True

####################################################################################
#this function was used for debbuging
    def write(self):
        for i in range (9):
            row=""
            for j in range (9):
                row+="{:4d}".format(self.matrix[i][j])
            print(row)
############################################################################

    def randomGenerator(self):
        randomNumber=random.randint(1,1000)
        choiceRow=list(range(9))
        choiceValue=list(range(1,10))
        while choiceRow!=[]:
            j=random.choice(choiceRow)
            choiceRow.remove(j)
            value=random.choice(choiceValue)
            self.fill(0,j,value)
            choiceValue.remove(value)
        solutionExists=self.backtrack(randomNumber)

        if not solutionExists:
            self.randomGenerator()

        for i in range (9):
            for j in range (9):
                self.solution[i][j]=self.matrix[i][j]

        for i in range (9):
            choicePosition=list(range(9))
            numberOfPositions=random.randint(4,7)
            for counter in range (numberOfPositions):
                j=random.choice(choicePosition)
                choicePosition.remove(j)
                self.unfill(i,j,self.matrix[i][j])

###################################################################################
    def fileGenerator(self,filename):
        file=open(filename,'r')
        i=0
        for line in file:
            text=line.strip()
            numberList=text.split()

            if text=="":
                continue
            if len(numberList)!=9:
                raise InvalidDimensionsException("Error: Your Sudoku is not a 9x9 table")
            for j in range(9):
                char=numberList[j].strip()
                if char in '123456789':
                    value=int(char)
                    intersect=self.row[i] | self.column[j] | self.square[i//3*3+j//3]
                    if (intersect & 1<<(value-1))==0:
                        self.fill(i,j,value)
                    else:
                        raise NoSudokuSolutionException("Error: Your Sudoku does not have a solution")
                elif char=='0':
                    pass
                
                else:
                    raise InvalidDataException("Error: Sudoku entries are not 0-9 digits")

            i+=1
        file.close()

        if i!=9:
            raise InvalidDimensionsException("Error: Your Sudoku is not a 9x9 table")

        if self.filledBoard():
            raise SolvedSudokuException("Error:You have entered an already solved Sudoku")

        for i in range(9):
            for j in range(9):
                self.solution[i][j]=self.matrix[i][j]

        solutionExists=self.backtrack(1)
        if not solutionExists:
            raise NoSudokuSolutionException("Error: Your Sudoku does not have a solution")

        for i in range (9):
            for j in range (9):
                temp=self.matrix[i][j]
                self.matrix[i][j]=self.solution[i][j]
                self.solution[i][j]=temp
        self.resetHelperLists()

#############################################################################################

    def resetHelperLists(self):
        for i in range(9):
            for j in range(9):
                if self.solution[i][j]!=self.matrix[i][j]:
                    self.unfill(i,j,self.solution[i][j])

                
                
                


