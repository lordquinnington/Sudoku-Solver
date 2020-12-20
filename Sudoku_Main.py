#~~~~~ Sudoku Main ~~~~~#

################################################ main program ################################################

validInput = False
while not validInput:
    option = input("pick an option: \n1) solve a grid \n2) generate a complete grid \noption >")
    if option == '1':
        from Sudoku_Solver import initialiseSolving
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

print("danke for doing sudoku-y stuff")
    
