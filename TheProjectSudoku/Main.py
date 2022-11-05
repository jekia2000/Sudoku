from GUISudoku import SudokuUI
from tkinter import Tk
from Game import Game
from Exceptions import *
MARGIN = 20  # Pixels around the board
SIDE = 50  # Width of every board cell.
WIDTH = HEIGHT = MARGIN * 2 + SIDE * 9  # Width and height of the whole board

def main():
    
    try:
        game=Game()
        root = Tk()
        SudokuUI(root, game)
        root.geometry("%dx%d" % (WIDTH, HEIGHT + 40))
        root.mainloop()

    except IOError:
        print("Error: Cannot open/read the specified file")
    except InvalidDataException as e:
        print(e)
    except NoSudokuSolutionException as e:
        print(e)
    except InvalidDimensionsException as e:
        print(e)
    except  SolvedSudokuException as e:
        print(e)

#############################################################
if __name__=="__main__":
    main()
