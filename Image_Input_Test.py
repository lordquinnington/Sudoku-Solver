#~~~~~ test to see if the program can take an image of a sudoku grid ~~~~~#

import cv2

sudokuGridImage = cv2.imread("Sudoku_Image_1.png")
cv2.imshow("image",sudokuGridImage)
(height,width,depth) = sudokuGridImage.shape
print("width=",width,", height=",height,", depth=",depth)
(B, G, R) = sudokuGridImage[0, 0]
print("R={}, G={}, B={}".format(R, G, B))

#roi = sudokuGridImage[4:32, 4:32]
#cv2.imshow("ROI", roi)

def locateMainGrid(sudokuImageGrid,height,width):
    topLeftFound = False
    for i in range(height):
        for j in range(width):
            (B,G,R) = sudokuGridImage[i,j]
            if B < 200 and G < 200 and R < 200 and topLeftFound == False:
                topLeftPixelPos = [i,j]
                topLeftFound = True            
    print(topLeftPixelPos)

    bottomRightFound = False
    for i in range(height):
        for j in range(width):
            (B,G,R) = sudokuGridImage[height-i-1,width-j-1]
            if B < 200 and G < 200 and R < 200 and bottomRightFound == False:
                bottomRightPixelPos = [height-i-1,width-j-1]
                bottomRightFound = True            
    print(bottomRightPixelPos)
    return topLeftPixelPos, bottomRightPixelPos


TLPixelPos, BRPixelPos = locateMainGrid(sudokuGridImage,height,width)
test1 = sudokuGridImage.copy()
cv2.rectangle(test1, (TLPixelPos[0],TLPixelPos[1]), (BRPixelPos[0],BRPixelPos[1]), (0,0,255),2)
cv2.imshow("hopefully...",test1)


#edged = cv2.Canny(image,0,259)
#cv2.imshow("boundary",edged)

#test1 = sudokuGridImage.copy()
#cv2.rectangle(test1, (0,200), (259, 10), (0, 0, 255), 2)    # image, (dist left,dist from top), (dist from left,dist from top), (colour), line width
#cv2.imshow("rectangle",test1)
#img_rgb = cv2.cvtColor(roi, cv2.COLOR_BGR2RGB)
#img_rgb = Image.open('Sudoku_Image_1.png')
#number = pytesseract.image_to_string(img_rgb) # '--psm 11
#print("number:",number)


'''
convert to greyscale first?
to get text from image, detect the number and crop so the entire number takes up the whole box then resize to a set amount. then have a base reference and compare the two numpy arrays.
if still comes back as not matching (perhaps due to different font), check each item in the numpy array to see which is most similar and perhaps say if there is more than 10 (??) pixels different, it's not correct
'''
