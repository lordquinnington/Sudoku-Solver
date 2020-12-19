#~~~~~ Sudoku Generator ~~~~~#

import random

################################################ generating functions ################################################

def generateCompletedGrid():
    newGrid = []
    # generate the initial random row
    rowNums = []
    options = [1,2,3,4,5,6,7,8,9]
    for i in range(9):
        rowNums.append(random.choice(options))
        options.remove(rowNums[i])
    # generate the shifted grid
    for i in range(3):
        print("---------------------------")#
        for j in range(3):
            if i != 0:
                if j == 0:
                    rowNums = rowNums[8:]+rowNums[:8]
                    print(rowNums)#
                else:
                    rowNums = rowNums[6:]+rowNums[:6]
                    print(rowNums)#
            else:
                rowNums = rowNums[6:]+rowNums[:6]
                print(rowNums)#
            newGrid.append(rowNums)
    print('\n')#
    # randomly rearrange the big rows
    bigRows = []
    for i in range(3):
        tempArray1 = []
        for j in range(3):
            tempArray1.append(newGrid[3*i+j])
            print("ta1>",tempArray1[j])#
        bigRows.append(tempArray1)
    print("br> ",bigRows)#
    newBigRowOrder = []
    options = [0,1,2]
    for i in range(3):
        x = random.choice(options)
        newBigRowOrder.append(bigRows[x])
        print("brx>",bigRows[x])#
        options.remove(x)
    print("nbro>",newBigRowOrder)#
    print("\n big rows>")#
    for i in range(3):#
        print("---------------------------")#
        for j in range(3):#
            print(newBigRowOrder[i][j])#
    # randomly rearrange the small rows inside the big rows
    newSmallRowOrder = []
    for i in range(3):
        tempArray1 = []
        options = [0,1,2]
        for j in range(3):
            x = random.choice(options)
            tempArray1.append(newBigRowOrder[i][x])
            options.remove(x)
        newSmallRowOrder.append(tempArray1)
    print("\n nsro>",newSmallRowOrder)
    print("\n small rows>")#
    for i in range(3):#
        print("---------------------------")#
        for j in range(3):#
            print(newSmallRowOrder[i][j])#
    # randomly rearrange the big columns
    bigColumnsTemp = []
    for i in range(9):
        tempArray1 = []
        for j in range(3):
            for k in range(3):
                tempArray1.append(newSmallRowOrder[j][k][i])
        bigColumnsTemp.append(tempArray1)
    print("\n bct>",bigColumnsTemp)#
    bigColumns = []
    for i in range(3):
        tempArray1 = []
        for j in range(3):
            tempArray1.append(bigColumnsTemp[3*i+j])
        bigColumns.append(tempArray1)
    print("\n bc>",bigColumns)#
    newBigColumnOrder = []
    options = [0,1,2]
    for i in range(3):
        x = random.choice(options)
        newBigColumnOrder.append(bigColumns[x])
        print("brx>",bigColumns[x])#
        options.remove(x)
    print("nbco>",newBigColumnOrder)#
    print("\n big columns>")#
    for i in range(3):#
        print("---------------------------")#
        for j in range(3):#
            print(newBigColumnOrder[i][j])#
    # randomly rearrange the small columns inside the big columns
    newSmallColumnOrder = []
    for i in range(3):
        tempArray1 = []
        options = [0,1,2]
        for j in range(3):
            x = random.choice(options)
            tempArray1.append(newBigColumnOrder[i][x])
            options.remove(x)
        newSmallColumnOrder.append(tempArray1)
    print("\n nsco>",newSmallColumnOrder)
    print("\n small columns>")#
    for i in range(3):#
        print("---------------------------")#
        for j in range(3):#
            print(newSmallColumnOrder[i][j])#        
    
    return newGrid
        
        
newGrid = generateCompletedGrid()
print('\n',newGrid)

'''perhaps generate some random numbers and then fill in the rest from randomly choosing the least possible numbers (or both, generate 1 and then fill some in and generate again (but that might be slower))'''
'''need to check for possible invalid inputs when randomly filling in so perhaps utilise the find numbers to remove function?'''
