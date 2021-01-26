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

def findROIForNumber(ROI):
    (height,width,depth) = ROI.shape

    bottomFound = False
    topFound = False
    leftFound = False
    rightFound = False

    for i in range(height):
        for j in range(width):
            (B,G,R) = ROI[i,j]
            if B < 200 and G < 200 and R < 200 and topFound == False:
                topPixel = i
            (B,G,R) = ROI[height-i-1,width-j-1]
            if B < 200 and G < 200 and R < 200 and bottomFound == False:
                bottomPixel = height-i-1
            (B,G,R) = ROI[j,i]
            if B < 200 and G < 200 and R < 200 and leftFound == False:
                leftPixel = j
            (B,G,R) = ROI[width-j-1,height-i-1]
            if B < 200 and G < 200 and R < 200 and rightFound == False:
                rightPixel = width-j-1
    #test = ROI[rightPixel:leftPixel,bottomPixel:topPixel]
    test = ROI[bottomPixel:topPixel,rightPixel:leftPixel]
    #TLPP = [topPixel,leftPixel]
    #BRPP = [bottomPixel,rightPixel]
    #test = ROI[TLPP[1]:BRPP[1],TLPP[0]:BRPP[0]]
    #test2 = 3
    print(height,width)
    print(topPixel,bottomPixel,leftPixel,rightPixel)
    print(test)
    cv2.imshow("new",test)
                




def determineNumber(ROI):
    numberReigon = findROIForNumber(ROI)
    return 'x'

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
    findROIForNumber(ROI)
    nine = ROI
    #print(nine)
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

##f = open("Numbers_For_Image_Recognition.txt","r")
##x = f.read()
##print(x)
##
##print(x[0][1])
##counter = 0
##for i in range(13):
##    for j in range(13):
##        for k in range(2):
##            if nine[i][j][k] == x[i][j][k]:
##                counter += 1
##print(counter)

'''
convert to greyscale first?
to get text from image, detect the number and crop so the entire number takes up the whole box then resize to a set amount. then have a base reference and compare the two numpy arrays.
if still comes back as not matching (perhaps due to different font), check each item in the numpy array to see which is most similar and perhaps say if there is more than 10 (??) pixels different, it's not correct
https://www.pyimagesearch.com/2018/07/19/opencv-tutorial-a-guide-to-learn-opencv/
https://medium.com/programming-fever/license-plate-recognition-using-opencv-python-7611f85cdd6c ?
(for ROI crap) https://blog.electroica.com/select-roi-or-multiple-rois-bounding-box-in-opencv-python/
'''
