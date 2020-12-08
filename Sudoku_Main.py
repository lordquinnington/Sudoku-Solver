#~~~~~ Sudoku Main ~~~~~#

################################################ main program ################################################

validInput = False
while not validInput:
    option = input("pick an option: \n1) solve a grid \n2) generate a 9x9 grid \noption >")
    if option == '1':
        from Sudoku_Solver import initialiseSolving
        initialiseSolving()
        validOption = True
    elif option == '2':
        from Sudoku_Generator import initialiseGenerating
        initialiseGenerating()
        validOption = True
    else:
        print("enter a valid option")
        validOption = False

print("danke for doing sudoku-y stuff")
    
