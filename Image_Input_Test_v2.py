#~~~~~ v2, with the code for finding the number tidied up, so work on identifying it ~~~~~#

import cv2
from Sudoku_Generator_v2 import print2DSudokuGrid

def resizeImage(image,newSize):     # resizing it means theres less to process and itll be a standard size
    resizedGrid = cv2.resize(image,(newSize,newSize))
    return resizedGrid

def determineIfSquareHasNumber(square):
    (height,width,depth) = square.shape
    blackCount = 0
    
    for i in range(height):
        for j in range(width):
            (B, G, R) = square[i,j]
            if B < 200 and G < 200 and R < 200:
                print("number")
                return True
    return False

def locateItem(image):
    (height,width,depth) = image.shape

    bottomFound = False
    topFound = False
    leftFound = False
    rightFound = False

    for i in range(height):
        for j in range(width):
            (B,G,R) = image[i,j]
            if B < 200 and G < 200 and R < 200 and topFound == False:
                topPixel = i
            (B,G,R) = image[height-i-1,width-j-1]
            if B < 200 and G < 200 and R < 200 and bottomFound == False:
                bottomPixel = height-i-1
            (B,G,R) = image[j,i]
            if B < 200 and G < 200 and R < 200 and leftFound == False:
                leftPixel = j
            (B,G,R) = image[width-j-1,height-i-1]
            if B < 200 and G < 200 and R < 200 and rightFound == False:
                rightPixel = width-j-1
    
    newImage = image[bottomPixel:topPixel,rightPixel:leftPixel]
    
    return newImage

def determineNumber(square):
    numberRegion = locateItem(square)
    #print(numberRegion)#
    #cv2.imshow("number region",numberRegion)#
    return 'x'

def analyseIndividualSquares(sudokuGridImage):
    sudokuGrid2D = []
    for i in range(9):
        tempArray1 = []
        for j in range(9):
            ROI = sudokuGridImage[(i*17)+2:(16+(i*17)),(j*17)+2:(16+(j*17))]
            numberPresent = determineIfSquareHasNumber(ROI)
            if numberPresent == True:
                tempArray1.append(determineNumber(ROI))
            else:
                tempArray1.append(0)
        sudokuGrid2D.append(tempArray1)
    return sudokuGrid2D
                

sudokuGridImage = cv2.imread("Sudoku_Image_1.png")
cv2.imshow("original grid image",sudokuGridImage)#

newGridImage = resizeImage(locateItem(sudokuGridImage),153)
#cv2.imshow("cropped grid",newGridImage)#

sudokuGrid2D = analyseIndividualSquares(newGridImage)
print2DSudokuGrid(sudokuGrid2D,3)
