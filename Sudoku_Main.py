#~~~~~ Sudoku Main ~~~~~#

################################################ main program ################################################

validInput = False
while not validInput:
    option = input("pick an option: \n1) Command Line Interface \n2) Graphical User Interface \noption >")
    if option == '1':
        validCLIInput = False
        while not validCLIInput:    # ensures the user enters in a valid option
            optionCLI = input("pick an option: \n1) solve a grid \n2) generate a complete grid \n3) create a puzzle \noption >")    # gets the user to choose which option they would like
            if optionCLI == '1':
                from Sudoku_Solver import initialiseSolving    # imports the functions the user requires
                initialiseSolving()
                validCLIInput = True
            elif optionCLI == '2':
                from Sudoku_Generator import initialiseGenerating     # doesn't import it at the start to save importing a bunch of unnecessary stuff - only one of these will be used
                initialiseGenerating()
                validCLIInput = True
            elif optionCLI == '3':
                from Sudoku_Creator import initialiseCreating
                initialiseCreating()
                validCLIInput = True
            else:
                print("enter a valid option")
                validCLIInput = False
        playAgain = input("play again, y/n?")
        if playAgain == 'y':
            validInput = False
        else:
            validInput = True
            
    elif option == '2':
        validGUIInput = False
        while not validGUIInput:
            optionGUI = input("pick an option: \n1) sudoku game \n2) sudoku solver")
            if optionGUI == '1':
                from Sudoku_Game_GUI import initialiseGameGUI
                initialiseGameGUI()
                validGUIInput = True
            elif option == '2':
                from Sudoku_Solver_GUI import initialiseSolverGUI
                initialiseSolverGUI()
                validGUIInput = True
            else:
                print("enter a valid option")
                validGUIInput = False
        playAgain = input("play again, y/n?")
        if playAgain == 'y':
            validInput = False
        else:
            validInput = True
    else:
        print("enter a valid input")
        validInput = False

print("danke for doing sudoku-y stuff")    # mandatory gratitude giving
    
