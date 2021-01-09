#~~~~~ test to see if the program can take an image of a sudoku grid ~~~~~#

import cv2
#import pytesseract
from Sudoku_Generator_v2 import print2DSudokuGrid
#pytesseract.pytesseract.tesseract_cmd = r"C:\Users\Matthew's Desktop\AppData\Local\Programs\Tesseract-OCR\tesseract.exe"

sudokuGridImage = cv2.imread("Sudoku_Image_1.png")
cv2.imshow("image",sudokuGridImage)
(height,width,depth) = sudokuGridImage.shape

def findROI(image,TLPixelPos,BRPixelPos):
    ROI = image[TLPixelPos[1]:BRPixelPos[1],TLPixelPos[0]:BRPixelPos[0]]
    return ROI

def resizeMainGrid(image):     # resizing it means theres less to process and itll be a standard size
    resizedGrid = cv2.resize(image,(153,153))
    return resizedGrid

def determineIfSquareHasNumber(square):
    (height,width,depth) = square.shape
    blackCount = 0
    for i in range(height):
        for j in range(width):
            (B, G, R) = square[i,j]
            if B < 200 and G < 200 and R < 200:
                blackCount += 1
    if blackCount > 1:
        return True
    return False
    

def locateMainGrid(sudokuImageGrid,height,width):
    topLeftFound = False
    for i in range(height):
        for j in range(width):
            (B,G,R) = sudokuGridImage[i,j]
            if B < 200 and G < 200 and R < 200 and topLeftFound == False:
                topLeftPixelPos = [i,j]
                topLeftFound = True            
    bottomRightFound = False
    for i in range(height):
        for j in range(width):
            (B,G,R) = sudokuGridImage[height-i-1,width-j-1]
            if B < 200 and G < 200 and R < 200 and bottomRightFound == False:
                bottomRightPixelPos = [height-i-1,width-j-1]
                bottomRightFound = True            
    return topLeftPixelPos, bottomRightPixelPos

def analyseIndividualSquares(sudokuGridImage):
    sudokuGrid2D = []
    for i in range(9):
        tempArray1 = []
        for j in range(9):
            ROI = sudokuGridImage[(i*17)+2:(16+(i*17)),(j*17)+2:(16+(j*17))]
            numberPresent = determineIfSquareHasNumber(ROI)
            if numberPresent == True:
                tempArray1.append('x')
            else:
                tempArray1.append(0)
        sudokuGrid2D.append(tempArray1)
    cv2.imshow("roi",ROI)
    nine = ROI
    print(nine)
    f = open("Numbers_For_Image_Recognition.txt","w")
    f.write(str(nine))
    f.close()
    return sudokuGrid2D, nine
                                                                


TLPixelPos, BRPixelPos = locateMainGrid(sudokuGridImage,height,width)

sudokuGridImage = findROI(sudokuGridImage,TLPixelPos,BRPixelPos)

sudokuGridImage = resizeMainGrid(sudokuGridImage)
cv2.imshow("smaller",sudokuGridImage)
sudokuGrid2D, nine = analyseIndividualSquares(sudokuGridImage)
print2DSudokuGrid(sudokuGrid2D,3)

f = open("Numbers_For_Image_Recognition.txt","r")
x = f.read()
print(x)

if nine == x:
    print("yay")
else:
    print("noaw")

counter = 0
for i in range(14):
    for j in range(14):
        for k in range(3):
            if nine[i][j] == x[i][j]:
                counter += 1
print(counter)
'''
convert to greyscale first?
to get text from image, detect the number and crop so the entire number takes up the whole box then resize to a set amount. then have a base reference and compare the two numpy arrays.
if still comes back as not matching (perhaps due to different font), check each item in the numpy array to see which is most similar and perhaps say if there is more than 10 (??) pixels different, it's not correct
https://www.pyimagesearch.com/2018/07/19/opencv-tutorial-a-guide-to-learn-opencv/
https://medium.com/programming-fever/license-plate-recognition-using-opencv-python-7611f85cdd6c ?
'''