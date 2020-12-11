#~~~~~ convert from QQWing ~~~~~#

import csv

def convertFromQQWing(QQWing):
    gridArray2D = []
    for i in range(9):
        tempArray1 = []
        for j in range(9):
            if QQWing[9*i+j] == '.':
                tempArray1.append(0)    # or change the 0 for '' to write black spaces to the grid
            else:
                tempArray1.append(int(QQWing[9*i+j]))
        gridArray2D.append(tempArray1)
    return writeGridToCSV(gridArray2D)

def writeGridToCSV(gridArray2D):
    with open("Sudoku_Grid.csv","w",newline='') as gridFile:    # you can change the name of the file to makes to whatever your program not die
        toWrite = csv.writer(gridFile,delimiter=',')
        for row in gridArray2D:
            toWrite.writerow(row)

convertFromQQWing(list("7..21.....615....7.3.....46.....5......16........925..349..1.....79.3.5...2...7.."))    # copy and paste the line of dots and numbers from QQWing into here (taken as a parameter so you can call it from elsewhere)
