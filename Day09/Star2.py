# IMPORTS
import numpy as np
import math

def getBasinSize(row : int, col : int) -> list:
    global data, basinList
    basinList.append((row,col))
    updateNorthBasin(row, col)
    updateSouthBasin(row, col)
    updateEastBasin(row, col)
    updateWestBasin(row, col)
    return basinList

def updateNorthBasin(row : int, col : int) -> None:
    if row > 0 :
        if data[row-1, col] < 9 and checkNorth((row, col)) and (row-1, col) not in basinList:
            getBasinSize(row-1, col)

def updateSouthBasin(row : int, col : int) -> None:
    if row < data.shape[0]-1 :
        if data[row+1, col] < 9 and checkSouth((row, col)) and (row+1, col) not in basinList:
            getBasinSize(row+1, col)

def updateEastBasin(row : int, col : int) -> None:
    if col < data.shape[1]-1 :
        if data[row, col+1] < 9 and checkEast((row, col)) and (row, col+1) not in basinList:
            getBasinSize(row, col+1)

def updateWestBasin(row : int, col : int) -> None:
    if col > 0:
        if data[row, col-1] < 9 and checkWest((row, col)) and (row, col-1) not in basinList:
            getBasinSize(row, col-1)
    
def checkNorth(pos : tuple) -> bool:
    global data
    return data[pos[0], pos[1]] < data[pos[0]-1, pos[1]] if pos[0] > 0 else True

def checkSouth(pos : tuple) -> int:
    global data
    return data[pos[0], pos[1]] < data[pos[0]+1, pos[1]] if pos[0] < data.shape[0]-1 else True

def checkEast(pos : tuple) -> bool:
    global data
    return data[pos[0], pos[1]] < data[pos[0], pos[1]+1] if pos[1] < data.shape[1]-1 else True

def checkWest(pos : tuple) -> bool:
    global data
    return data[pos[0], pos[1]] < data[pos[0], pos[1]-1] if pos[1] > 0 else True

def findBasins() -> list:
    global data
    basins : list = []
    for row in range(data.shape[0]):
        for col in range(data.shape[1]):
            if isBasin((row, col)): basins.append((row, col)) 
    return basins

def isBasin(pos : tuple) -> bool:
    return  checkNorth(pos) and \
            checkSouth(pos) and \
            checkWest(pos) and \
            checkEast(pos) 

if __name__ == '__main__':
    global data, basinList
    # TEST INPUT
    '''
    data = np.matrix([
        [2, 1, 9, 9, 9, 4, 3, 2, 1, 0],
        [3, 9, 8, 7, 8, 9, 4, 9, 2, 1],
        [9, 8, 5, 6, 7, 8, 9, 8, 9, 2],
        [8, 7, 6, 7, 8, 9, 6, 7, 8, 9],
        [9, 8, 9, 9, 9, 6, 5, 6, 7, 8]
    ])
    '''
    file = open('data.txt')
    file_data = file.readlines()
    file.close()
    data = []
    file_data = [line.split() for line in file_data]
    for line in file_data:
        for n in line:
            data.append([int(x) for x in n])
    
    data : np.matrix = np.matrix(data)
    res : int = 0
    basins_pos : list = findBasins()
    basins_size : list = []
    for pos in basins_pos:
        basinList : list = []
        basins_size.append(len(getBasinSize(pos[0], pos[1])))
    print(f'RES: {math.prod(sorted(basins_size, reverse=True)[:3])}')