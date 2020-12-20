#~~~~~ Sudoku Main ~~~~~#

################################################ main program ################################################

validInput = False
while not validInput:    # ensures the user enters in a valid option
    option = input("pick an option: \n1) solve a grid \n2) generate a complete grid \n3) create a puzzle \noption >")    # gets the user to choose which option they would like
    if option == '1':
        from Sudoku_Solver import initialiseSolving    # imports the functions the user requires
        initialiseSolving()
        validInput = True
    elif option == '2':
        from Sudoku_Generator import initialiseGenerating
        initialiseGenerating()
        validInput = True
    elif option == '3':
        from Sudoku_Creator import initialiseCreating
        initialiseCreating()
        validInput = True
    else:
        print("enter a valid option")
        validInput = False

print("danke for doing sudoku-y stuff")    # mandatory gratitude giving
    
