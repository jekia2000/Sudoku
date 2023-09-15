# Sudoku
Developed on Windows 10 in my 2nd year

1) Code for the graphical part of Sudoku has been taken from http://newcoder.io/gui/part-3/ and altered to suit my needs

2) Sudoku rules: http://www.counton.org/sudoku/rules-of-sudoku.php

3) How to run the project?

    Be sure to import the tkinter library if you do not have it.
    -You can open the python files in an editor, e.g. Visual Studio Code, and simply run Main.py
    -You can enter the "TheProjectSudoku" folder either via Windows cmd or Linux terminal and type "python Main.py" 

4) How to play?

    Click on an empty cell. You can enter numbers 0-9 from the keyboard. By entering 0 you erase a previous digit. If you want to
    erase all your entries, click on the "Clear answers" button. Digits are displayed as black, blue and red. Black digits represent the 
    original digits in the Sudoku. Blue digits are the correctly entered digits, i.e. they do not break Sudoku rules. Red digits are wrongly
    entered digits which break Sudoku rules. You cannot continue with your play until you change the red digit to blue, or erases it. When you
    fill in the Sudoku, click on the "Finish" button to finish your game. If you cannot solve the puzzle, click on the "Give up" button. After
    that, you can start a new game by simply clicking on the "New Game".
