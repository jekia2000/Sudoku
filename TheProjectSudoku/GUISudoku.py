from tkinter import Tk, Canvas, Frame, Button, BOTH, TOP, BOTTOM
MARGIN = 20  # Pixels around the board
SIDE = 50  # Width of every board cell.
WIDTH = HEIGHT = MARGIN * 2 + SIDE * 9  # Width and height of the whole board

#Note: Code for the graphical part of Sudoku has been taken from http://newcoder.io/gui/part-3/ and altered to suit my needs

class SudokuUI(Frame):
    """
    The Tkinter UI, responsible for drawing the board and accepting user input.
    """
    def __init__(self, parent, game):
        self.game = game
        self.parent = parent
        Frame.__init__(self, parent)

        self.__initUI()
##########################################################################

    def __initUI(self):
        self.indicator,self.row, self.col = True,0, 0
        self.parent.title("Sudoku")
        self.pack(fill=BOTH, expand=1)
        self.buttonFamily=Frame(self)
        self.buttonFamily.pack(fill=BOTH , side=BOTTOM)
        self.canvas = Canvas(self,width=WIDTH,height=HEIGHT)
        self.canvas.pack(fill=BOTH, side=TOP)

        self.createButtons()

        self.drawGrid()
        self.drawPuzzle()

        self.canvas.bind("<ButtonPress-1>", self.cellClicked)
        self.canvas.bind("<Key>", self.keyPressed)
    
###################################################################################################

    def createButtons(self):
        clearButton = Button(self.buttonFamily, text="Clear answers", command=self.clearAnswers)
        clearButton.pack(fill=BOTH ,side="left")

        computerButton = Button(self.buttonFamily, text="Give Up", command=self.computerSolution)
        computerButton.pack( fill=BOTH, side="left")

        finishButton = Button(self.buttonFamily, text="Finish" , command=self.check)
        finishButton.pack(fill=BOTH, side="left")

    #############################################################################

    def drawGrid(self):
        """
        Draws grid divided with blue lines into 3x3 squares
        """
        for i in range(10):
            color = "blue" if i % 3 == 0 else "gray"

            x0 = MARGIN + i * SIDE
            y0 = MARGIN
            x1 = MARGIN + i * SIDE
            y1 = HEIGHT - MARGIN
            self.canvas.create_line(x0, y0, x1, y1, fill=color)

            x0 = MARGIN
            y0 = MARGIN + i * SIDE
            x1 = WIDTH - MARGIN
            y1 = MARGIN + i * SIDE
            self.canvas.create_line(x0, y0, x1, y1, fill=color)

##########################################################################
    def drawPuzzle(self):
        for i in range(9):
            for j in range(9):
                self.canvas.delete("number{}{}".format(i,j))
                self.drawTile(i,j)

    ########################################################################

    def drawTile(self,i,j):
        answer = self.game.getBoardValue(i,j)
        if answer != 0:
            x = MARGIN + j * SIDE + SIDE / 2
            y = MARGIN + i * SIDE + SIDE / 2
            original = self.game.getResetListValue(i,j)
            if answer==original:
                color="black"

            elif self.indicator==False:
                color="red"

            else:
                color="blue"

            self.canvas.create_text(
                x, y, text=answer, tags="number{}{}".format(i,j), fill=color
            )
#######################################################################
    
    def clearAnswers(self):
        self.game.reset(self.indicator,self.row,self.col)
        self.indicator=True
        self.drawPuzzle()


#######################################################################
    def cellClicked(self, event):
        x, y = event.x, event.y
        self.canvas.focus_set()
        if (MARGIN < x < WIDTH - MARGIN and MARGIN < y < HEIGHT - MARGIN):
            self.canvas.focus_set()
            row, col =(int)((y - MARGIN) / SIDE),(int) ((x - MARGIN) / SIDE)
            if self.indicator and (self.row, self.col)==(row,col):
                self.row, self.col = -1, -1

            elif self.indicator and self.game.isOriginalEmpty(row,col):
                self.row, self.col = row, col

            if self.indicator or (self.indicator==False and (self.row,self.col)==(row,col)):
                self.drawCursor()

###########################################################################
    def drawCursor(self):
        self.canvas.delete("cursor")

        if self.row >= 0 and self.col >= 0: 
            x0 = MARGIN + self.col * SIDE + 1
            y0 = MARGIN + self.row * SIDE + 1
            x1 = MARGIN + (self.col + 1) * SIDE - 1
            y1 = MARGIN + (self.row + 1) * SIDE - 1
            self.canvas.create_rectangle(
                x0, y0, x1, y1,
                outline="red", tags="cursor"
            )
#################################################################################3
    def keyPressed(self, event):
        if self.row >= 0 and self.col >= 0 and (event.char in "1234567890") and event.char!="":
            self.indicator=self.game.addNumber(self.row,self.col,int(event.char), self.indicator)
            self.canvas.delete("number{}{}".format(self.row,self.col))
            self.drawTile(self.row,self.col)
            self.drawCursor()

    #################################################################################
    def drawVictory(self):
        x0 = y0 = MARGIN + SIDE * 2
        x1 = y1 = MARGIN + SIDE * 7
        self.canvas.create_oval(
            x0, y0, x1, y1,
            tags="victoryShape", fill="green", outline="black"
        )
       
        x = y = MARGIN + 4 * SIDE + SIDE / 2
        self.canvas.create_text(
            x, y,
            text="You win!", tags="victoryText",
            fill="white", font=("Arial", 32)
        )
##################################################################################
    def drawConsistency(self):
        x0 = y0 = MARGIN + SIDE * 2
        x1 = y1 = MARGIN + SIDE * 7
        self.canvas.create_oval(
            x0, y0, x1, y1,
            tags="consistencyShape", fill="yellow", outline="black"
        )
        x = y = MARGIN + 4 * SIDE + SIDE / 2
        self.canvas.create_text(
            x, y,
            text="Not yet!", tags="consistencyText",
            fill="white", font=("Arial", 32)
        )

###############################################################################
    def drawLoss(self):
        x0 = y0 = MARGIN + SIDE * 2
        x1 = y1 = MARGIN + SIDE * 7
        self.canvas.create_oval(
            x0, y0, x1, y1,
            tags="lossShape", fill="red", outline="black"
        )
        x = y = MARGIN + 4 * SIDE + SIDE / 2
        self.canvas.create_text(
            x, y,
            text="You lost!", tags="lossText",
            fill="white", font=("Arial", 32)
        )
#######################################################################
    def showNewGameButton(self):
        self.canvas.delete("victoryShape")
        self.canvas.delete("victoryText")
        self.canvas.delete("lossShape")
        self.canvas.delete("lossText")
        newGameButton = Button(self.buttonFamily, text="New Game", command=self.newGame)
        newGameButton.pack( fill=BOTH, side="left")
######################################################################
    def computerSolution(self):
        self.game.computerSolution(self.indicator,self.row,self.col)
        self.indicator=True
        self.drawPuzzle()
        self.indicator, self.row, self.col=False,-1,-1
        self.deleteButtons()
        self.drawCursor()
        self.drawLoss()
        self.canvas.after(3000,self.showNewGameButton)
        
    ###############################################################
    def deleteButtons(self):
        buttonList=self.buttonFamily.winfo_children()
        for i in range (3):
            buttonList[i].destroy()

#######################################################################################
    def newGame(self):
        self.game.startNewGame()
        self.indicator, self.row, self.col=True, 0, 0
        buttonList=self.buttonFamily.winfo_children()
        buttonList[0].destroy()
        self.createButtons()
        self.drawPuzzle()
########################################################

    def beforeConsistency(self,ind,row,col):
        self.canvas.delete("consistencyShape")
        self.canvas.delete("consistencyText")
        self.indicator,self.row,self.col=ind, row, col
        self.drawCursor()
######################################################## 

    def check(self):
        
        if self.game.checkWin():
            self.indicator, self.row, self.col=False,-1,-1
            self.drawCursor()
            self.deleteButtons()
            self.drawVictory()
            self.canvas.after(3000,self.showNewGameButton)
            
        else:
            ind,row,col=self.indicator,self.row,self.col
            self.indicator, self.row, self.col= False,-1, -1
            self.drawCursor()
            self.drawConsistency()
            self.canvas.after(3000,self.beforeConsistency,ind,row,col)
            